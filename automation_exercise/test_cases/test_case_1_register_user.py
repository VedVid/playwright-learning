# -*- coding: utf-8 -*-


from .. import credentials as c
from ..fill_new_user_form import fill_and_confirm as fill_form
from ..delete_user import delete_user

from playwright.sync_api import Page, expect


def setup_function():
    delete_user()


def test_register_user(page: Page):
    page.goto("http://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

    page.get_by_label("Consent", exact=True).click()

    page.get_by_role("link").filter(has_text="Signup").click()
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(c.USER_NAME)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_role("button").filter(has_text="Signup").click()

    fill_form(page)

    expect(page.get_by_text("Account Created")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    expect(page.get_by_text(f"Logged in as {c.USER_NAME}")).to_be_visible()
    page.locator("li").filter(has_text="Delete Account").click()

    expect(page.get_by_text("Account Deleted")).to_be_visible()
    page.get_by_role("link", name="Continue").click()


"""
No teardown function, as the test itself
ensures that the account is deleted.
"""
