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

    def test_get_model(self):
        """Test to get model information using a GET request."""
        response = requests.get(f"{self.BASE_URL}/models")
        self.assertEqual(response.status_code, 200)

    def test_add_model_version(self):
        """Test to add version to model."""
        model_id = '611cd27f-7d65-4433-8a9b-4e78b12d6b37'  # Replace with actual model ID for testing
        response = requests.post(f"{self.BASE_URL}/models/{model_id}/versions", json={'name': "mk51",'hugging_face_model': "mk51"})
        self.assertEqual(response.status_code, 200)

    def test_get_model_version(self):
        """Test to get model version information using a GET request."""
        model_id = 'e8247593-9b56-4199-9c6f-87346ecdc252'  # Replace with actual model ID for testing
        response = requests.get(f"{self.BASE_URL}/models/{model_id}/versions")
        self.assertEqual(response.status_code, 200)

    def test_delete_model_version(self):
        """Test deleting a model version by IDs."""
        model_id = 'e45c278c-6cd2-4bf3-8a84-a6d6592ac0d9'  # Replace with actual model ID for testing
        version_id = '287103fb-5085-4837-b7bc-dbcce0fa2489'  # Replace with actual version ID for testing
        response = requests.delete(f"{self.BASE_URL}/models/{model_id}/versions/{version_id}")
        self.assertEqual(response.status_code,200)

    def test_model_version_inference(self):
        """Test model version inference on a model."""
        model_id = "dfbf7ae0-4329-499e-a11b-97cbba967734"  # Replace with actual model ID
        version_id = "287103fb-5085-4837-b7bc-dbcce0fa2489"  # Replace with actual version ID for testing
        response = requests.post(f"{self.BASE_URL}/models/{model_id}/versions/{version_id}/infer", json={"text": "abc", "apply_template": "False", "max_new_tokens": "256", "do_sample": "True", "temperature": "0.7", "top_k": "50","top_p": "0.95"})
        self.assertEqual(response.status_code, 200)
