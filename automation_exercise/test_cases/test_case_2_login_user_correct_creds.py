# -*- coding: utf-8 -*-


from .. import credentials as c
from ..create_user import create_user
from ..delete_user import delete_user

from playwright.sync_api import Playwright, expect


def setup_function():
    delete_user()
    create_user()


def test_login_user_correct_creds(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    expect(page.locator("body")).to_be_visible()
    page.locator("li").filter(has_text="Signup / Login").click()
    expect(page.locator("div").filter(has_text="Login to your account Login").nth(2)).to_be_visible()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(c.PASSWORD)
    page.get_by_role("button", name="Login").click()
    expect(page.locator("li").filter(has_text=f"Logged in as {c.USER_NAME}")).to_be_visible()
    page.locator("li").filter(has_text="Delete Account").click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()
