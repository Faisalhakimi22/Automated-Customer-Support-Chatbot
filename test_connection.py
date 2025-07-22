import requests
import json

def test_rasa_connection():
    """Test if Rasa server is responding"""
    try:
        response = requests.get("http://localhost:5005/version", timeout=5)
        if response.status_code == 200:
            print("✅ Rasa server is running!")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"❌ Rasa server responded with status: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Rasa server on localhost:5005")
        print("Make sure to run: rasa run --enable-api --cors '*' --port 5005")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_message():
    """Test sending a message to Rasa"""
    if not test_rasa_connection():
        return
    
    try:
        message = {"sender": "test", "message": "hello"}
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json=message,
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Message sent successfully!")
            print(f"Bot response: {result}")
        else:
            print(f"❌ Failed to send message: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending message: {e}")

if __name__ == "__main__":
    print("Testing Rasa connection...")
    test_message()
