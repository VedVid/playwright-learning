# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from ..actions import goto_page


def test_add_recommended_product_to_cart(page: Page) -> None:
    goto_page(page)

    expect(page.get_by_role("heading", name="recommended items")).to_be_visible()
    add_to_cart_css = "div.active:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(4)"
    product_name_css = "div.left:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)"
    product_name = page.locator(product_name_css).text_content()
    page.locator(add_to_cart_css).first.click()
    page.get_by_role("link", name="View Cart").click()
    expect(page.get_by_text("Shopping Cart")).to_be_visible()
    expect(page.get_by_role("link", name=product_name)).to_be_visible()
