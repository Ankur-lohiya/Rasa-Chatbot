# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import smtplib
# class ActionSendMail(Action):

#     def name(self) -> Text:
#         return "action_send_email"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         FROMADDR = "deepankur1002.cse18@chitkara.edu.in" #Sender Mail
#         LOGIN    = FROMADDR 
#         PASSWORD = "#Ankur1401"	# Write password of your mail
#         TOADDRS  = tracker.get_slot("email")	# Write receiver mail in list
#         # SUBJECT  = "Reservation of a table"

#         msg = "Your table is been reserved for "+tracker.get_slot("num_count")+" people at "+tracker.get_slot("hour") # Message you want to send

#         server = smtplib.SMTP('smtp.gmail.com:587')
#         server.set_debuglevel(1)
#         server.ehlo()	# Identify yourself to an ESMTP server using EHLO
#         server.starttls()	# To upgarde insecure connection to sceure connection
#         server.login(LOGIN, PASSWORD)	# To login 
#         server.sendmail(FROMADDR, TOADDRS, msg)
#         server.quit()
#         emailAddr=tracker.get_slot('email')
#         print(emailAddr)
#         return []
