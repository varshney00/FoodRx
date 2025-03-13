import unittest
import requests

class TestUI(unittest.TestCase):
    def test_ui_response(self):
        response = requests.get("http://127.0.0.1:8000/recipes/?diet=gluten-free")
        self.assertEqual(response.status_code, 200)
        self.assertIn("recipes", response.json())

if __name__ == "__main__":
    unittest.main()
