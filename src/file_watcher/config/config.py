"""
Configuration of the file-watcher
"""
from typing import List
from typing.io import TextIO

from .config_elements import FilesConfig, NotificationsConfig


class Config:
    """
    The configuration object

    Methods:
        from_config_files: creates this object from a config file handler

    Attributes:
        * files: the files configuration
        * notifications: the notifications configuration
    """

    def __init__(self,
                 files: List[FilesConfig],
                 notifications: NotificationsConfig):
        """
        Initialises the config object

        Args:
            files: the files configuration
            notifications: the notifications configuration
        """
        self.files = files
        self.notifications = notifications

    @classmethod
    def from_config_file(cls, config_file_handler: TextIO) -> 'Config':
        """

        Args:
            config_file_handler: the config file handler

        Returns:
            an object of this class
        """
        pass

