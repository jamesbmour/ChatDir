# ChatDir

CLI tool that allows you to chat with files in a directory using LLMs.

---

# ChatDir: Chat with Files in a Directory

## Overview

**ChatDir** is a powerful command-line interface (CLI) tool designed to enable users to interactively chat with files in a directory. Leveraging the capabilities of both local and API-based large language models (LLMs), ChatDir provides an intuitive interface to explore, analyze, and gain insights from your files using natural language processing (NLP) techniques.

Whether you need to quickly summarize documents, search for specific information, or understand complex datasets, ChatDir makes it easy to communicate with your files as if you were having a conversation.

## Features

- **Local and API-Based LLMs**: Seamlessly switch between local LLMs for offline processing and API-based LLMs for leveraging the latest advancements in NLP.
- **File Handling**: Efficiently manage and process files within a specified directory, supporting various file types and formats.
- **Vector Database Integration**: Utilize a local vector database for efficient similarity search and data retrieval.
- **User-Friendly CLI**: Intuitive command-line interface built with Click for easy interaction and command execution.
- **Extensible Architecture**: Modular design allows for easy extension and customization of functionality.

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

Here’s a detailed project description for your CLI tool, which you can use for your `README.md` or other documentation:


## Installation

### Prerequisites

- Python 3.9 or higher
- Poetry for dependency management

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/chatdir.git
   cd chatdir
   ```

2. **Install dependencies**:
   ```bash
   poetry install
   ```

3. **Activate the environment**:
   ```bash
   poetry shell
   ```

4. **Run the tool**:
   ```bash
   chatdir --help
   ```

## Usage

### Basic Command

To start a chat session with files in a specific directory:

```bash
chatdir chat <directory_path> [--use-api]
```

- `<directory_path>`: Path to the directory containing files you want to interact with.
- `--use-api`: Optional flag to use an API-based LLM instead of the local LLM.

### Example

```bash
chatdir chat /path/to/your/files --use-api
```

This command initializes a chat session with the files in the specified directory using the API-based LLM.

## Configuration

The configuration for ChatDir is managed through a `config.yaml` file. This file includes settings for file paths, LLM configurations, and logging. Below is an example configuration:

```yaml
file_path: /default/path/to/files
vector_db_path: /default/path/to/vector_db
local_llm:
  model_name: gpt-3
api_llm:
  api_key: YOUR_API_KEY
  endpoint: https://api.example.com
logging:
  logfile: /path/to/logfile.log
```

## Contributing

We welcome contributions to ChatDir! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

### Development Setup

1. **Fork the repository**.
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/chatdir.git
   cd chatdir
   ```
3. **Create a new branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**.
5. **Run tests**:
   ```bash
   pytest
   ```
6. **Commit your changes** and **push to your fork**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature/your-feature-name
   ```
7. **Open a pull request** on GitHub.

## License

ChatDir is licensed under the MIT License. See the `LICENSE` file for more details.

---

This description provides a comprehensive overview of the project, including installation instructions, usage examples, configuration details, and contribution guidelines.