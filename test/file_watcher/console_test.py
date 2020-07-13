import logging
from logging import ERROR, INFO, DEBUG

import pytest
from assertpy import assert_that
from click.testing import CliRunner
from file_watcher.console import run


@pytest.fixture(autouse=True)
def mocked_logging_basic_config(mocker):
    return mocker.spy(logging, 'basicConfig')


@pytest.fixture(autouse=True)
def mocked_open(mocker):
    return mocker.patch("builtins.open")


@pytest.fixture(autouse=True)
def mocked_config(mocker):
    return mocker.patch("file_watcher.config.config.Config.from_config_file")


@pytest.fixture(autouse=True)
def mocked_watch(mocker):
    return mocker.patch("file_watcher.file_watcher.watch")


def test_config_file_is_required():
    # given
    runner = CliRunner()

    # when
    result = runner.invoke(run)

    # then
    assert_that(result.exit_code).is_not_zero()
    assert_that(result.output).contains(
        "Error: Missing option '-c' / '--config-file'")


def test_default_verbosity_is_error(mocked_logging_basic_config):
    # given
    runner = CliRunner()

    # when
    runner.invoke(run, ['-c', 'my_config.yaml'])

    # then
    mocked_logging_basic_config.assert_called_with(level=ERROR)


def test_set_verbosity_info(mocked_logging_basic_config):
    # given
    runner = CliRunner()

    # when
    runner.invoke(run, ['-c', 'my_config.yaml', '-v'])

    # then
    mocked_logging_basic_config.assert_called_with(level=INFO)


def test_set_verbosity_debug(mocked_logging_basic_config):
    # given
    runner = CliRunner()

    # when
    runner.invoke(run, ['-c', 'my_config.yaml', '-vv'])

    # then
    mocked_logging_basic_config.assert_called_with(level=DEBUG)


def test_set_verbosity_is_clamped_to_debug(mocked_logging_basic_config):
    # given
    runner = CliRunner()

    # when
    runner.invoke(run, ['-c', 'my_config.yaml', '-vvv'])

    # then
    mocked_logging_basic_config.assert_called_with(level=DEBUG)
