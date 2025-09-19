# 🎭 Python Playwright + HTTPX Demo

A clean, modular framework for end-to-end web automation using [Playwright](https://playwright.dev/python/) and [HTTPX](https://www.python-httpx.org/)  in Python. This repository showcases scalable test architecture, explicit configuration, and CI/CD-friendly design principles.

## 🚀 Project Goals

- Demonstrate Playwright usage for UI automation in Python
- Demonstrate HTTPX usage for API automation in Python
- Apply strict architectural discipline with isolated config
- Enable reproducible, scalable test workflows
- Integrate seamlessly with CI/CD pipelines and reporting tools

## 🧱 Tech Stack

- **Python 3.13**
- **Playwright**
- **httpx**
- **pytest**
- **Allure**
- **Faker**
- **pydantic**
- **jsonschema**
- **pydantic-settings**
- **email-validator**
- **Docker (optional)**

## ⚙️ Quick Start
bash
### Install dependencies
pip install -r requirements.txt

### Install Playwright browsers
playwright install

# Run tests
pytest -m "regression" --headed --alluredir=./allure-results


