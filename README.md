# ChatDir

CLI tool that allows you to chat with files in a directory using LLMs.

# Explanation of the Structure

- **README.md**: This file will contain an overview of your project, how to set it up, and how to use it.
- **setup.py**: This script is for setting up your package, including dependencies and entry points.
- **requirements.txt**: List of dependencies required for your project.
- **.gitignore**: Specifies files and directories to ignore in the git repository.
- **chatdir/**: The main package directory.
  - **__init__.py**: This file makes the directory a package.
  - **cli.py**: This file contains the code for the command-line interface.
  - **core/**: Directory for the core functionality of the tool.
    - **chat.py**: Logic for managing chat interactions.
    - **file_handler.py**: Logic for handling file operations.
    - **llm_local.py**: Interface for interacting with local LLMs.
    - **llm_api.py**: Interface for interacting with API-based LLMs.
    - **vector_db.py**: Logic for interacting with the local vector database.
  - **utils/**: Directory for utility functions and configurations.
    - **config.py**: Configuration settings for the project.
    - **logger.py**: Logging setup and utilities.
  - **tests/**: Directory for unit tests.
    - **test_chat.py**: Unit tests for chat logic.
    - **test_file_handler.py**: Unit tests for file handling logic.
    - **test_llm_local.py**: Unit tests for local LLM interactions.
    - **test_llm_api.py**: Unit tests for API-based LLM interactions.
    - **test_vector_db.py**: Unit tests for vector database interactions.
    - **test_cli.py**: Unit tests for the CLI functionality.
- **docs/**: Directory for documentation.
  - **index.md**: The main documentation index.
  - **usage.md**: Instructions on how to use the tool.
  - **api_reference.md**: API reference for developers.

### Details to Consider

- **CLI**: `cli.py` will use a library like `argparse` or `click` to handle command-line arguments and commands.
- **Local and API-based LLMs**: `llm_local.py` and `llm_api.py` will handle the logic for interacting with local and API-based large language models, respectively.
- **Local Vector Database**: `vector_db.py` will manage interactions with a local vector database, possibly using a library like `Faiss` or `Annoy`.
- **Testing**: Use a testing framework like `unittest` or `pytest` to write and run your tests.
