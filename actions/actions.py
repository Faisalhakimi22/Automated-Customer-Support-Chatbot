from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.openai_actions import ActionAskGPT

class ActionQueryHotel(Action):
    def name(self) -> Text:
        return "action_query_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        pricerange = tracker.get_slot("hotel_hotel-pricerange")
        hotel_type = tracker.get_slot("hotel_hotel-type")
        area = tracker.get_slot("hotel_hotel-area")
        stars = tracker.get_slot("hotel_hotel-stars")
        
        # Build query context
        context = f"Find hotels with: price range={pricerange}, type={hotel_type}, area={area}, stars={stars}"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

class ActionQueryTrain(Action):
    def name(self) -> Text:
        return "action_query_train"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        departure = tracker.get_slot("train_train-departure")
        destination = tracker.get_slot("train_train-destination")
        day = tracker.get_slot("train_train-day")
        leaveat = tracker.get_slot("train_train-leaveat")
        
        # Build query context
        context = f"Find trains from {departure} to {destination} on {day} leaving at {leaveat}"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

class ActionQueryRestaurant(Action):
    def name(self) -> Text:
        return "action_query_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        pricerange = tracker.get_slot("restaurant_restaurant-pricerange")
        area = tracker.get_slot("restaurant_restaurant-area")
        food = tracker.get_slot("restaurant_restaurant-food")
        
        # Build query context
        context = f"Find restaurants with: price range={pricerange}, area={area}, food type={food}"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

class ActionQueryAttraction(Action):
    def name(self) -> Text:
        return "action_query_attraction"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        area = tracker.get_slot("attraction_attraction-area")
        attraction_type = tracker.get_slot("attraction_attraction-type")
        
        # Build query context
        context = f"Find attractions in {area} of type {attraction_type}"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

class ActionQueryHospital(Action):
    def name(self) -> Text:
        return "action_query_hospital"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        department = tracker.get_slot("hospital_hospital-department")
        
        # Build query context
        context = f"Find hospitals with {department} department"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

class ActionQueryTaxi(Action):
    def name(self) -> Text:
        return "action_query_taxi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        departure = tracker.get_slot("taxi_taxi-departure")
        destination = tracker.get_slot("taxi_taxi-destination")
        leaveat = tracker.get_slot("taxi_taxi-leaveat")
        
        # Build query context
        context = f"Book taxi from {departure} to {destination} leaving at {leaveat}"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

class ActionQueryBus(Action):
    def name(self) -> Text:
        return "action_query_bus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        departure = tracker.get_slot("bus_bus-departure")
        destination = tracker.get_slot("bus_bus-destination")
        day = tracker.get_slot("bus_bus-day")
        
        # Build query context
        context = f"Find bus from {departure} to {destination} on {day}"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

class ActionQueryPolice(Action):
    def name(self) -> Text:
        return "action_query_police"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extract relevant slots
        name = tracker.get_slot("police_police-name")
        
        # Build query context
        context = f"Find information about {name}"
        
        # Use GPT to generate response
        gpt_action = ActionAskGPT()
        return gpt_action.run(dispatcher, tracker, domain)

# Export all actions
__all__ = [
    'ActionAskGPT',
    'ActionQueryHotel',
    'ActionQueryTrain', 
    'ActionQueryRestaurant',
    'ActionQueryAttraction',
    'ActionQueryHospital',
    'ActionQueryTaxi',
    'ActionQueryBus',
    'ActionQueryPolice'
]