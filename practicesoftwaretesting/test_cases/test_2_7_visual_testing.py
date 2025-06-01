# -*- coding: utf-8 -*-


import pytest


from playwright.sync_api import Page, Playwright


def test_capture_screenshot(page: Page, playwright: Playwright, customer_01_auth) -> None:
    print("It seems that Python Playwright does not have `to_have_screenshot page` assertion available, so we will just save a screenshot and we'll move on.")
    page.goto("https://practicesoftwaretesting.com/")
    page.screenshot(path="test_screenshot.png", full_page=True)
