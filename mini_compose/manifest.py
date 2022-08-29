"""Configuration manifest"""
import logging
from pathlib import Path

import yaml
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class Service(BaseModel):
    """Service to start"""

    name: str
    image: str

    ports: list[str]


class Config(BaseModel):
    """Compose configuration"""

    services: dict[str, Service]


def read(manifest_file: str) -> Config:
    """Reads configuration from manifest file"""
    with open(manifest_file) as f:
        config_yaml = yaml.safe_load(f)

    # Name containers after the directory if no name is given
    for name, service in config_yaml.get("services", {}).items():
        if "name" not in service:
            directory = Path(manifest_file).parent.name
            service["name"] = f"{directory}-{name}"

    return Config(**config_yaml)
