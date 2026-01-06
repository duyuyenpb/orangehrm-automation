import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # 1. Thiết lập Options cho Chrome
    options = Options()
    
    # --- CẤU HÌNH QUAN TRỌNG CHO GITHUB CODESPACES / CI/CD ---
    options.add_argument("--headless")  # Chạy không giao diện
    options.add_argument("--no-sandbox") # Bắt buộc trên Linux/Docker
    options.add_argument("--disable-dev-shm-usage") # Tránh lỗi thiếu bộ nhớ trên container
    options.add_argument("--window-size=1920,1080") # Set size ảo để không bị lỗi UI responsive
    # ---------------------------------------------------------

    # 2. Khởi tạo Driver
    # Webdriver Manager sẽ tự tải chromedriver phù hợp với bản Chrome vừa cài ở Bước 1
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # driver.maximize_window() -> Không cần thiết trong headless, đã set window-size ở trên
    
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    yield driver
    
    driver.quit()

# --- PHẦN MỚI: HOOK CHỤP ẢNH ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Chỉ xử lý nếu test case kết thúc (call) và bị Fail
    if rep.when == "call" and rep.failed:
        # Lấy driver từ fixture
        driver = item.funcargs.get('driver', None)
        
        if driver:
            print(f"\n📸 Taking screenshot for failed test: {item.name}")
            # Chụp ảnh và attach vào Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot_on_Failure",
                attachment_type=allure.attachment_type.PNG
            )