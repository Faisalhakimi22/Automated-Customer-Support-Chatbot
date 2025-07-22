#!/usr/bin/env python3
"""
Startup script for the Automated Customer Support Chatbot
This script starts both Rasa servers and the Streamlit frontend
"""

import subprocess
import time
import sys
import requests
import os
from pathlib import Path

def check_rasa_server(port=5005, max_attempts=10):
    """Check if Rasa server is running"""
    for attempt in range(max_attempts):
        try:
            response = requests.get(f"http://localhost:{port}/version", timeout=2)
            if response.status_code == 200:
                return True
        except:
            pass
        print(f"Waiting for Rasa server on port {port}... (attempt {attempt + 1}/{max_attempts})")
        time.sleep(2)
    return False

def start_rasa_action_server():
    """Start Rasa action server"""
    print("🚀 Starting Rasa Action Server...")
    try:
        # Start action server in background
        action_process = subprocess.Popen([
            "rasa", "run", "actions", 
            "--port", "5055",
            "--cors", "*"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        time.sleep(3)  # Give it time to start
        
        if action_process.poll() is None:  # Process is still running
            print("✅ Rasa Action Server started on port 5055")
            return action_process
        else:
            print("❌ Failed to start Rasa Action Server")
            return None
    except Exception as e:
        print(f"❌ Error starting action server: {e}")
        return None

def start_rasa_core_server():
    """Start Rasa core server"""
    print("🚀 Starting Rasa Core Server...")
    try:
        # Start core server in background
        core_process = subprocess.Popen([
            "rasa", "run", 
            "--enable-api",
            "--cors", "*",
            "--port", "5005"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for server to be ready
        if check_rasa_server(5005):
            print("✅ Rasa Core Server started on port 5005")
            return core_process
        else:
            print("❌ Rasa Core Server failed to start properly")
            core_process.terminate()
            return None
    except Exception as e:
        print(f"❌ Error starting core server: {e}")
        return None

def start_streamlit_app():
    """Start Streamlit frontend"""
    print("🚀 Starting Streamlit Frontend...")
    try:
        # Start Streamlit app
        streamlit_process = subprocess.Popen([
            "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "0.0.0.0"
        ])
        
        print("✅ Streamlit app started on http://localhost:8501")
        return streamlit_process
    except Exception as e:
        print(f"❌ Error starting Streamlit: {e}")
        return None

def main():
    """Main startup function"""
    print("🤖 Starting Automated Customer Support Chatbot...")
    print("=" * 50)
    
    # Check if model exists
    models_dir = Path("models")
    if not models_dir.exists() or not list(models_dir.glob("*.tar.gz")):
        print("❌ No trained model found!")
        print("Please run 'rasa train' first to train the model.")
        return
    
    processes = []
    
    try:
        # Start action server
        action_server = start_rasa_action_server()
        if action_server:
            processes.append(action_server)
        
        # Start core server
        core_server = start_rasa_core_server()
        if core_server:
            processes.append(core_server)
        else:
            print("❌ Cannot proceed without Rasa core server")
            return
        
        # Start Streamlit app
        streamlit_app = start_streamlit_app()
        if streamlit_app:
            processes.append(streamlit_app)
        
        print("\\n" + "=" * 50)
        print("🎉 Chatbot is running!")
        print("📱 Frontend: http://localhost:8501")
        print("🤖 Rasa API: http://localhost:5005")
        print("⚙️  Actions: http://localhost:5055")
        print("=" * 50)
        print("\\n📝 To stop all services, press Ctrl+C")
        
        # Wait for user interrupt
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\\n🛑 Stopping all services...")
            
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        # Clean up processes
        for process in processes:
            if process and process.poll() is None:
                print(f"Stopping process {process.pid}...")
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
        
        print("✅ All services stopped")

if __name__ == "__main__":
    main()
