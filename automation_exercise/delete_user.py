# -*- coding: utf-8 -*-


import requests

from .credentials import EMAIL_ADDRESS, PASSWORD


def delete_user():
    params = {"email": EMAIL_ADDRESS, "password": PASSWORD}
    requests.delete(
        "https://automationexercise.com/api/deleteAccount",
        data=params
    )
