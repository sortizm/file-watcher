class FilesConfig:

    def __init__(self, directory, change, pattern=None):
        self.directory = directory
        self.change = change
        self.pattern = pattern


class NotificationsConfig:

    def __init__(self,
                 level,
                 email_receivers,
                 error_period=None,
                 info_period=None):
        self.level = level
        self.error_period = error_period
        self.info_period = info_period
        self.email_receivers = email_receivers
