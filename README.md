# QA Challenge -  API Test Pipeline

## How to Run Tests

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests:
    ```bash
    python -m unittest discover tests/
    ```

3. Generate Allure report:
    ```bash
    pytest --alluredir=./allure-results
    allure serve ./allure-results
    ```

## Pipeline Structure

- **tests/**: Contains all the test cases for API endpoints.
- **Dockerfile**: Defines the Docker image for running tests.
- **allure-results/**: Directory for storing Allure reports.
- **requirements.txt**: Lists Python dependencies.

## Advantages

- **Comprehensive Coverage**: All API endpoints are tested.
- **Detailed Failure Reports**: Logs and reports help in pinpointing issues.
- **Visualization**: Allure provides clear, actionable reports.

## Disadvantages

- **Overhead**: Maintaining detailed reports and logs can slow down the pipeline.
- **Docker Dependency**: Running tests in Docker adds complexity, especially in CI environments.
