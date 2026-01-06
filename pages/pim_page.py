from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import allure

class PIMPage(BasePage):
    # --- LOCATORS ---
    # Left menu
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    
    # Add button
    ADD_BTN = (By.XPATH, "//button[normalize-space()='Add']")
    
    # Information form
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")
    
    # Success message (Toast Message) - This is the key part
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class, 'oxd-toast-content')]")

    # --- ACTIONS ---
    @allure.step("Click on PIM menu")
    def click_menu_pim(self):
        self.do_click(self.MENU_PIM)

    @allure.step("Enter username: {0} and password: {1}")
    def add_new_employee(self, firstname, lastname):
        # 1. Click Add button
        self.do_click(self.ADD_BTN)
        
        # 2. Fill in name
        self.do_send_keys(self.FIRST_NAME, firstname)
        self.do_send_keys(self.LAST_NAME, lastname)
        
        # 3. Click Save
        self.do_click(self.SAVE_BTN)

    @allure.step("Get success message")
    def get_success_message(self):
        # Get the text of the green notification box that appears in the corner of the screen
        return self.get_element_text(self.SUCCESS_TOAST)