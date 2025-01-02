# -*- coding: utf-8 -*-


import re
from playwright.sync_api import Page, expect


def test_visit_test_cases_page(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    expect(page.locator("body")).to_be_visible()
    page.locator("li").filter(has_text="Test Cases").click()
    expect(page).to_have_url(re.compile("automationexercise.com/test_cases"))
