from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class DashboardPage(BasePage):
    # --- LOCATORS ---
    # "Dashboard" title on the header bar (used to verify successful login)
    PAGE_HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    
    # Left menu to navigate to other pages
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    MENU_ADMIN = (By.XPATH, "//span[text()='Admin']")

    # --- ACTIONS ---
    @allure.step("Get dashboard page title")
    def get_dashboard_title(self):
        """Get the page title text. Expected return: 'Dashboard'"""
        return self.get_element_text(self.PAGE_HEADER)

    @allure.step("Navigate to PIM module")
    def navigate_to_pim_module(self):
        """Click PIM menu to go to Employee page"""
        self.do_click(self.MENU_PIM)
        # Note: Page navigation logic is here. 
        # After this function runs, in the Test file we will initialize PIMPage.