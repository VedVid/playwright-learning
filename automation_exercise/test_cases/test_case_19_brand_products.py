# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from ..actions import goto_page


def test_example(page: Page) -> None:
    goto_page(page)

    page.locator("li").filter(has_text="Products").click()
    expect(page.get_by_role("heading", name="Brands")).to_be_visible()
    page.locator("a").filter(has_text="Madame").click()
    expect(page.get_by_role("heading", name="Brand - Madame Products")).to_be_visible()
    expect(page.get_by_text("View Product").first).to_be_visible()
    page.locator("a").filter(has_text="Kookie Kids").click()
    expect(page.get_by_role("heading", name="Brand - Kookie Kids Products")).to_be_visible()
    expect(page.get_by_text("View Product").first).to_be_visible()
