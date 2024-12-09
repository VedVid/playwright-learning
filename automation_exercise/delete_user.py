# -*- coding: utf-8 -*-


import requests

from .credentials import EMAIL_ADDRESS, PASSWORD


def delete_user():
    params = {"email": EMAIL_ADDRESS, "password": PASSWORD}
    response = requests.delete(
        "https://automationexercise.com/api/deleteAccount",
        data=params
    )
    data = response.json()
    assert(data["responseCode"] in [200, 404])
    assert(data["message"] in ["Account deleted!", "Account not found!"])
    return (data["responseCode"], data["message"])
