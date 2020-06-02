from fastapi import APIRouter, HTTPException
from typing import List

from .database import db
from .models import Provider, Database

# TODO: Accessing private attribute & undocumented error
# TODO: Creating anf root "info" endpoint

providers = APIRouter()
databases = APIRouter()


@providers.get("/", response_model=List[Provider])
async def get_all_providers():
    return db.providers


@providers.get("/{provider}", response_model=Provider)
async def get_provider_by_id(provider: str):
    if provider not in db._providers_table:
        raise HTTPException(status_code=404, detail="Provider id not found!")

    return db.get_provider(provider)


@providers.get("/{provider}/{database}", response_model=Database)
async def get_provider_by_id(provider: str, database: str):
    if provider not in db._providers_table or database not in db._providers_table[provider]:
        raise HTTPException(status_code=404, detail="Provider or database not found!")

    return db.get_provider(provider)


@databases.get("/", response_model=List[Database])
async def get_all_databases():
    return db.databases


@databases.get("/{database}", response_model=Database)
async def get_database_by_id(database: str):
    # TODO: Accessing private attribute & undocumented error
    if database not in db._databases_table:
        raise HTTPException(status_code=404, detail="Database id not found!")

    return db.get_database(database)
