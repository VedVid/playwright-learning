# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect


USER_NAME = "Ved"
PASSWORD = "111"


def test_register_user(page: Page):
    page.goto("http://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

    page.get_by_label("Consent", exact=True).click()

    page.get_by_role("link").filter(has_text="Signup").click()
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()

    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill(USER_NAME)
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").click()
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill("ved@example.com")
    page.get_by_role("button").filter(has_text="Signup").click()

    expect(page.get_by_text("Enter Account Information")).to_be_visible()
    page.get_by_label("Mr.").check()
    expect(page.get_by_label("Name *", exact=True)).to_have_value(USER_NAME)
    expect(page.get_by_label("Email *", exact=True)).to_have_value("ved@example.com")
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill(PASSWORD)
    page.locator("#days").select_option("1")
    page.locator("#months").select_option("1")
    page.locator("#years").select_option("2021")
    page.get_by_label("Sign up for our newsletter!").check()
    page.get_by_label("Receive special offers from").check()
    page.get_by_label("First name *").click()
    page.get_by_label("First name *").fill("Ved")
    page.get_by_label("Last name *").click()
    page.get_by_label("Last name *").fill("Vid")
    page.get_by_label("Company", exact=True).click()
    page.get_by_label("Company", exact=True).fill("N/A")
    page.get_by_label("Address *").click()
    page.get_by_label("Address *").fill("Main Street")
    page.get_by_label("Address 2").click()
    page.get_by_label("Address 2").fill("123B")
    page.get_by_label("Country *").select_option("United States")
    page.get_by_label("State *").click()
    page.get_by_label("State *").fill("NY")
    page.get_by_label("City *").click()
    page.get_by_label("City *").fill("New York")
    page.locator("#zipcode").click()
    page.locator("#zipcode").fill("111-11")
    page.get_by_label("Mobile Number *").click()
    page.get_by_label("Mobile Number *").fill("111-111-111")
    page.get_by_role("button", name="Create Account").click()

    expect(page.get_by_text("Account Created")).to_be_visible()
    page.get_by_role("link", name="Continue").click()

    expect(page.get_by_text(f"Logged in as {USER_NAME}")).to_be_visible()
    page.locator("li").filter(has_text="Delete Account").click()

    expect(page.get_by_text("Account Deleted")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
