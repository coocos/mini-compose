"""CLI entrypoint"""
import logging

import click

from mini_compose import container, manifest

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)


@click.group()
def cli():
    """Miniature container orchestrator"""
    pass


@click.command()
@click.option("--file", default="mini-compose.yml", help="Compose file")
def down(file: str):
    """Tear down containers"""
    config = manifest.read(file)
    for service in config.services.values():
        logger.info(f"Stopping {service.name}")
        container.remove(service.name)


@click.command()
@click.option("--file", default="mini-compose.yml", help="Compose file")
def up(file: str):
    """Create containers"""
    config = manifest.read(file)
    for service in config.services.values():
        logger.info(f"Starting {service.name}")
        container.create(service.image, service.name)


cli.add_command(up)
cli.add_command(down)

if __name__ == "__main__":
    cli()
