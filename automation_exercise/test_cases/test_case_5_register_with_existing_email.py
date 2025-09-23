# -*- coding: utf-8 -*-


from ..actions import goto_page
from ..create_user import create_user
from ..delete_user import delete_user

from playwright.sync_api import Page, expect


def setup_function():
    delete_user()
    create_user()


def test_register_user_with_existing_email(page: Page):
    goto_page(page)
    page.locator("li").filter(has_text="Signup / Login").click()
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Ved")
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill("ved@example.com")
    page.get_by_role("button", name="Signup").click()
    expect(page.get_by_text("Email Address already exist!")).to_be_visible()


def teardown_function():
    delete_user()
