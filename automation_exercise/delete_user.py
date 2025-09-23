# -*- coding: utf-8 -*-


import requests

from .credentials import EMAIL_ADDRESS, PASSWORD


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
    params = {"email": EMAIL_ADDRESS, "password": PASSWORD}
    response = requests.delete(
        "https://automationexercise.com/api/deleteAccount",
        data=params
    )
    data = response.json()
    assert(data["responseCode"] in [200, 404])
    assert(data["message"] in ["Account deleted!", "Account not found!"])
    return (data["responseCode"], data["message"])
