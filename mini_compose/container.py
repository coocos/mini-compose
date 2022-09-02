"""Container operations"""
import logging

import docker
import docker.errors
from docker.models.networks import Network

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
        stdout=False,
        detach=True,
    )


def remove(service: Service):
    """Stops and removes a service container"""
    container = client.containers.get(service.container)
    container.remove(force=True)


def create_network(name: str) -> Network:
    """Creates a new network if needed and returns it"""
    try:
        return client.networks.get(name)
    except docker.errors.NotFound:
        return client.networks.create(name, "bridge")


def delete_network(name: str) -> bool:
    """Deletes network"""
    try:
        network = client.networks.get(name)
        network.remove()
        return True
    except docker.errors.NotFound:
        return False
