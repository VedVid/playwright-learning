# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from .. import credentials as c
from ..actions import goto_page, handle_card_payment, new_user_form_fill_and_confirm


def test_place_order_register_before_checkout(page: Page) -> None:
    goto_page(page)

    page.locator("li").filter(has_text="Signup / Login").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(c.USER_NAME)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_role("button", name="Signup").click()

    new_user_form_fill_and_confirm(page)
    expect(page.get_by_text("Account Created!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    page.locator(".productinfo > .btn").first.click()
    page.get_by_role("link", name="View Cart").click()

    expect(page.get_by_text("Shopping Cart")).to_be_visible()
    page.get_by_text("Proceed To Checkout").click()

    expect(page.get_by_text("Rs.").nth(1)).to_be_visible()
    first_product_css = ".cart_price > p:nth-child(1)"
    first_product_price = page.locator(first_product_css).text_content()
    assert(first_product_price == page.get_by_text("Rs.").first.text_content())
    total_price_css = ".table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(4) > p:nth-child(1)"
    total_price = page.locator(total_price_css).text_content()
    assert (first_product_price == total_price)
    expect(page.get_by_role("heading", name="Your delivery address")).to_be_visible()
    page.locator("textarea[name=\"message\"]").click()
    page.locator("textarea[name=\"message\"]").fill("test")
    page.get_by_role("link", name="Place Order").click()

    handle_card_payment(page)

    page.locator("li").filter(has_text="Delete Account").click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
