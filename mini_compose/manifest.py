"""Configuration manifest"""
from pathlib import Path

import yaml
from pydantic import BaseModel

from mini_compose.entities import Service


class Config(BaseModel):
    """Compose configuration"""

    services: dict[str, Service]
    network: str


def read(manifest_file: str) -> Config:
    """Reads configuration from manifest file"""
    with open(manifest_file) as f:
        config = yaml.safe_load(f)

    directory = Path(manifest_file).absolute().parent.name

    # Name containers after the directory if no name is given
    for name, service in config.get("services", {}).items():
        if "container" not in service:
            service["container"] = f"{directory}-{name}"
        service["name"] = name

    return Config(network=f"{directory}-network", **config)
