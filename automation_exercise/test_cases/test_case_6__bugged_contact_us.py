# -*- coding: utf-8 -*-


from playwright.sync_api import Page, expect


def test_contact_us_form(page: Page) -> None:
    page.goto("https://www.automationexercise.com/")
    page.get_by_label("Consent", exact=True).click()
    page.locator("li").filter(has_text="Contact us").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Ved")
    page.get_by_placeholder("Email", exact=True).click()
    page.get_by_placeholder("Email", exact=True).fill("ved@example.com")
    page.get_by_placeholder("Subject").click()
    page.get_by_placeholder("Subject").fill("Test subject")
    page.get_by_placeholder("Your Message Here").click()
    page.get_by_placeholder("Your Message Here").fill("Test message")
    with page.expect_file_chooser() as fc_info:
        page.locator("input[name=\"upload_file\"]").click()
        file_chooser = fc_info.value
        file_chooser.set_files("test_file_for_contact_us.txt")
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Submit").click()
    expect(page.locator("#contact-page").get_by_text("Success! Your details have")).to_be_visible()
    page.get_by_role("link", name=" Home").click()
