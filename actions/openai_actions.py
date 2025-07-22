from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

LLM_API_URL = os.getenv("LLM_API_URL", "http://localhost:8000/chat")

class ActionAskGPT(Action):
    def name(self) -> Text:
        return "action_ask_gpt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get the latest user message
        user_message = tracker.latest_message.get('text', 'No message provided')
        
        # Build conversation history (last 5 turns)
        conversation_history = []
        for event in reversed(tracker.events):
            if len(conversation_history) >= 10:  # 5 user + 5 bot
                break
            if event.get('event') == 'user' and event.get('text'):
                conversation_history.append({"role": "user", "content": event.get('text')})
            elif event.get('event') == 'bot' and event.get('text'):
                conversation_history.append({"role": "assistant", "content": event.get('text')})
        
        conversation_history.reverse()
        
        # Prepare messages for LLM API
        messages = conversation_history
        
        try:
            payload = {
                "message": user_message,
                "history": messages,
                "model": os.getenv("OLLAMA_MODEL", "mistral")
            }
            response = requests.post(LLM_API_URL, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            llm_response = data.get("response", "Sorry, I didn't understand that.")
            dispatcher.utter_message(text=llm_response)
        except Exception as e:
            dispatcher.utter_message(text="I'm having trouble connecting to my local LLM. Please try again later.")
            print(f"LLM API Error: {e}")
        
        return []