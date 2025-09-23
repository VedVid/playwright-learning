# -*- coding: utf-8 -*-


from .. import credentials as c
from ..actions import goto_page, handle_card_payment, new_user_form_fill_and_confirm
from ..user_management import delete_user

from playwright.sync_api import Page, expect


def setup_function():
    delete_user()


def test_place_order_and_register(page: Page) -> None:
    goto_page(page)

    page.locator(".productinfo > .btn").first.click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.get_by_role("link", name=" Cart").click()
    expect(page.get_by_text("Shopping Cart")).to_be_visible()
    page.get_by_text("Proceed To Checkout").click()
    page.get_by_role("link", name="Register / Login").click()

    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(c.USER_NAME)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_role("button", name="Signup").click()

    new_user_form_fill_and_confirm(page)
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    expect(page.get_by_text(f"Logged in as {c.USER_NAME}")).to_be_visible()
    page.get_by_role("link", name=" Cart").click()
    page.get_by_text("Proceed To Checkout").click()

    expect(page.get_by_role("heading", name="Review Your Order")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.TITLE} {c.FIRST_NAME} {c.LAST_NAME}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.COMPANY}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.ADDRESS}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.ADDRESS_2}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.CITY} {c.STATE} {c.ZIPCODE}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.COUNTRY}")).to_be_visible()
    expect(page.locator("#address_delivery").get_by_text(f"{c.MOBILE}")).to_be_visible()

    expect(page.get_by_text("Rs.").nth(1)).to_be_visible()
    first_product_css = ".cart_price > p:nth-child(1)"
    first_product_price = page.locator(first_product_css).text_content()
    assert(first_product_price == page.get_by_text("Rs.").first.text_content())

    expect(page.get_by_role("row", name="Total Amount Rs.").get_by_role("paragraph")).to_be_visible()
    total_price = page.get_by_role("row", name="Total Amount Rs.").get_by_role("paragraph").text_content()
    assert(total_price == first_product_price)

    page.locator("textarea[name=\"message\"]").click()
    page.locator("textarea[name=\"message\"]").fill("Test description.")
    page.get_by_role("link", name="Place Order").click()
    handle_card_payment(page)

    page.locator("li").filter(has_text="Delete Account").click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
