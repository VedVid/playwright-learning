# -*- coding: utf-8 -*-


from .. import credentials as c
from ..fill_new_user_form import fill_and_confirm as fill_form
from ..delete_user import delete_user

from playwright.sync_api import Page, expect


def setup_function():
    delete_user()


def test_place_order_and_register(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    expect(page.locator("body")).to_be_visible()

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

    fill_form(page)

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

    expect(page.get_by_role("link", name="Blue Top")).to_be_visible()
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
    page.locator("input[name=\"name_on_card\"]").click()
    page.locator("input[name=\"name_on_card\"]").fill(f"{c.FIRST_NAME} {c.LAST_NAME}")
    page.locator("input[name=\"card_number\"]").click()
    page.locator("input[name=\"card_number\"]").fill("1234567890")
    page.get_by_placeholder("ex.").click()
    page.get_by_placeholder("ex.").fill("111")
    page.get_by_placeholder("MM").click()
    page.get_by_placeholder("MM").fill("01")
    page.get_by_placeholder("YYYY").click()
    page.get_by_placeholder("YYYY").fill("2030")
    page.get_by_role("button", name="Pay and Confirm Order").click()
    expect(page.get_by_text("Order Placed!")).to_be_visible()
    expect(page.get_by_text("Order Placed!")).to_be_visible()

    page.locator("li").filter(has_text="Delete Account").click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
