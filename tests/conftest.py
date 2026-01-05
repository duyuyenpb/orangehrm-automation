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