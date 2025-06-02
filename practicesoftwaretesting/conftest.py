# -*- coding: utf-8 -*-


from . import credentials as c

from playwright.sync_api import Page, Playwright, expect

from pathlib import Path

import pytest


@pytest.fixture(scope="function")
def customer_01_auth(page: Page, playwright: Playwright):
    print('fixture ran!!!!')
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()  # is that necessary?

    customer_01_auth_file = ".auth/customer01.json"

    playwright.selectors.set_test_id_attribute("data-test")

    page.goto("https://practicesoftwaretesting.com/auth/login")
    page.get_by_test_id("email").fill(
        c.get_user_data(c.USER_CUSTOMER, "email")
    )
    page.get_by_test_id("password").fill(
        c.get_user_data(c.USER_CUSTOMER, "password")
    )
    page.get_by_test_id("login-submit").click()

    user_name = c.get_user_data(c.USER_CUSTOMER, "name")
    user_surname = c.get_user_data(c.USER_CUSTOMER, "surname")
    expect(page.get_by_test_id("nav-menu")).to_contain_text(
        f"{user_name} {user_surname}"
    )

    Path(".auth").mkdir(exist_ok=True)
    with open(customer_01_auth_file, "w"):
        storage = context.storage_state(path=customer_01_auth_file)

    context.close()
    browser.close()

    return customer_01_auth_file
