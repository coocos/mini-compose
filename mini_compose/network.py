"""Container network operations"""
import docker
import docker.errors
from docker.models.networks import Network

client = docker.client.from_env()


def create(name: str) -> Network:
    """Creates a new network if needed and returns it"""
    try:
        return client.networks.get(name)
    except docker.errors.NotFound:
        return client.networks.create(name, "bridge")


def delete(name: str) -> bool:
    """Deletes network"""
    try:
        network = client.networks.get(name)
        network.remove()
        return True
    except docker.errors.NotFound:
        return False
