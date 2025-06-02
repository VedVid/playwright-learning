# -*- coding: utf-8 -*-


import pytest

from playwright.sync_api import expect, Page


class Test_API():
    @staticmethod
    def test_get_products(page: Page):
        api_url = "https://api.practicesoftwaretesting.com"
        response = page.request.get(api_url + "/products")
        expect(response).to_be_ok()
        data = response.json()
        import pprint
        pprint.pprint(data)
        assert(len(data["data"]) == 9)
        # I am not entirely sure why the line below doesn't work.
        # Error code suggests that the argument to "to_be"
        # must be either instance of Page, Locator, or APIResponse.
        # But why it can't just compare `int` as in TypeScript examples?
        # expect(len(data["data"])).to_be(9)
        # expect(len(data["data"])).to_have_value(9)
