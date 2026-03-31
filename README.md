# AutomationExercise - UI Test Automation Suite

Self-built end-to-end UI automation suite for the [AutomationExercise](https://www.automationexercise.com) e-commerce demo site using **Python, pytest, and Playwright**.

Built as part of my self-training for **Junior QA Automation Engineer** roles while transitioning from running a small business.

## About This Project

This suite covers realistic e-commerce user journeys across the full shopping flow:
- **Authentication**: User registration and login (success and failure paths)
- **Products**: Browsing, searching, and sorting by name and category
- **Cart**: Adding and removing items
- **Checkout**: Complete checkout flow including pop-up handling

## Technologies Used

- **Python 3.12**
- **pytest** (test framework + fixtures)
- **Playwright** (browser automation)

## Key Features & Design Patterns

- **Page Object Model (POM)** with dedicated page classes for clean separation of test logic and page interactions
- Shared **pytest fixtures** via `conftest.py` to reduce duplication
- Supports both **headed and headless** test runs
- `.env` file for secure credential management
- Automated CI pipeline that runs the full suite on every push

## Project Structure
```
automation-exercise/
├── .github/workflows/      # GitHub Actions CI
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .env
```

## Setup & Running Tests

1. Clone the repository
2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```
4. Create a `.env` file in the root directory:
```
EMAIL=your_test_email@gmail.com
PASSWORD=your_test_password
```
5. Run tests:
```bash
# All tests
pytest tests -v

# With visible browser
pytest tests -v --headed

# Specific file
pytest tests/test_cart.py -v
```

## CI/CD

GitHub Actions workflow automatically runs the full test suite in headless mode on every push.

## Why This Matters for QA Roles

This project demonstrates the ability to structure scalable UI automation using modern best practices — particularly Page Object Model for maintainability across a multi-page e-commerce application.