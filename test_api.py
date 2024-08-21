import requests
import unittest
import logging

# Set up logging for troubleshooting
logging.basicConfig(level=logging.INFO)


class TestAPI(unittest.TestCase):
    BASE_URL = "http://yourapiurl.com"  # Change to actual API URL

    def test_add_model_valid(self):
        response = requests.post(f"{self.BASE_URL}/models", json={"name": "Test Model"})
        self.assertEqual(response.status_code, 201)

    def test_add_model_invalid(self):
        response = requests.post(f"{self.BASE_URL}/models", json={"name": "", "owner": ""})
        self.assertEqual(response.status_code, 400)
        logging.info(f"Missing validation response: {response.json()}")

    def test_delete_model(self):
        model_id = "12345"  # Replace with a valid model ID
        response = requests.delete(f"{self.BASE_URL}/models/{model_id}")
        self.assertEqual(response.status_code, 204)


# Additional tests can be added for append and inference...

if __name__ == "__main__":
    unittest.main()
