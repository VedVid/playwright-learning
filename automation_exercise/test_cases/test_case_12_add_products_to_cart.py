# -*- coding: utf-8 -*-


from .. import actions as a

import time
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    a.goto_page(page)

    page.locator("li").filter(has_text="Products").click()

    #
    # Hover over product info, wait for the overlay,
    # then click on the "Add to cart" button displayed on the overlay.
    # It seems that using time.sleep is actually necessary, because
    # clicking button immediately after page.wait_for_selector
    # was failing often. Perhaps due the animation?
    #

    # Setting up CSS selectors to not pollute the code later.
    first_product_content_css = "div.col-sm-4:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
    first_product_overlay_button_css = "div.col-sm-4:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(3) > i:nth-child(1)"
    first_product_price_css = "div.col-sm-4:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h2:nth-child(1)"
    first_product_name_css = ".features_items > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(2)"

    # Hovering over first element to trigger overlay animation.
    page.hover(first_product_content_css)
    page.wait_for_selector(first_product_overlay_button_css)
    time.sleep(1)

    # Overlay triggered, now we are:
    # - assigning product data to variables to use it later to compare data
    #   in `product` menu with `cart` content,
    # - interact with overlay.
    first_product_name = page.locator(first_product_name_css).text_content()
    first_product_price = page.locator(first_product_price_css).text_content()
    page.click(first_product_overlay_button_css)
    page.get_by_role("button", name="Continue Shopping").click()

    #
    # Second product is handled in the same way.
    #

    # Setting up CSS selectors to not pollute the code later.
    second_product_content_css = "div.col-sm-4:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
    second_product_overlay_button_css = "div.col-sm-4:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(3)"
    second_product_price_css = "div.col-sm-4:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h2:nth-child(1)"
    second_product_name_css = "div.col-sm-4:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(2)"

    # Hovering over second element to trigger overlay animation.
    page.hover(second_product_content_css)
    page.wait_for_selector(second_product_overlay_button_css)
    time.sleep(1)

    # Overlay triggered, now we are:
    # - assigning product data to variables to use it later to compare data
    #   in `product` menu with `cart` content,
    # - interact with overlay.
    second_product_name = page.locator(second_product_name_css).text_content()
    second_product_price = page.locator(second_product_price_css).text_content()
    page.click(second_product_overlay_button_css)
    page.get_by_role("link", name="View Cart").click()

    #
    # Testing cart and comparing cart data with products data
    #

    # This doesn't seem to need additional asserts if I use
    # product names for locators.
    expect(page.get_by_role("link", name=first_product_name)).to_be_visible()
    expect(page.get_by_role("link", name=second_product_name)).to_be_visible()

    expect(page.get_by_text("Rs.").first).to_be_visible()
    assert(first_product_price == page.get_by_text("Rs.").first.text_content())
    expect(page.get_by_text("Rs.").nth(2)).to_be_visible()
    assert(second_product_price == page.get_by_text("Rs.").nth(2).text_content())

    # This doesn't seem to need additional asserts if I use
    # products quantity for locators.
    expect(page.locator("#product-1").get_by_role("button", name="1")).to_be_visible()
    expect(page.locator("#product-2").get_by_role("button", name="1")).to_be_visible()
