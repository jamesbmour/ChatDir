import os
import requests
from dotenv import load_dotenv
from typing import Dict, Any, Optional

# Load environment variables from .env file
load_dotenv()


class LLMAPI:
    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")
        self.api_endpoint = os.getenv("LLM_API_ENDPOINT", "http://localhost:11434")
        self.model = os.getenv("LLM_MODEL", "gemma2")  # Default model is now 'gemma2'

        # Convert "None" string to None
        if self.api_key == "None":
            self.api_key = None

    def generate(self, prompt: str, max_tokens: int = 100, temperature: float = 0.7) -> Dict[str, Any]:
        """
        Generate a response using the configured LLM API.
        """
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": temperature,
            }
        }

        try:
            response = requests.post(f"{self.api_endpoint}/api/generate", json=payload, headers=headers)
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
        Set a custom API key. Use None to remove the API key.
        """
        self.api_key = api_key if api_key != "None" else None

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


if __name__ == "__main__":
    llm_api = LLMAPI()
    response = llm_api.generate("Hello, how are you?")
    print(response)

    models = llm_api.get_available_models()
    print(models)