#!/usr/bin/python3
import requests

"""
author: rce01
version: 1.0
"""

class COUNTRIES:
    netherlands = "NL"
    united_states = "US"
    united_kingdom = "UK"


class API():
    """
    JuicySMS API wrapper
    """
    def __init__(self, API_KEY):
        if (API_KEY == None or API_KEY == ""):
            raise Exception("No API key has been provided.")
        else:
            self.API_KEY = str(API_KEY)

    def get_balance(self) -> int:
        """
        Get available account balance
        """
        request = requests.get("https://juicysms.com/api/getbalance?key={}".format(self.API_KEY))
        if (int(request.text) == 0):
            raise Exception("(WARNING) User has 0 balance")
        elif ("ERROR" in request.text):
            raise Exception("Unhandled exception has been raised.")
        elif ("NO_KEY_PROVIDED" in request.text):
            raise Exception("No API key has been provided.")
        else:
            return int(request.text)
    
    def reuse_number(self, orderid : int) -> str:
        """
        Re-use a phone number provided in a past order
        """
        request = requests.get("https://juicysms.com/api/reuse?key={}&orderId={}".format(self.API_KEY, str(orderid)))
        if ("NUMBER_OFFLINE" in request.text):
            raise Exception("Phone number is currently offline.")
        elif ("ORDER_ALREADY_OPEN_{}".format(str(orderid)) in request.text):
            raise Exception("Phone number is already in use in an active order.")
        elif ("NO_BALANCE" in request.text):
            raise Exception("Insufficient account balance.")
        elif ("ERROR" in request.text):
            raise Exception("Unhandled exception has been raised.")
        elif ("NO_KEY_PROVIDED" in request.text):
            raise Exception("No API key has been provided.")
        else:
            return request.text
        
    def skip_number(self, orderid : int) -> str:
        """
        Skip a phone number on an active order
        """
        request = requests.get("https://juicysms.com/api/skipnumber?key={}&orderId={}".format(self.API_KEY, str(orderid)))
        if ("ORDER_ALREADY_EXPIRED" in request.text):
            raise Exception("Order has already expired.")
        elif ("ORDER_ALREADY_COMPLETED" in request.text):
            raise Exception("Order has already completed")
        elif ("ERROR" in request.text):
            raise Exception("Unhandled exception has been raised.")
        elif ("NO_KEY_PROVIDED" in request.text):
            raise Exception("No API key has been provided.")
        else:
            return request.text
        
    def cancel_order(self, orderid : int) -> str:
        """
        Cancel an active order
        """
        request = requests.get("https://juicysms.com/api/cancelorder?key={}&orderId={}".format(self.API_KEY, str(orderid)))
        if ("ORDER_ALREADY_EXPIRED" in request.text):
            raise Exception("Order has already expired.")
        elif ("ORDER_ALREADY_COMPLETED" in request.text):
            raise Exception("Order has already completed.")
        elif ("ERROR" in request.text):
            raise Exception("Unhandled exception has been raised.")
        elif ("NO_KEY_PROVIDED" in request.text):
            raise Exception("No API key has been provided.")
        else:
            return request.text
        
    def get_sms(self, orderid : int) -> str:
        """
        Get sms message received on ordered number
        """
        request = requests.get("https://juicysms.com/api/getsms?key={}&orderId={}".format(self.API_KEY, str(orderid)))
        if ("ORDER_EXPIRED" in request.text):
            raise Exception("Order has expired.")
        elif ("WAITING" in request.text):
            raise Exception("Order is still awaiting an SMS message.")
        elif ("ERROR" in request.text):
            raise Exception("Unhandled exception has been raised.")
        elif ("NO_KEY_PROVIDED" in request.text):
            raise Exception("No API key has been provided.")
        else:
            return request.text
        
    def make_order(self, serviceid : int, country : str) -> str:
        """
        Create an order (COUNTRIES class used for country, serviceID's can be found on site. SERVICES class will be added in future updates)
        """
        request = requests.get("https://juicysms.com/api/makeorder?key={}&serviceId={}&country={}".format(self.API_KEY, str(serviceid), country))
        if ("NO_PHONE_AVAILABLE" in request.text):
            raise Exception("There is currently no phone number available for the specified service with country choice: {}.".format(country))
        elif ("ORDER_ALREADY_OPEN_" in request.text):
            raise Exception("There is currently already an order queued, please finish this order before ordering a new number.")
        elif ("NO_BALANCE" in request.text):
            raise Exception("Insufficient account balance.")
        elif ("ERROR" in request.text):
            raise Exception("Unhandled exception has been raised.")
        elif ("NO_KEY_PROVIDED" in request.text):
            raise Exception("No API key has been provided.")
        else:
            return request.text