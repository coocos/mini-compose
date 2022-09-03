"""Container operations"""
import logging
import os

import docker
import docker.errors

from mini_compose.entities import Service

logger = logging.getLogger(__name__)
client = docker.client.from_env()


def exists(service: Service) -> bool:
    """Returns whether service container exists"""
    try:
        client.containers.get(service.container)
        return True
    except docker.errors.NotFound:
        return False


def create(service: Service):
    """Creates a new service container"""
    try:
        _ = client.images.get(service.image)
    except docker.errors.ImageNotFound:
        logger.info(f"{service.image} not found, pulling it...")
        client.images.pull(service.image)

    client.containers.run(
        service.image,
        name=service.container,
        ports=service.ports,
        environment={
            var: os.environ[var] for var in service.environment if var in os.environ
        },
        stdout=False,
        detach=True,
    )


def remove(service: Service):
    """Stops and removes a service container"""
    container = client.containers.get(service.container)
    container.remove(force=True)
