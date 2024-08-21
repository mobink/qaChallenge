import requests
import unittest


class TestRecruitingAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:8000"  # Change based on how you run the API

    def test_add_model_valid(self):
        """Test adding a model with valid data."""
        response = requests.post(f"{self.BASE_URL}/models", json={"name": "My Model1", "owner": "john1"})
        self.assertEqual(response.status_code, 200)

    def test_add_model_invalid(self):
        """Test adding a model with missing mandatory field."""
        response = requests.post(f'{self.BASE_URL}/models', json={"name1": "", "owner1": ""})
        self.assertEqual(response.status_code, 422)


    def test_delete_model(self):
        """Test deleting a model by ID."""
        model_id = "dfbf7ae0-4329-499e-a11b-97cbba967734"  # Replace with actual model ID for testing
        response = requests.delete(f"{self.BASE_URL}/models/{model_id}")
        self.assertEqual(response.status_code, 404)

    def test_inference(self):
        """Test inference on a model."""
        model_id = "dfbf7ae0-4329-499e-a11b-97cbba967734"  # Replace with actual model ID
        response = requests.post(f"{self.BASE_URL}/models/{model_id}/inference", json={"data": "sample input"})
        self.assertEqual(response.status_code, 200)
