import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_openai_connection():
    """Test OpenAI API connection"""
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ No OpenAI API key found in .env file")
        return False
    
    if api_key == "your_openai_api_key_here":
        print("❌ OpenAI API key is still placeholder value")
        print("Please update .env file with your actual API key")
        return False
    
    print(f"🔑 API Key found: {api_key[:20]}...")
    
    try:
        # Initialize OpenAI client
        client = openai.OpenAI(api_key=api_key)
        
        # Test with a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello, can you hear me?"}
            ],
            max_tokens=50
        )
        
        result = response.choices[0].message.content
        print("✅ OpenAI API working!")
        print(f"🤖 Response: {result}")
        return True
        
    except openai.AuthenticationError:
        print("❌ OpenAI API authentication failed - invalid API key")
        return False
    except openai.RateLimitError:
        print("❌ OpenAI API rate limit exceeded")
        return False
    except Exception as e:
        print(f"❌ OpenAI API error: {e}")
        return False

if __name__ == "__main__":
    test_openai_connection()
