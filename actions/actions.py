# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from cgitb import text
from os import link
from re import template
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        Link= " https://www.space.com/"  
        dispatcher.utter_message( template="utter_response1.4",link= " https://www.space.com/"  ) 
        # dispatcher.utter_template("utter_response1.4",tracker,link=Link)

        return []

        # --------------------   MASTER LINK SECTION ----------------------------------

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "Master_link_admission"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message( template="utter_response_MASTER_LINK" , link= " https://www.space.com/"  ) 
        # dispatcher.utter_template("utter_response1.4",tracker,link=Link)

        return []
