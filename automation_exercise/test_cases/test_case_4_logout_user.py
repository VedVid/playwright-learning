# -*- coding: utf-8 -*-


import re

from playwright.sync_api import Page, expect

from .. import credentials as c
from ..actions import goto_page
from ..user_management import create_user, delete_user


def setup_function():
    delete_user()
    create_user()


def test_logout_user(page: Page) -> None:
    goto_page(page)
    page.locator("li").filter(has_text="Signup / Login").click()
    expect(page.locator("div").filter(has_text="Login to your account Login").nth(2)).to_be_visible()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(c.PASSWORD)
    page.get_by_role("button", name="Login").click()
    expect(page.locator("li").filter(has_text=f"Logged in as {c.USER_NAME}")).to_be_visible()
    page.locator("li").filter(has_text="Logout").click()
    expect(page).to_have_url(re.compile("automationexercise.com/login"))
