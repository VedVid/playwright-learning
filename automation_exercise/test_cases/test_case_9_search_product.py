# -*- coding: utf-8 -*-


import re

from playwright.sync_api import Page, expect


def test_search_product(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    expect(page.locator("body")).to_be_visible()
    page.locator("li").filter(has_text="Products").click()
    expect(page).to_have_url(re.compile("automationexercise.com/products"))
    product_name = page.get_by_text("Blue Top").nth(1).text_content()
    page.get_by_placeholder("Search Product").click()
    page.get_by_placeholder("Search Product").fill(product_name)
    page.locator('//*[@id="submit_search"]').click()
    expect(page.get_by_text(product_name).first).to_be_visible()
