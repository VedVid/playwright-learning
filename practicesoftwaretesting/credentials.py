# -*- coding: utf-8 -*-


from typing import Dict


USER_ADMIN: Dict[str, str] = {
    "name": "John",
    "surname": "Doe",
    "role": "admin",
    "email": "admin@practicesoftwaretesting.com",
    "password": "welcome01"
}

USER_CUSTOMER: Dict[str, str] = {
    "name": "Jane",
    "surname": "Doe",
    "role": "user",
    "email": "customer@practicesoftwaretesting.com",
    "password": "welcome01"
}

USER_CUSTOMER_2: Dict[str, str] = {
    "name": "Jack",
    "surname": "Howe",
    "role": "user",
    "email": "customer2@practicesoftwaretesting.com",
    "password": "welcome01"
}


USER_FIELDS = ["name", "surname", "role", "email", "password"]


def get_user_data(user: Dict[str, str], data: str):
    if not data:
        raise ValueError("Data type to be returned is not specified.")
    if data not in USER_FIELDS:
        raise ValueError("Specified data type to be returned is incorrect.")

    return user[data]


VERSIONS = ["1", "2", "3", "4", "5", "5 (with bugs)"]


def get_url_data(version: str):
    if version not in VERSIONS:
        raise ValueError("Incorrect version string passed.")

    app_subdomain = f"v{version}."
    api_subdomain = f"api-v{version}."
    if version == "5":
        app_subdomain = ""
        api_subdomain = "api."
    elif version == "5 (with bugs)":
        app_subdomain = "bugs."
        api_subdomain = "api-with-bugs."

    d = Dict[str, str] = {
        "description": "Sprint {version}",
        "application": f"https://{app_subdomain}practicesoftwaretesting.com",
        "api": f"https://{api_subdomain}practicesoftwaretesting.com",
        "swagger": f"https://{api_subdomain}practicesoftwaretesting.com"
    }

    return d
