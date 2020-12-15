import logging


def get_logger(cls):
    # Create a custom logger
    logger = logging.getLogger(cls)

    # Create handlers
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.WARNING)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    logger.addHandler(c_handler)
    return logger
