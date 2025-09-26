# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from .. import credentials as c
from ..actions import goto_page, handle_card_payment
from ..user_management import create_user, delete_user


def setup_function():
    delete_user()
    create_user()


def test_download_invoice(page: Page) -> None:
    goto_page(page)

    page.locator("li").filter(has_text="Signup / Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(f"{c.EMAIL_ADDRESS}")
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(f"{c.PASSWORD}")
    page.get_by_role("button", name="Login").click()

    page.locator(".productinfo > .btn").first.click()
    page.get_by_role("link", name="View Cart").click()
    page.get_by_text("Proceed To Checkout").click()
    page.get_by_role("link", name="Place Order").click()

    handle_card_payment(page, should_continue=False)
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download Invoice").click()
    download = download_info.value
    print(download)

    page.locator("li").filter(has_text="Delete Account").click()
    page.get_by_role("link", name="Continue").click()
