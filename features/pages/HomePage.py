from selenium.webdriver.common.by import By
import time

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage
from features.pages.RegisterPage import RegisterPage
from features.pages.SearchPage import SearchPage
I am the other user
I am not the other user

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)

    def select_login_option(self):
        self.click_on_element("login_option_link_text", self.login_option_link_text)
        return LoginPage(self.driver)

    def select_register_option(self):
        self.click_on_element("register_option_link_text", self.register_option_link_text)
        return RegisterPage(self.driver)

    def check_home_page_title(self, expected_title_text):
        return self.verify_page_title(expected_title_text)

    def enter_product_into_search_box_field(self, product_text):
        self.type_into_element("search_box_field_name", self.search_box_field_name, product_text)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        time.sleep(2)
        return SearchPage(self.driver)
    This is feature1
