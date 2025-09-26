# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from .. import credentials as c
from ..actions import goto_page


def test_example(page: Page) -> None:
    goto_page(page)

    page.locator("li").filter(has_text="Products").click()
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()

    page.locator(".choose > .nav > li > a").first.click()
    page.get_by_placeholder("Your Name").click()
    page.get_by_placeholder("Your Name").fill(c.FIRST_NAME)
    page.get_by_placeholder("Email Address", exact=True).click()
    page.get_by_placeholder("Email Address", exact=True).fill(c.EMAIL_ADDRESS)
    page.get_by_placeholder("Add Review Here!").click()
    page.get_by_placeholder("Add Review Here!").fill("Awesome product (test review)")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Thank you for your review.")).to_be_visible()
