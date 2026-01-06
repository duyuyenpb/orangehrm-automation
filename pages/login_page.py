from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    # Locators
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")

    @allure.step("Enter username: {0} and password: {1}")
    # Actions
    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BTN)
    
    @allure.step("Check if login is successful")
    def is_login_successful(self):
        # Kiểm tra xem URL có chứa chữ dashboard không
        return "dashboard" in self.driver.current_url