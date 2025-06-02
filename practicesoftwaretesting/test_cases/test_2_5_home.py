# -*- coding: utf-8 -*-


import pytest

from playwright.sync_api import Page, Playwright, expect


# I wanted to use a class-based approach, but I could not
# find a way to pass Page and Playwright to the class itself.
# - classes with `__init__` method are not collected by pytest
# - classmethods are not initializing Page and Playwright
# - Page and Playwright as a class attributed simply did not work
# Also, all docs I was able to found about using Playwright with
# Pytest were using functions-only approaches, so perhaps it is
# a way to go.
# But since I tried to mimic the TypeScript video, I kept
# tinkering with various approaches.
# Tried to use closures – but pytest will not execute closures
# that are not called, in contrast to top-level functions.
# Tried to use setup_function and the separate functions for
# everything else, but it ended with page: Page being repeated
# over and over.
# Finally, I settled with the implementation you can see below.
# I do not love it, it is unnecessarily verbose, and it repeats
# `page: Page` over and over, but it works and I think it mimics
# the approach presented in the video close enough.


class TestHomePage():
    @pytest.fixture(autouse=True)
    def before(self, page: Page, playwright: Playwright) -> None:
        playwright.selectors.set_test_id_attribute("data-test")
        page.goto("https://practicesoftwaretesting.com/")

    @staticmethod
    def test_sign_in_link(page: Page) -> None:
        expect(
            page.get_by_test_id("nav-sign-in")
        ).to_have_text("Sign in")

    @staticmethod
    def test_page_title(page: Page) -> None:
        expect(page).to_have_title(
            "Practice Software Testing - Toolshop - v5.0"
        )

    @staticmethod
    def test_items_count(page: Page) -> None:
        productGrid = page.locator(".col-md-9")
        expect(productGrid.get_by_role("link")).to_have_count(9)

    @staticmethod
    def test_thor_hammer_visible(page: Page) -> None:
        expect(page.get_by_alt_text("Thor Hammer")).to_be_visible()
