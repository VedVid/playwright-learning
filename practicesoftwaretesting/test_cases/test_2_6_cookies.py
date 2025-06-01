# -*- coding: utf-8 -*-


from .. import credentials as c

from playwright.sync_api import Page, Playwright, expect


def test_customer_01_is_signed_in(page: Page, playwright: Playwright, customer_01_auth) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state=customer_01_auth)
    page = context.new_page()

    playwright.selectors.set_test_id_attribute("data-test")

    page.goto("https://practicesoftwaretesting.com/")
    expect(page.get_by_test_id("nav-sign-in")).not_to_be_visible()
    user_name = c.get_user_data(c.USER_CUSTOMER, "name")
    user_surname = c.get_user_data(c.USER_CUSTOMER, "surname")
    expect(page.get_by_test_id("nav-menu")).to_contain_text(
        f"{user_name} {user_surname}"
    )

    context.close()
    browser.close()
