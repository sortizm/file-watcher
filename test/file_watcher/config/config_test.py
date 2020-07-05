from io import StringIO

import pytest
from assertpy import assert_that
from file_watcher.config.config import Config
from file_watcher.config.config_elements import FilesConfig, NotificationsConfig

UNEXPECTED_ELEMENT_CONFIGURATION = """
files:
  my_files:
    directory: /some/stuff
    change: modification
notifications:
  email_receivers: [steve@abc.com]
my_new_unexpected_element:
  info: hello
"""

TWO_FILES_CONFIGURATION = """
files:
  my_files:
    directory: /some/stuff
    change: modification
    pattern: '*.txt'
  other_files:
    directory: /other/stuff
    change: creation
notifications:
  period: 0.5
  email_receivers: [steve@abc.com]
"""

SINGLE_FILE_CONFIGURATION = """
files:
  my_files:
    directory: /some/stuff
    change: modification
    pattern: '*.txt'
notifications:
  period: 0.5
  email_receivers: [steve@abc.com]
"""


def test_value_error_on_unexpected_element():
    # given
    config_stream = StringIO(UNEXPECTED_ELEMENT_CONFIGURATION)

    # when
    with pytest.raises(ValueError, match='.* my_new_unexpected_element'):
        Config.from_config_file(config_stream)


def test_loads_files_section_to_files_config():
    # given
    config_stream = StringIO(TWO_FILES_CONFIGURATION)

    # when
    config = Config.from_config_file(config_stream)

    # then
    assert_that(config.files).extracting('directory').contains_only(
        '/some/stuff', '/other/stuff')


def test_loads_all_files_section_info_to_files_config():
    # given
    config_stream = StringIO(SINGLE_FILE_CONFIGURATION)

    # when
    config = Config.from_config_file(config_stream)

    # then
    expected_files_config = FilesConfig('/some/stuff', 'modification', '*.txt')
    assert_that(config.files[0]).is_equal_to(expected_files_config)


def test_loads_notifications_section_to_notifications_config():
    # given
    config_stream = StringIO(SINGLE_FILE_CONFIGURATION)

    # when
    config = Config.from_config_file(config_stream)

    # then
    expected_notifications_config = NotificationsConfig(['steve@abc.com'], 0.5)
    assert_that(config.notifications).is_equal_to(expected_notifications_config)
