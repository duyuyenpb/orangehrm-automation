import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    # 1. Set up Options for Chrome
    options = Options()
    
    # --- IMPORTANT CONFIGURATION FOR GITHUB CODESPACES / CI/CD ---
    options.add_argument("--headless")  # Run without interface
    options.add_argument("--no-sandbox") # Mandatory on Linux/Docker
    options.add_argument("--disable-dev-shm-usage") # Avoid memory shortage errors on container
    options.add_argument("--window-size=1920,1080") # Set virtual size to avoid UI responsive errors
    # ---------------------------------------------------------

    # 2. Initialize Driver
    # Webdriver Manager will automatically download the appropriate chromedriver for the Chrome version installed in Step 1
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # driver.maximize_window() -> Not necessary in headless, window-size already set above
    
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    yield driver
    
    driver.quit()

# --- NEW PART: SCREENSHOT HOOK ---
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Only process if test case ends (call) and fails
    if rep.when == "call" and rep.failed:
        # Get driver from fixture
        driver = item.funcargs.get('driver', None)
        
        if driver:
            logging.info(f"\n📸 Taking screenshot for failed test: {item.name}")
            # Take screenshot and attach to Allure
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Screenshot_on_Failure",
                attachment_type=allure.attachment_type.PNG
            )