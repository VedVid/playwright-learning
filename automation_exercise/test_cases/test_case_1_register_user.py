# -*- coding: utf-8 -*-


from ..actions import goto_page, new_user_form_fill_and_confirm
from .. import credentials as c
from ..delete_user import delete_user

from playwright.sync_api import Page, expect


def setup_function():
    delete_user()


def test_register_user(page: Page):
    goto_page(page)

    page.get_by_role("link").filter(has_text="Signup").click()
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(c.USER_NAME)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_role("button").filter(has_text="Signup").click()

    new_user_form_fill_and_confirm(page)

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
