# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import sqlite3
from typing import Any, Text, Dict, List

# import arrow 
# import dateparser
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

conn = sqlite3.connect('rasa.db')
c = conn.cursor() 

class queryActivityInfor(Action):

    def name(self) -> Text:
        return "action_activity_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        activity_name =  tracker.get_slot("activity_name")  
        print(activity_name)
        # conn = sqlite3.connect('rasa.db')
        c = conn.cursor()   
        c.execute("SELECT * from activity WHERE name = ?",(activity_name,))
        result = c.fetchone()
        print(result)
        if result != None:
            dispatcher.utter_message(text=f"Activity name: {result[0]} \n start date: \n ticket price {result[2]} \n organizer: {result[3]} \n description: {result[4]} \n")
        else:
            dispatcher.utter_message(text=f"{activity_name} not exist")
        c.close()

        # dispatcher.utter_message(text="Hello World!")

        return [SlotSet("activity_name",None)]

class quaryUser(Action):

    def name(self) -> Text:
        return "initializing_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        username =  tracker.get_slot("user_name")  
        print(username)
        # conn = sqlite3.connect('rasa.db')
        c = conn.cursor()   
        c.execute("SELECT * from customer WHERE name = ?",(username,))
        result = c.fetchone()
        print(result)
        if result != None:
            dispatcher.utter_message(text=f"Hello {username}")
        else:
            c.execute("INSERT INTO customer(name,gender,STU_EMAIL) VALUES(?,?,?)",(str(username),int(1),"123@gmail.com"))
            # conn.commit()
            dispatcher.utter_message(text=f"you are a new user! We set up an account for you. your name is {username}")
        conn.commit()
        c.close()

        return []


class quaryAllActivity(Action):

    def name(self) -> Text:
        return "action_activity_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # conn = sqlite3.connect('rasa.db')
        c = conn.cursor()   
        c.execute("SELECT name from activity")
        result = c.fetchall()
        print(result[0])
        res = "activity name list:"

        for re in result:  
            res = res + "\n" + str(re[0])

        print(res)
        dispatcher.utter_message(text=res)
        c.close()

        return []

class bookActivity(Action):

    def name(self) -> Text:
        return "action_book_activity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        activity_name =  tracker.get_slot("activity_name")  
        print(activity_name)
        user_name =  tracker.get_slot("user_name")  
        print(user_name)
        c = conn.cursor()   
        c.execute("SELECT * from activity WHERE name = ?",(activity_name,))
        result = c.fetchone()
        print(result)
        if result != None:
            c.execute("INSERT INTO book(activity_name,user_name) VALUES(?,?)",(activity_name,user_name))
            
            dispatcher.utter_message(text=f"The subscription to activity {activity_name} succeeded")
        else:
            dispatcher.utter_message(text=f"{activity_name} not exist")
        conn.commit()
        c.close()

        return []

class bookList(Action):

    def name(self) -> Text:
        return "action_book_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name =  tracker.get_slot("user_name")  
        print(user_name)
        c = conn.cursor()   
        c.execute("SELECT * FROM book WHERE user_name = ?",(user_name,))
        result = c.fetchall()
        print(result[0])
        res = "your book list:"

        for re in result:  
            res = res + "\n" + "id:" + str(re[0]) + "   activity:" +  str(re[1])

        print(res)
        dispatcher.utter_message(text=res)
        c.close()

        return []

