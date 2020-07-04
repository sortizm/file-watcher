import logging

from .config.config import Config


def watch(configuration: Config):
    logging.debug(f'Configuration object is: {configuration!r}')
