#!/usr/bin/python3
from api import *

# example


def main():
    instance = API("") # api key here
    try:
        print(instance.get_balance()) # call get balance
    except Exception as e: # catch any exceptions
        print(e)

if __name__ == '__main__':
    main()