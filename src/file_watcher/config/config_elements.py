from dataclasses import dataclass
from typing import List


@dataclass
class FilesConfig:
    """
    Configuration for the files to be watched
    """
    directory: str
    change: str
    pattern: str = None


@dataclass
class NotificationsConfig:
    """
    Configuration for the notifications
    """
    email_receivers: List[str]
    period: float = None
