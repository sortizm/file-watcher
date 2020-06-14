import click
import yaml
import logging

from yaml import Loader, Dumper
from logging import ERROR, INFO, DEBUG

LOG_LEVEL = [ERROR, INFO, DEBUG]


@click.command()
@click.option('-c', '--config-file', required=True, help='Configuration file to use')
@click.option('-v', 'verbosity', count=True, type=click.IntRange(0, 2, clamp=True), help='Verbosity (v, vv)')
def main(config_file, verbosity):
    """Configurable File watcher & notifier"""
    logging.basicConfig(level=LOG_LEVEL[verbosity])
    logging.info(f"Reading configuration from file {config_file}")
    with open(config_file, 'r') as config:
        print(yaml.dump(yaml.load(config, Loader=Loader), Dumper=Dumper))
