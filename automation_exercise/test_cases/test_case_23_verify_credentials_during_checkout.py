# -*- coding: utf-8 -*-


from .. import credentials as c
from ..actions import goto_page, new_user_form_fill_and_confirm
from ..user_management import delete_user

from playwright.sync_api import Page, expect


def setup_function():
    delete_user()


def test_verify_credentials_during_checkout(page: Page) -> None:
    goto_page(page)

    page.get_by_role("link", name="Signup / Login").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(c.USER_NAME)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_role("button", name="Signup").click()
    new_user_form_fill_and_confirm(page)
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    expect(page.get_by_text(f"Logged in as {c.USER_NAME}")).to_be_visible()
    page.locator(".productinfo > .btn").first.click()
    page.get_by_role("link", name="View Cart").click()
    page.get_by_text("Proceed To Checkout").click()

    # Test case instructs to ensure that the data during checkout is the same
    # as data passed during user creation.
    # This suggest manual asserting, but I decided agains of it,
    # as getting locators by text / user credentials will fail anyway
    # if data during checkout do not match specified credentials.
    expect(page.get_by_role("heading", name="Review Your Order")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.TITLE} {c.FIRST_NAME} {c.LAST_NAME}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.COMPANY}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.ADDRESS}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.ADDRESS_2}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.CITY} {c.STATE} {c.ZIPCODE}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.COUNTRY}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.MOBILE}")).to_be_visible()


def teardown_function():
    delete_user()
