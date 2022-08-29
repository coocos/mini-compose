import logging

import docker

logger = logging.getLogger(__name__)


def create(image: str, name: str):
    """Creates a new container"""
    client = docker.client.from_env()

    try:
        _ = client.images.get(image)
    except docker.errors.ImageNotFound:
        logger.info(f"{image} not found, pulling it...")
        client.images.pull(image)

    client.containers.run(image, name=name, stdout=False, detach=True)


def remove(name: str):
    """Stops and removes a container"""
    client = docker.client.from_env()
    container = client.containers.get(name)
    container.remove(force=True)
