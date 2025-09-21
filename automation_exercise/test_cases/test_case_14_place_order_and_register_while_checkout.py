# -*- coding: utf-8 -*-


from .. import credentials as c
from ..delete_user import delete_user

from playwright.sync_api import Page, expect


def setup_function():
    delete_user()


def test_example(page: Page) -> None:
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
