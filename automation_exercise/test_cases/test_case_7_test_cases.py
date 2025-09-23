# -*- coding: utf-8 -*-


import re

from playwright.sync_api import Page, expect

from ..actions import goto_page


def test_visit_test_cases_page(page: Page) -> None:
    goto_page(page)
    page.locator("li").filter(has_text="Test Cases").click()
    expect(page).to_have_url(re.compile("automationexercise.com/test_cases"))
