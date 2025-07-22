#!/usr/bin/env python3
"""
Setup script for the Automated Customer Support Chatbot
This script helps initialize the project and check for common issues.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def check_env_file():
    """Check if .env file exists and has required variables."""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found")
        print("📝 Creating .env template...")
        with open(".env", "w") as f:
            f.write("# OpenAI API Configuration\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n\n")
            f.write("# Rasa Configuration\n")
            f.write("RASA_HOST=localhost\n")
            f.write("RASA_PORT=5005\n")
            f.write("ACTION_SERVER_PORT=5055\n")
        print("✅ .env template created. Please add your OpenAI API key.")
        return False
    
    with open(".env", "r") as f:
        content = f.read()
        if "your_openai_api_key_here" in content:
            print("❌ Please update your OpenAI API key in .env file")
            return False
    
    print("✅ .env file configured")
    return True

def install_dependencies():
    """Install project dependencies."""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def train_rasa_model():
    """Train the Rasa model."""
    print("🤖 Training Rasa model...")
    try:
        subprocess.run(["rasa", "train"], check=True, capture_output=True)
        print("✅ Rasa model trained successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to train Rasa model: {e}")
        return False
    except FileNotFoundError:
        print("❌ Rasa CLI not found. Please install Rasa first:")
        print("   pip install rasa")
        return False

def check_rasa_installation():
    """Check if Rasa is properly installed."""
    try:
        subprocess.run(["rasa", "--version"], check=True, capture_output=True)
        print("✅ Rasa CLI found")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Rasa CLI not found")
        return False

def main():
    """Main setup function."""
    print("🚀 Setting up Automated Customer Support Chatbot...\n")
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check .env file
    env_ok = check_env_file()
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check Rasa installation
    if not check_rasa_installation():
        print("📦 Installing Rasa...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "rasa"], 
                          check=True, capture_output=True)
            print("✅ Rasa installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install Rasa")
            sys.exit(1)
    
    # Train model
    if not train_rasa_model():
        print("⚠️  Model training failed, but you can try manually with 'rasa train'")
    
    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("1. Add your OpenAI API key to .env file")
    print("2. Start the action server: rasa run actions")
    print("3. Start the Rasa server: rasa run --enable-api")
    print("4. Run the Streamlit app: streamlit run app.py")
    
    if not env_ok:
        print("\n⚠️  Remember to configure your OpenAI API key in .env file!")

if __name__ == "__main__":
    main() 