# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from ..actions import goto_page


def test_remove_item_from_cart(page: Page) -> None:
    goto_page(page)

    page.locator(".productinfo > .btn").first.click()
    page.get_by_role("link", name="View Cart").click()

    expect(page.get_by_text("Shopping Cart")).to_be_visible()
    page.locator(".cart_quantity_delete").first.click()
    expect(page.get_by_text("Cart is empty!")).to_be_visible()
