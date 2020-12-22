from enum import Enum
from typing import List, Dict, Optional
from pydantic import BaseModel, HttpUrl


class APIVersion(BaseModel):
    version: str
    base_url: HttpUrl

    class Config:
        schema_extra = {
            "example": {
                "version": "v0.10",
                "base_url": "https://example.com/optimade/v0.10/",
            }
        }


class State(str, Enum):
    available = "available"
    unavailable = "unavailable"
    unknown = "unknown"


class Status(BaseModel):
    state: State
    api_version: str


class Database(BaseModel):
    id: str
    name: str
    description: Optional[str]
    homepage: Optional[HttpUrl]
    api_versions: Optional[List[APIVersion]] = []

    # TODO: Supporting only a the latest version
    # base_url: HttpUrl
    # status: Optional[Status]

    class Config:
        schema_extra = {
            "example": {
                "id": "exmpl_exmpl",
                "name": "Example Database",
                "description": "a short description of the database",
                "homepage": "https://example.com",
                "latest_api_version": "v0.10.1",
                "api_versions": [APIVersion.Config.schema_extra["example"]],
            }
        }


class Provider(BaseModel):
    id: str
    name: str
    description: str
    homepage: HttpUrl
    databases: Dict[str, Database] = {}

    # TODO: Using set instead of list
    # databases: Optional[Set[Database]] = set()

    class Config:
        schema_extra = {
            "example": {
                "id": "exmpl",
                "name": "Example provider",
                "description": "Provider used for examples, not to be assigned to a real database",
                "homepage": "https://example.com",
                "databases": [Database.Config.schema_extra["example"]],
            }
        }
