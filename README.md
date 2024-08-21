# QA Challenge -  API Test Pipeline

## How to Run Tests

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests:
    ```bash
    python -m unittest -m requests discover tests/
    ```

3. Generate Allure report:
    ```bash
    pytest --alluredir=./allure-results
    allure serve ./allure-results
    ```

## Pipeline Structure

- **tests/**: Contains all the test cases for API endpoints.
- **allure-results/**: Directory for storing Allure reports.
- **requirements.txt**: Lists Python dependencies.

## Advantages

- **Comprehensive Coverage**: All API endpoints are tested.
- **Visualization**: Allure provides clear, actionable reports.

## Disadvantages

- **Overhead**: Maintaining detailed reports and logs can slow down the test execution.
