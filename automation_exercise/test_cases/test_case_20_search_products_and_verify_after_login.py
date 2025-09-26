# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect

from .. import credentials as c
from ..actions import goto_page
from ..user_management import create_user, delete_user


def setup_function():
    delete_user()
    create_user()


def test_search_products_veryfiry_after_login(page: Page) -> None:
    goto_page(page)

    page.locator("li").filter(has_text="Products").click()

    first_featured_product_css_locator = ".features_items > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)"
    first_product_name = page.locator(first_featured_product_css_locator).text_content()
    expect(page.get_by_text(first_product_name).first).to_be_visible()

    page.get_by_placeholder("Search Product").click()
    page.get_by_placeholder("Search Product").fill(first_product_name)
    search_button_css_locator = "html body section#advertisement div.container button#submit_search.btn.btn-default.btn-lg"
    page.locator(search_button_css_locator).click()
    expect(page.get_by_role("heading", name="Searched Products")).to_be_visible()
    expect(page.get_by_text(first_product_name).first).to_be_visible()
    page.get_by_text("Add to cart").first.click()
    page.get_by_role("button", name="Continue Shopping").click()

    page.locator("li").filter(has_text="Signup / Login").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill(c.EMAIL_ADDRESS)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(c.PASSWORD)
    page.get_by_role("button", name="Login").click()

    page.locator("li").filter(has_text="Cart").click()
    expect(page.get_by_text("Shopping Cart")).to_be_visible()
    expect(page.get_by_text(first_product_name).first).to_be_visible()
