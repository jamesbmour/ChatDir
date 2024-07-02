import yaml
import os


class Config:
    @staticmethod
    def load_config(config_path=None):
        """
        Load configuration from a YAML file.
        If no path is provided, it looks for a 'config.yaml' in the current directory.
        """
        if not config_path:
            config_path = os.path.join(os.getcwd(), 'config.yaml')

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)

        return config

    @staticmethod
    def get_default_config():
        """
        Return a dictionary with default configuration values.
        """
        return {
            'file_path': os.getcwd(),
            'vector_db_path': os.path.join(os.getcwd(), 'vector_db'),
            'local_llm': {
                'model_path': 'path/to/local/model',
                'context_length': 2048,
            },
            'api_llm': {
                'api_key': 'your_api_key_here',
                'model': 'gpt-3.5-turbo',
            },
            'logging': {
                'level': 'INFO',
                'file': 'chatdir.log',
            },
        }