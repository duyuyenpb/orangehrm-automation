import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage  # <--- Import mới
from pages.pim_page import PIMPage
from utilities.config_reader import get_config

USERNAME = get_config('common', 'username')
PASSWORD = get_config('common', 'password')

class TestAddEmployee:
    
    def test_add_employee_successfully(self, driver):
        # 1. Login
        login_page = LoginPage(driver)
        login_page.do_login(USERNAME, PASSWORD)
        
        # 2. Verify entered Dashboard & Navigate to PIM
        dashboard_page = DashboardPage(driver)
        assert dashboard_page.get_dashboard_title() == "Dashboard" # Ensure login is successful
        
        dashboard_page.navigate_to_pim_module() # Navigate to page
        
        # 3. Operate on PIM page
        pim_page = PIMPage(driver)
        pim_page.add_new_employee("Test", "User 01")
        
        # 4. Verify
        assert "Success" in pim_page.get_success_message()