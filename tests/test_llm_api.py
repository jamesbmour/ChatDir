import unittest
from unittest.mock import patch, MagicMock
import os
import json
from chatdir.core.llm_api import LLMAPI


class TestLLMAPI(unittest.TestCase):

    def setUp(self):
        # Set up environment variables for testing
        os.environ['LLM_API_KEY'] = 'test_api_key'
        os.environ['LLM_API_ENDPOINT'] = 'http://test.api/generate'
        os.environ['LLM_MODEL'] = 'test_model'
        self.llm_api = LLMAPI()

    def tearDown(self):
        # Clean up environment variables after tests
        del os.environ['LLM_API_KEY']
        del os.environ['LLM_API_ENDPOINT']
        del os.environ['LLM_MODEL']

    def test_init(self):
        self.assertEqual(self.llm_api.api_key, 'test_api_key')
        self.assertEqual(self.llm_api.api_endpoint, 'http://test.api/generate')
        self.assertEqual(self.llm_api.model, 'test_model')

    def test_set_model(self):
        self.llm_api.set_model('new_model')
        self.assertEqual(self.llm_api.model, 'new_model')

    def test_set_api_endpoint(self):
        self.llm_api.set_api_endpoint('http://new.api/generate')
        self.assertEqual(self.llm_api.api_endpoint, 'http://new.api/generate')

    def test_set_api_key(self):
        self.llm_api.set_api_key('new_api_key')
        self.assertEqual(self.llm_api.api_key, 'new_api_key')

    @patch('requests.post')
    def test_generate_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"generated_text": "Hello, world!"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        response = self.llm_api.generate("Test prompt")

        self.assertEqual(response, {"generated_text": "Hello, world!"})
        mock_post.assert_called_once()
        _, kwargs = mock_post.call_args
        self.assertEqual(kwargs['json']['prompt'], "Test prompt")
        self.assertEqual(kwargs['json']['model'], "test_model")

    @patch('requests.post')
    def test_generate_error(self, mock_post):
        mock_post.side_effect = Exception("API Error")

        response = self.llm_api.generate("Test prompt")

        self.assertEqual(response, {"error": "API Error"})

    @patch('requests.get')
    def test_get_available_models_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"models": ["model1", "model2"]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        models = LLMAPI.get_available_models()

        self.assertEqual(models, {"models": ["model1", "model2"]})
        mock_get.assert_called_once_with("http://localhost:11434/api/tags")

    @patch('requests.get')
    def test_get_available_models_error(self, mock_get):
        mock_get.side_effect = Exception("API Error")

        models = LLMAPI.get_available_models()

        self.assertIsNone(models)

    def test_default_values(self):
        # Test default values when environment variables are not set
        del os.environ['LLM_API_ENDPOINT']
        del os.environ['LLM_MODEL']

        llm_api = LLMAPI()

        self.assertEqual(llm_api.api_endpoint, "http://localhost:11434/api/generate")
        self.assertEqual(llm_api.model, "gemma2")


if __name__ == '__main__':
    unittest.main()