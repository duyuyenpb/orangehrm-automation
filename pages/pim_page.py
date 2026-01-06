from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
import allure

class PIMPage(BasePage):
    # --- LOCATORS (Địa chỉ nhà) ---
    # Menu bên trái
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    
    # Nút Add
    ADD_BTN = (By.XPATH, "//button[normalize-space()='Add']")
    
    # Form điền thông tin
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")
    
    # Thông báo thành công (Toast Message) - Đây là phần "ăn tiền"
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class, 'oxd-toast-content')]")

    # --- ACTIONS (Hành động) ---
    @allure.step("Click on PIM menu")
    def click_menu_pim(self):
        self.do_click(self.MENU_PIM)

    @allure.step("Enter username: {0} and password: {1}")
    def add_new_employee(self, firstname, lastname):
        # 1. Click nút Add
        self.do_click(self.ADD_BTN)
        
        # 2. Điền tên
        self.do_send_keys(self.FIRST_NAME, firstname)
        self.do_send_keys(self.LAST_NAME, lastname)
        
        # 3. Click Save
        self.do_click(self.SAVE_BTN)

    @allure.step("Get success message")
    def get_success_message(self):
        # Lấy text của cái bảng thông báo màu xanh hiện lên góc màn hình
        return self.get_element_text(self.SUCCESS_TOAST)