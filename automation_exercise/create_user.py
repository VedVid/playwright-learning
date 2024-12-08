# -*- coding: utf-8 -*-


import requests

import credentials as c


def create_user():
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
