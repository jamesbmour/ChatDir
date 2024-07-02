import logging
import os


def setup_logger(config):
    """
    Set up and return a logger based on the provided configuration.
    """
    logger = logging.getLogger('chatdir')
    logger.setLevel(config.get('level', 'INFO'))

    # Create a file handler
    log_file = config.get('file', 'chatdir.log')
    file_handler = logging.FileHandler(log_file)

    # Create a console handler
    console_handler = logging.StreamHandler()

    # Create a formatting configuration
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger