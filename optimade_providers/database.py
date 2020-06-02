from typing import List, Dict
from pydantic import BaseModel

from .models import Provider, Database


class DB(BaseModel):
    _providers_table: Dict[str, Provider] = {}
    _databases_table: Dict[str, Database] = {}

    @property
    def providers(self) -> List[Provider]:
        return list(self._providers_table.values())

    @property
    def databases(self) -> List[Database]:
        return list(self._databases_table.values())

    def get_provider(self, id: str) -> Provider:
        return self._providers_table[id]

    def get_database(self, id: str) -> Database:
        return self._databases_table[id]

    def register_provider(self, **kwargs):
        data = Provider(**kwargs)
        self._providers_table[data.id] = data

    def register_database(self, **kwargs):
        data = Database(**kwargs)

        if data.provider_id not in self._providers_table:
            raise KeyError

        # Update the relationship
        self._providers_table[data.provider_id].databases.append(data)
        self._databases_table[data.id] = data


db = DB()

if __name__ == '__main__':
    db.register_provider(
        id="mcloud",
        name="Materials Cloud",
        description="Materials Cloud: A platform for Open Science built for seamless sharing of resources in "
                    "computational materials science",
        homepage="https://www.materialscloud.org")

    db.register_database(
        provider_id="mcloud",
        id="autowannier",
        name="Automated high-throughput Wannierisation",
        description="Validation results of an automated protocol for generating maximally-localized Wannier "
                    "functions in a high-throughput framework.",
        homepage="https://materialscloud.org/discover/autowannier",
        api_versions=[
            {
                "version": "0.10",
                "base_url": "https://dev-aiida-dev.materialscloud.org/autowannier/optimade/v0.10/",
            }
        ]

    )

    print(db.providers)
    print(db.get_provider("mcloud"))

    print(db.databases)
    print(db.get_database("autowannier"))
