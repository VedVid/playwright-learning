# -*- coding: utf-8 -*-


import re

from .. import actions as a

from playwright.sync_api import Page, expect


QUANTITY = "4"


def test_verify_product_quantity_in_cart(page: Page) -> None:
    a.goto_page(page)
    page.get_by_text("View Product", exact=False).first.click()
    expect(page).to_have_url(re.compile(r".automationexercise.com.product_details.[0-9]+"))
    page.locator("#quantity").click()
    page.locator("#quantity").fill(QUANTITY)
    page.get_by_role("button").filter(has_text="Add to cart").click()
    page.get_by_role("link", name="View Cart").click()
    expect(page.get_by_role("button", name=QUANTITY).first).to_be_visible()
