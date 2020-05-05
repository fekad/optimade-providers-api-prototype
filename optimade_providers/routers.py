from fastapi import APIRouter, HTTPException
from typing import List

from .database import db
from .models import Provider, Database

providers, databases = APIRouter(), APIRouter()


@providers.get("/", response_model=List[Provider])
async def get_all_providers():
    return db.providers


@providers.get("/{id}", response_model=Provider)
async def get_provider_by_id(id: str):
    # TODO: Accessing private attribute & undocumented error
    if id not in db._providers_table:
        raise HTTPException(status_code=404, detail="Provider id not found!")

    return db.get_provider(id)


@databases.get("/", response_model=List[Database])
async def get_all_databases():
    return db.databases


@databases.get("/{id}", response_model=Database)
async def get_database_by_id(id: str):
    # TODO: Accessing private attribute & undocumented error
    if id not in db._databases_table:
        raise HTTPException(status_code=404, detail="Database id not found!")

    return db.get_database(id)
