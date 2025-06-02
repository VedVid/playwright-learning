# -*- coding: utf-8 -*-


from .. import credentials as c

from playwright.sync_api import Page, expect


def test_login(page: Page) -> None:
    page.goto("https://practicesoftwaretesting.com/")
    page.locator("[data-test=\"nav-sign-in\"]").click()
    page.locator("[data-test=\"email\"]").click()
    page.locator("[data-test=\"email\"]").fill(
        c.get_user_data(c.USER_CUSTOMER, "email")
    )
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill(
        c.get_user_data(c.USER_CUSTOMER, "password")
    )
    page.locator("[data-test=\"login-submit\"]").click()
    user_name = c.get_user_data(c.USER_CUSTOMER, "name")
    user_surname = c.get_user_data(c.USER_CUSTOMER, "surname")
    expect(page.locator("[data-test=\"nav-menu\"]")).to_contain_text(
        f"{user_name} {user_surname}"
    )
    page.locator("[data-test=\"page-title\"]").click()
    expect(page.locator("[data-test=\"page-title\"]")).to_contain_text("My account")
