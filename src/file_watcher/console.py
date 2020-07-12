import logging
from logging import ERROR, INFO, DEBUG

import click

from .config.config import Config
from .file_watcher import watch

LOG_LEVEL = [ERROR, INFO, DEBUG]


@click.command()
@click.option('-c', '--config-file',
              required=True,
              help='Configuration file to use')
@click.option('-v', 'verbosity',
              count=True, type=click.IntRange(0, 2, clamp=True),
              help='Verbosity (v, vv)')
def run(config_file, verbosity):
    """Configurable File watcher & notifier"""
    logging.basicConfig(level=LOG_LEVEL[verbosity])
    with open(config_file, 'r') as config_file_handler:
        logging.info(f'Reading configuration from file {config_file}')
        config = Config.from_config_file(config_file_handler)
    watch(config)
