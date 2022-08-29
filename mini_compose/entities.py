"""Domain entities"""
from pydantic import BaseModel


class Service(BaseModel):
    """Service to start"""

    name: str
    image: str

    ports: list[str]
