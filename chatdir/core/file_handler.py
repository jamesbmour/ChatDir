import os
from typing import List


class FileHandler:
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.current_directory = None

    def set_directory(self, directory: str):
        """
        Set the current working directory.
        """
        full_path = os.path.join(self.base_path, directory)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Directory not found: {full_path}")
        self.current_directory = full_path

    def list_files(self) -> List[str]:
        """
        List all files in the current directory.
        """
        if not self.current_directory:
            raise ValueError("No directory set. Use set_directory() first.")

        files = []
        for root, _, filenames in os.walk(self.current_directory):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files

    def read_file(self, file_path: str) -> str:
        """
        Read and return the contents of a file.
        """
        full_path = os.path.join(self.current_directory, file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")

        with open(full_path, 'r', encoding='utf-8') as file:
            return file.read()

    def get_file_info(self, file_path: str) -> dict:
        """
        Get information about a file (size, modification time, etc.).
        """
        full_path = os.path.join(self.current_directory, file_path)
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File not found: {full_path}")

        stat = os.stat(full_path)
        return {
            'path': full_path,
            'size': stat.st_size,
            'modified': stat.st_mtime,
            'created': stat.st_ctime,
        }