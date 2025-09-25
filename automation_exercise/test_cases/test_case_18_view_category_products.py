# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from ..actions import goto_page


def test_example(page: Page) -> None:
    goto_page(page)

    expect(page.get_by_role("heading", name="Category")).to_be_visible()
    page.get_by_role("link").filter(has_text="Women").click()
    page.get_by_role("link", name="Dress").click()
    expect(page.get_by_role("heading", name="Women - Dress Products")).to_be_visible()
    page.get_by_role("link").filter(has_text="Men").nth(1).click()
    expect(page.locator("#Men div")).to_be_visible()
