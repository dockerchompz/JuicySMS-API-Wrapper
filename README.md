## API Wrapper for JuicySMS written in Python3
- features all functions provided in the API
### API wrapper includes:
```
get_balance() - returns balance; throws warning if balance is 0; returns an integer

reuse_number(orderid : int) - takes orderid of past order; allows for re-use of an old number; returns a string

skip_number(orderid : int) - takes orderid of an active order; allows a user to skip an active number; returns a string

cancel_order(orderid : int) - takes orderid of an active order; allows a user to cancel an active order; returns a string

get_sms(orderid : int) - takes orderid of an active order; allows a user to check the status of a phone number, if no message has been received user will be notified that the number is still pending; returns a string

make_order(serviceid : int, country : str) - takes a serviceid and a country (predefined class is supplied for countries); allows user to create an order; returns a string


```

### An example file has been provided under the name of:
- main.py




#
#
#
#
## ALL CREDITS GO TO JUICYSMS, ONLY THE CODE PROVIDED HERE HAS BEEN WRITTEN BY ME. ANYTHING RELATED TO THEIR SITE IS THEIR PROPERTY, NOT MINE.
