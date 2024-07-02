import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any, Optional

# Load environment variables from .env file
load_dotenv()

class LLMAPI:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")
        self.api_endpoint = os.getenv("LLM_API_ENDPOINT", "http://localhost:11434/api/generate")  # Default to Ollama
        self.model = os.getenv("LLM_MODEL", "llama2")  # Default model for Ollama

    def generate(self, prompt: str, max_tokens: int = 100, temperature: float = 0.7) -> Dict[str, Any]:
        """
        Generate a response using the configured LLM API.
        """
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "prompt": prompt,
            "model": self.model,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        try:
            response = requests.post(self.api_endpoint, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error calling LLM API: {e}")
            return {"error": str(e)}

    def set_model(self, model: str):
        """
        Set the model to be used for generation.
        """
        self.model = model

    def set_api_endpoint(self, endpoint: str):
        """
        Set a custom API endpoint.
        """
        self.api_endpoint = endpoint

    def set_api_key(self, api_key: str):
        """
        Set a custom API key.
        """
        self.api_key = api_key

    @staticmethod
    def get_available_models() -> Optional[Dict[str, Any]]:
        """
        Get a list of available models from the Ollama API.
        """
        try:
            response = requests.get("http://localhost:11434/api/tags")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching available models: {e}")
            return None