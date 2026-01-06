from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class DashboardPage(BasePage):
    # --- LOCATORS ---
    # Tiêu đề "Dashboard" nằm trên thanh header (dùng để verify login thành công)
    PAGE_HEADER = (By.XPATH, "//h6[normalize-space()='Dashboard']")
    
    # Menu bên trái để điều hướng sang các trang khác
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    MENU_ADMIN = (By.XPATH, "//span[text()='Admin']")

    # --- ACTIONS ---
    @allure.step("Get dashboard page title")
    def get_dashboard_title(self):
        """Lấy text tiêu đề trang. Mong đợi trả về: 'Dashboard'"""
        return self.get_element_text(self.PAGE_HEADER)

    @allure.step("Navigate to PIM module")
    def navigate_to_pim_module(self):
        """Click menu PIM để chuyển sang trang Nhân viên"""
        self.do_click(self.MENU_PIM)
        # Lưu ý: Logic chuyển trang nằm ở đây. 
        # Sau khi hàm này chạy xong, ở file Test chúng ta sẽ khởi tạo PIMPage.