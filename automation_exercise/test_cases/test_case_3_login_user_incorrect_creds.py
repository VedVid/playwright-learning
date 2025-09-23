# -*- coding: utf-8 -*-


from .. import actions as a
from .. import credentials as c

from playwright.sync_api import Page, expect


def test_login_user_incorrect_creds(page: Page) -> None:
    a.goto_page(page)
    page.locator("li").filter(has_text="Signup / Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(c.INCORRECT_EMAIL_ADDRESS)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(c.INCORRECT_PASSWORD)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your email or password is")).to_be_visible()
