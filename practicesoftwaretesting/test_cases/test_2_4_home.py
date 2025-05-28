# -*- coding: utf-8 -*-


from playwright.sync_api import Page, Playwright, expect


def test_home_page(page: Page, playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-test")
    page.goto("https://practicesoftwaretesting.com/")

    # Ensure the sign-in link is present.
    expect(page.get_by_test_id("nav-sign-in")).to_have_text("Sign in")

    # Check the title of the page.
    expect(page).to_have_title("Practice Software Testing - Toolshop - v5.0")
    
    # Check the count of items displayed.
    productGrid = page.locator(".col-md-9")
    expect(productGrid.get_by_role("link")).to_have_count(9)

    # Search for Thor Hammer and check the result.
    expect(page.get_by_alt_text("Thor Hammer")).to_be_visible()
