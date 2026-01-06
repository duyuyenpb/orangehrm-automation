from pages.login_page import LoginPage

def test_login_successfully(driver):
    login_page = LoginPage(driver)
    login_page.do_login("Admin", "admin123")
    login_page.is_login_successful()
    # Assert title hoặc URL để verify
    assert "dashboard" in driver.current_url