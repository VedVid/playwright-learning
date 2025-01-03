# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect


def test_verify_all_products(page: Page) -> None:
    page.goto("https://automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    expect(page.locator("body")).to_be_visible()
    page.locator("li").filter(has_text="Products").click()
    expect(page.get_by_role("heading", name="All Products")).to_be_visible()
    expect(page.locator("body > section:nth-child(3) > div.container > div > div.col-sm-9.padding-right > div")).to_be_visible()
    page.locator(".choose > .nav > li > a").first.click()
    expect(page.locator("div").filter(has_text="Products Cart Signup").first).to_be_visible()

    # That's how it was generated by codegen:
    # expect(page.get_by_role("heading", name="Blue Top")).to_be_visible()
    # but it seems quite flaky for me.
    # Decided to use css selector instead
    expect(page.locator(".product-information > h2:nth-child(2)")).to_be_visible()

    # The idea there is to check if "Category" element is visible,
    # and to check if it does has some category actually displayed,
    # without asserting specific text visible.
    category = page.get_by_text("Category:")
    expect(category).to_be_visible()
    assert(len(category.text_content()) > len("Category: "))

    price = page.get_by_text("Rs.")
    expect(price).to_be_visible()
    assert(price.text_content()[-1].isnumeric())

    availability = condition = page.locator(".product-information > p:nth-child(6)")
    expect(availability).to_contain_text("Availability")
    expect(availability).to_be_visible()
    expect(availability).to_contain_text("tock")

    condition = page.locator(".product-information > p:nth-child(7)")
    expect(condition).to_contain_text("Condition")
    expect(condition).to_be_visible()
    assert(len(condition.text_content()) > len("Condition: "))
