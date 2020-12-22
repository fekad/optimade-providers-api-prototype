from typing import List
from fastapi import APIRouter, HTTPException

from .database import db
from .models import Provider, Database

# TODO: Accessing private attribute & undocumented error

providers = APIRouter()


@providers.get("/", response_model=List[Provider])
async def get_all_providers():
    return db.providers


@providers.get("/{provider}", response_model=Provider)
async def get_provider_by_id(provider: str):
    if provider not in db._table:
        raise HTTPException(status_code=404, detail="Provider id not found!")

    return db.get_provider(provider)


@providers.get("/{provider}/{database}", response_model=Database)
async def get_database_by_id(provider: str, database: str):

    if provider not in db._table:
        raise HTTPException(status_code=404, detail="Provider id not found!")

    if database not in db._table[provider].databases:
        raise HTTPException(status_code=404, detail="Database not found!")

    return db.get_database(provider, database)

