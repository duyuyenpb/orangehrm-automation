# 🍊 OrangeHRM Automation Framework

![Build Status](https://img.shields.io/github/actions/workflow/status/<your-username>/orangehrm-automation/main.yml?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green?style=flat-square&logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-7.0+-yellow?style=flat-square&logo=pytest)

## 📖 Introduction

This project is a **scalable and maintainable** test automation framework designed for the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) platform. 

It focus on architecture, stability, and visibility. The framework is built using **Python and Selenium**, following the **Page Object Model (POM)** design pattern to ensure strict separation between test logic and UI elements.

### 🎯 Key Features (Why this project stands out)

* **🏗 Page Object Model (POM):** Ensures code reusability and easy maintenance.
* **🛡️ Flakiness Handling:** Implemented `Explicit Waits` (smart waits) via a robust `BasePage` wrapper. No hard-coded `time.sleep()`.
* **📊 Advanced Reporting:** Integrated **Allure Report** with automatic **Screenshot on Failure**.
* **💾 Data-Driven Testing:** Test data is decoupled from code using JSON/Config files.
* **🚀 CI/CD Integration:** Automated regression runs via **GitHub Actions** on every push/pull request.
* **⚡ Parallel Execution:** Configured to support parallel test execution using `pytest-xdist`.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Core Library:** Selenium WebDriver
* **Test Runner:** Pytest
* **Reporting:** Allure / Pytest-HTML
* **CI/CD:** GitHub Actions
* **Utilities:** `webdriver-manager`, `python-dotenv`

---

## 📂 Project Structure

```text
orangehrm-automation/
├── .github/workflows/   # CI/CD Pipeline configurations
├── configurations/      # Global configs (URL, Browser, Timeouts)
├── pages/               # Page Object Classes (Locators & Actions)
│   ├── base_page.py     # Wrapper for Selenium Driver
│   ├── login_page.py
│   └── pim_page.py
├── tests/               # Test Scenarios (No direct Selenium calls here)
│   ├── conftest.py      # Fixtures (Setup/Teardown/Hooks)
│   └── test_login.py
├── test_data/           # External data (JSON/CSV)
├── utilities/           # Helper functions (ConfigReader, Logger)
├── reports/             # Test execution reports
└── requirements.txt     # Project dependencies
````

## Prerequisites

### Install Google Chrome

1. Update software packages  
   ```bash
   sudo apt-get update
   ```

2. Download the Chrome installation file (latest stable version)  
   ```bash
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   ```

3. Install Chrome (This command may report missing library errors -> Don't worry)  
   ```bash
   sudo dpkg -i google-chrome-stable_current_amd64.deb
   ```

4. Fix missing library errors and complete installation (Important!)  
   ```bash
   sudo apt-get install -f -y
   ```

5. Check if installation was successful  
   ```bash
   google-chrome --version
   ```

## 🏃‍♂️ How to Run the Project

1. **Install Dependencies**  
   Run the following command to install the required packages:  
   ```bash
   pip install -r requirements.txt
   ```  

2. **Verify Configuration**  
   Check the `configurations/config.ini` file for the base URL and credentials. Ensure they match your test environment.

3. **Run the Tests**  
   Use the following command to run all tests:  
   ```bash
   pytest
   ```  
   For specific tests, use:  
   ```bash
   pytest tests/test_login.py
   ```  

4. **Generate Reports**  
   To generate HTML reports, run:  
   ```bash
   pytest --html=reports/report.html
   ```  
   For Allure reports, use:  
   ```bash
   pytest --alluredir=reports/allure-results
   allure serve reports/allure-results
   ```  

5. **Additional Notes**  
   - Ensure Chrome is installed for Selenium tests.
   - Use headless mode for CI/CD environments.
   - For parallel execution, install `pytest-xdist` and run:  
   ```bash
   pytest -n 2
   ```
