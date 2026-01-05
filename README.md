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
