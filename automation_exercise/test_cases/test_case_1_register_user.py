# -*- coding: utf-8 -*-


from .. import credentials as c
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

    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    page.get_by_label(c.TITLE).check()
    expect(page.get_by_label("Name *", exact=True)).to_have_value(c.USER_NAME)
    expect(page.get_by_label("Email *", exact=True)).to_have_value(c.EMAIL_ADDRESS)
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill(c.PASSWORD)
    page.locator("#days").select_option(c.BIRTHDAY_DAY)
    page.locator("#months").select_option(c.BIRTHDAY_MONTH)
    page.locator("#years").select_option(c.BIRTHDAY_YEAR)
    page.get_by_label("Sign up for our newsletter!").check()
    page.get_by_label("Receive special offers from").check()
    page.get_by_label("First name *").click()
    page.get_by_label("First name *").fill(c.FIRST_NAME)
    page.get_by_label("Last name *").click()
    page.get_by_label("Last name *").fill(c.LAST_NAME)
    page.get_by_label("Company", exact=True).click()
    page.get_by_label("Company", exact=True).fill(c.COMPANY)
    page.get_by_label("Address *").click()
    page.get_by_label("Address *").fill(c.ADDRESS)
    page.get_by_label("Address 2").click()
    page.get_by_label("Address 2").fill(c.ADDRESS_2)
    page.get_by_label("Country *").select_option(c.COUNTRY)
    page.get_by_label("State *").click()
    page.get_by_label("State *").fill(c.STATE)
    page.get_by_label("City *").click()
    page.get_by_label("City *").fill(c.CITY)
    page.locator("#zipcode").click()
    page.locator("#zipcode").fill(c.ZIPCODE)
    page.get_by_label("Mobile Number *").click()
    page.get_by_label("Mobile Number *").fill(c.MOBILE)
    page.get_by_role("button", name="Create Account").click()

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
