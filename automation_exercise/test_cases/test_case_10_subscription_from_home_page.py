# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect


def test_subscription_from_home_page(page: Page) -> None:
    page.goto("https://automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    expect(page.locator("body")).to_be_visible()
    expect(page.get_by_role("heading", name="Subscription")).to_be_visible()
    page.get_by_placeholder("Your email address").click()
    page.get_by_placeholder("Your email address").fill("ved@example.com")
    page.get_by_role("button", name="").click()
    page.get_by_placeholder("Your email address").click()
    page.get_by_placeholder("Your email address").fill("ved@example.com")
    page.locator('#subscribe').click()
    expect(page.get_by_text("You have been successfully subscribed!")).to_be_visible()
