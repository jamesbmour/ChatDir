from setuptools import setup, find_packages

setup(
    name="chatdir",
    version="0.1.0",
    description="A CLI tool to chat with files in a directory",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "click",
        "transformers",
        "openai",
        "faiss-cpu",
        "annoy",
        "pandas",
        "pyyaml",
        "loguru",
        "pytest",
        "pytest-mock",
        "sphinx"
    ],
    entry_points={
        'console_scripts': [
            'chatdir=chatdir.cli:main',
        ],
    },
)
