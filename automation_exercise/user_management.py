# -*- coding: utf-8 -*-


import requests

from . import credentials as c


def create_user():
    '''
    This function creates a new user by using automationexercise's API.
    It uses user credentials specified in separate `credentials.py` file.

    Parameters
    ----------
    No parameters passed

    Returns
    -------
    tuple(integer, string)
        It contains response code and message returned by API.
    '''
    params = {
        "name": c.USER_NAME,
        "email": c.EMAIL_ADDRESS,
        "password": c.PASSWORD,
        "title": c.TITLE,
        "birth_date": c.BIRTHDAY_DAY,
        "birth_month": c.BIRTHDAY_MONTH,
        "birth_year": c.BIRTHDAY_YEAR,
        "firstname": c.FIRST_NAME,
        "lastname": c.LAST_NAME,
        "company": c.COMPANY,
        "address1": c.ADDRESS,
        "address2": c.ADDRESS_2,
        "country": c.COUNTRY,
        "zipcode": c.ZIPCODE,
        "state": c.STATE,
        "city": c.CITY,
        "mobile_number": c.MOBILE
    }

    response = requests.post(
        "https://automationexercise.com/api/createAccount",
        data=params
    )

    data = response.json()
    assert(data["responseCode"] in [201, 400])
    assert(data["message"] in ["User created!", "Email already exists!"])
    return (data["responseCode"], data["message"])


def delete_user():
    '''
    This function deletes existing user by using automationexercise's API.
    It uses user credentials specified in separate `credentials.py` file.
    It might be safely used even if we do not know if user exists -- in that case,
    an "Account not found!" message will be returned.

    Parameters
    ----------
    No parameters passed

    Returns
    -------
    tuple(integer, string)
        It contains response code and message returned by API.
    '''
    params = {"email": c.EMAIL_ADDRESS, "password": c.PASSWORD}
    response = requests.delete(
        "https://automationexercise.com/api/deleteAccount",
        data=params
    )
    data = response.json()
    assert(data["responseCode"] in [200, 404])
    assert(data["message"] in ["Account deleted!", "Account not found!"])
    return (data["responseCode"], data["message"])

