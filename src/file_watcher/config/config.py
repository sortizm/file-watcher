"""
Configuration of the file-watcher
"""
import logging
from dataclasses import dataclass
from typing import List
from typing.io import TextIO

import yaml
from yaml import Loader

from .config_elements import FilesConfig, NotificationsConfig


@dataclass
class Config:
    """
    The configuration object

    Methods:
        from_config_files: creates this object from a config file handler

    Attributes:
        * files: the files configuration
        * notifications: the notifications configuration
    """
    files: List[FilesConfig]
    notifications: NotificationsConfig

    @classmethod
    def from_config_file(cls, text_stream: TextIO) -> 'Config':
        """

        Args:
            text_stream: the configuration

        Returns:
            an object of this class
        """
        files = []
        notifications = None
        for key, val in yaml.load(text_stream, Loader=Loader).items():
            logging.debug(f'Config element {key!r}: {val}')
            if key == 'files':
                files = [FilesConfig(**config) for config in
                         val.values()]
            elif key == 'notifications':
                notifications_config = val
                notifications = NotificationsConfig(**notifications_config)
            else:
                raise ValueError(f'Unexpected element {key}')

        return cls(files, notifications)

