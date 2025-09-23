# -*- coding: utf-8 -*-


from . import credentials as c

from playwright.sync_api import Page, expect


def goto_page(page: Page, url: str=None) -> None:
    '''
    This function visits an url and ensures that the webpage body is visible.
    If it's necessary, it also confirms consent popup.

    Parameters
    ----------
    page : Page
        Playwright's Page
    url : str
        url Playwright is about to visit. If url is not present, it
        defaults to automationexercise.com home page.

    Returns
    -------
    Nothing
    '''
    if url is None:
        url = "https://www.automationexercise.com/"
    page.goto(url)
    try:
        page.get_by_label("Consent", exact=True).click()
    except:
        print("No consent popup displayed. Passing...")
    expect(page.locator("body")).to_be_visible()


def new_user_form_fill_and_confirm(page: Page) -> bool:
    '''
    This function fills a form to create a new user, using credentials
    specified in separate file `credentials.py`.

    Parameters
    ----------
    page : Page
        Playwright's Page

    Returns
    -------
    bool
        Returns True if no exceptions were encountered; otherwise, returns False.
    '''
    try:
        expect(page.get_by_text("Enter Account Information")).to_be_visible()
        page.get_by_label(c.TITLE).check()
        expect(page.get_by_label("Name *", exact=True)).to_have_value(c.USER_NAME)
        expect(page.get_by_label("Email *", exact=True)).to_have_value(c.EMAIL_ADDRESS)
        page.get_by_label("Password *").click()
        page.get_by_label("Password *").fill(c.PASSWORD)
        page.locator("#days").select_option(c.BIRTHDAY_DAY)
        page.locator("#months").select_option(c.BIRTHDAY_MONTH)
        page.locator("#years").select_option(c.BIRTHDAY_YEAR)
        page.get_by_label("Sign up for our newsletter!").check()
        page.get_by_label("Receive special offers from").check()
        page.get_by_label("First name *").click()
        page.get_by_label("First name *").fill(c.FIRST_NAME)
        page.get_by_label("Last name *").click()
        page.get_by_label("Last name *").fill(c.LAST_NAME)
        page.get_by_label("Company", exact=True).click()
        page.get_by_label("Company", exact=True).fill(c.COMPANY)
        page.get_by_label("Address *").click()
        page.get_by_label("Address *").fill(c.ADDRESS)
        page.get_by_label("Address 2").click()
        page.get_by_label("Address 2").fill(c.ADDRESS_2)
        page.get_by_label("Country *").select_option(c.COUNTRY)
        page.get_by_label("State *").click()
        page.get_by_label("State *").fill(c.STATE)
        page.get_by_label("City *").click()
        page.get_by_label("City *").fill(c.CITY)
        page.locator("#zipcode").click()
        page.locator("#zipcode").fill(c.ZIPCODE)
        page.get_by_label("Mobile Number *").click()
        page.get_by_label("Mobile Number *").fill(c.MOBILE)
        page.get_by_role("button", name="Create Account").click()
    except Exception as e:
        print(f"Unexpected {e=}, {type(e)=}")
        return False
    else:
        return True


def handle_card_payment(page: Page) -> None:
    '''
    This function fills a form to required to proceed with payment, using
    credit card data specified in separate file `credentials.py`.

    Parameters
    ----------
    page : Page
        Playwright's Page

    Returns
    -------
    Nothing
    '''
    page.locator("input[name=\"name_on_card\"]").click()
    page.locator("input[name=\"name_on_card\"]").fill(f"{c.FIRST_NAME} {c.LAST_NAME}")
    page.locator("input[name=\"card_number\"]").click()
    page.locator("input[name=\"card_number\"]").fill(f"{c.CARD_NO}")
    page.get_by_placeholder("ex.").click()
    page.get_by_placeholder("ex.").fill(f"{c.CARD_EX}")
    page.get_by_placeholder("MM").click()
    page.get_by_placeholder("MM").fill(f"{c.CARD_MM}")
    page.get_by_placeholder("YYYY").click()
    page.get_by_placeholder("YYYY").fill(f"{c.CARD_YYYY}")
    page.get_by_role("button", name="Pay and Confirm Order").click()
    expect(page.get_by_text("Order Placed!")).to_be_visible()
    page.get_by_role("link", name="Continue").click()
