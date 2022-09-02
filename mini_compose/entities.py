"""Domain entities"""
from pydantic import BaseModel, validator


class Service(BaseModel):
    """Service to start"""

    name: str
    container: str
    image: str

    ports: dict[int, int]

    @validator("ports", pre=True)
    @classmethod
    def split_ports(cls, v: str) -> dict[int, int]:
        """Maps port pairs like '1234:1234' to (1234, 1234)"""
        ports: dict[int, int] = {}
        for port in v:
            host, container = port.split(":")
            ports[int(container)] = int(host)
        return ports
