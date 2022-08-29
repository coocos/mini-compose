import logging

import docker
import docker.errors

from mini_compose.entities import Service

logger = logging.getLogger(__name__)


def exists(service: Service) -> bool:
    """Returns whether service exists"""
    client = docker.client.from_env()
    try:
        _ = client.containers.get(service.name)
        return True
    except docker.errors.NotFound:
        return False


def create(service: Service):
    """Creates a new service container"""
    client = docker.client.from_env()

    try:
        _ = client.images.get(service.image)
    except docker.errors.ImageNotFound:
        logger.info(f"{service.image} not found, pulling it...")
        client.images.pull(service.image)

    client.containers.run(service.image, name=service.name, stdout=False, detach=True)


def remove(service: Service):
    """Stops and removes a service container"""
    client = docker.client.from_env()
    container = client.containers.get(service.name)
    container.remove(force=True)
