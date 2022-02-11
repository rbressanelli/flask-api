from werkzeug.exceptions import BadRequest
from datetime import datetime
import re

from app.errors import (
    EmailUpdateError, 
    WrongEmailNameError, 
    NoStringError, 
    InvalidEmailError
    )


def date_maker():
    return datetime.now()


def phone_check(phone):
    checked_data = re.compile(r'^\([1-9]{2}\)(?:[2-9][0-9])[0-9]{3}\-[0-9]{4}$')
    if checked_data.match(phone) == None:
        raise BadRequest


def keys_check(request_data):
    class_request_keys = ['name', 'email', 'phone']
    if len(request_data) > 3:
        raise KeyError("Only the three correct fields should be informed")
    elif len({key:value for (key,value) in request_data.items() if key in class_request_keys}) < 3:
        raise KeyError("All three fields should be informed")
    elif {key:value for (key,value) in request_data.items() if type(value) != str}:
        raise NoStringError("The values must be string type")


def check_update_request(update_request):
    if len(update_request) > 1:
        raise EmailUpdateError("Only email field accepted")
    data = {key:value for (key,value) in update_request.items() if key=='email'}
    if not data:
        raise WrongEmailNameError("The key correct name is 'email'.")
    data = {key:value for key,value in update_request.items() if type(value) == str}
    if not data:
        raise NoStringError('The key value must be string')


def valid_email_checker(income_data):
    email_checker = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$') 
    if email_checker.match(income_data) == None:
        raise InvalidEmailError("Wrong email format")
