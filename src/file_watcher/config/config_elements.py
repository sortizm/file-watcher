class FilesConfig:

    def __init__(self, directory, change, pattern):
        self.directory = directory
        self.change = change
        self.pattern = pattern


class NotificationsConfig:

    def __init__(self, level, error_period, email_receivers):
        self.level = level
        self.error_period = error_period
        self.email_receivers = email_receivers
