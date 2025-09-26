# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from ..actions import goto_page


def test_verify_scroll_without_arrow_button(page: Page) -> None:
    goto_page(page)

    page.get_by_role("heading", name="Subscription").scroll_into_view_if_needed()
    expect(page.get_by_role("heading", name="Subscription")).to_be_visible()
    page.get_by_role("heading", name="Full-Fledged practice website").scroll_into_view_if_needed()
    expect(page.get_by_role("heading", name="Full-Fledged practice website")).to_be_visible()
