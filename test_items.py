import time

import pytest
from selenium.webdriver.common.by import By


def test_add_button_is_visible(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        add_to_basket_btn = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        assert add_to_basket_btn.is_displayed(), "Cant find add_to_basket_btn in page"
