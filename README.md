# AutomationExercise Test Automation Suite

An automated testing suite for the [Automationexercise](https://www.automationexercise.com) e-commerce demo site using Python, Pytest and Playwright.

## About This Project

This project demonstrates end-to-end test automation for a web application, covering user registration, user authentication, product browsing, shopping cart functionality, checkout flows and handling checkout pop-ups.

## Technologies Used

- **Python 3.12**
- **pytest** Testing Framework
- **playwright** Browser Automation

## Testing Coverage

- User Login (successful and failed attempts)
- User Registration
- Product Listing and Display
- Product Searching and Sorting (product name and cetagory)
- Cart Functionality (add and remove item)
- Complete Checkout Flow

## Project Structure
```
automation-exercise/
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
└── README.md
```
## Setup Instructions

### Prerequisites 

1. Clone this repository
2. Create a virtual environment:
```bash
   python -m venv venv
```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies
```bash
   pip install -r requirements.txt
   playwright install
```
5. Create a `.env` file in the root directory with your test credentials:
```
EMAIL=your_test_email@gmail.com
PASSWORD=your_test_password
```

### Running Tests

Run all tests:
```bash
pytest tests -v
```

Run with visible browser:
```bash
pytest tests -v --headed
```

Run a specific test:
```bash
pytest tests/test_cart.py::test_cart_page_loads -v
```
## Design Patterns

- **Page Object Model (POM)** - Each page is represented by a class in the `pages/` directory, separating test logic from page interactions
- **Fixtures** - Shared setup managed via `conftest.py` to avoid code repetition