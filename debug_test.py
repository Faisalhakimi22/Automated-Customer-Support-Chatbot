import requests
import json

def test_rasa_with_different_messages():
    """Test Rasa with various message types"""
    messages = [
        "hello",
        "hi there",
        "good morning",
        "I need help",
        "what can you do",
        "bye"
    ]
    
    print("Testing Rasa with different messages...")
    print("-" * 50)
    
    for message in messages:
        try:
            payload = {"sender": "test_user", "message": message}
            print(f"\n📤 Sending: '{message}'")
            
            response = requests.post(
                "http://localhost:5005/webhooks/rest/webhook",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if result:
                    for msg in result:
                        print(f"🤖 Bot: {msg.get('text', 'No text')}")
                else:
                    print("🔍 Empty response - checking why...")
                    # Try to parse message directly
                    parse_response = requests.post(
                        "http://localhost:5005/model/parse",
                        json={"text": message},
                        timeout=10
                    )
                    if parse_response.status_code == 200:
                        parse_result = parse_response.json()
                        print(f"   Intent: {parse_result.get('intent', {}).get('name', 'unknown')}")
                        print(f"   Confidence: {parse_result.get('intent', {}).get('confidence', 0):.2f}")
                    else:
                        print("   Could not parse message")
            else:
                print(f"❌ HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 50)

def check_model_info():
    """Get information about the loaded model"""
    try:
        response = requests.get("http://localhost:5005/status", timeout=5)
        if response.status_code == 200:
            status = response.json()
            print("📊 Rasa Status:")
            print(f"   Model: {status.get('model_file', 'Unknown')}")
            print(f"   Loaded: {status.get('model_id', 'Unknown')}")
            print(f"   Fingerprint: {status.get('fingerprint', 'Unknown')}")
        else:
            print("❌ Could not get status")
    except Exception as e:
        print(f"❌ Status error: {e}")

if __name__ == "__main__":
    check_model_info()
    print()
    test_rasa_with_different_messages()
