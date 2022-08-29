"""Container operations"""
import logging

import docker
import docker.errors

from mini_compose.entities import Service

logger = logging.getLogger(__name__)
client = docker.client.from_env()


def exists(service: Service) -> bool:
    """Returns whether service exists"""
    try:
        _ = client.containers.get(service.name)
        return True
    except docker.errors.NotFound:
        return False


def create(service: Service, network: str):
    """Creates a new service container"""
    try:
        _ = client.images.get(service.image)
    except docker.errors.ImageNotFound:
        logger.info(f"{service.image} not found, pulling it...")
        client.images.pull(service.image)

    client.containers.run(
        service.image, name=service.name, network=network, stdout=False, detach=True
    )


def remove(service: Service):
    """Stops and removes a service container"""
    container = client.containers.get(service.name)
    container.remove(force=True)


def create_network(name: str) -> bool:
    """
    Creates a new network if it does not exist yet.
    Returns a boolean indicating if the network was created
    """
    try:
        _ = client.networks.get(name)
        return False
    except docker.errors.NotFound:
        client.networks.create(name, "bridge")
        return True


def delete_network(name: str) -> bool:
    """Deletes network"""
    try:
        network = client.networks.get(name)
        network.remove()
        return True
    except docker.errors.NotFound:
        return False
