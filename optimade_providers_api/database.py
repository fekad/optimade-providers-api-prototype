from typing import List, Dict
from pydantic import BaseModel

from .models import Provider, Database


class ProviderDatabase(BaseModel):
    _table: Dict[str, Provider] = {}

    @property
    def providers(self) -> List[Provider]:
        return list(self._table.values())

    def get_provider(self, id: str) -> Provider:
        return self._table[id]

    def get_database(self, provider_id: str, id: str) -> Database:
        return self._table[provider_id].databases[id]

    def register_provider(self, **kwargs):
        data = Provider(**kwargs)

        if data.id in self._table:
            raise KeyError

        self._table[data.id] = data

    def register_database(self, provider_id: str, /, **kwargs):
        data = Database(**kwargs)

        if provider_id not in self._table:
            raise KeyError

        if data.id in self._table[provider_id].databases:
            raise KeyError

        self._table[provider_id].databases[data.id] = data


db = ProviderDatabase()

if __name__ == "__main__":
    db.register_provider(
        id="mcloud",
        name="Materials Cloud",
        description="Materials Cloud: A platform for Open Science built for seamless sharing of resources in "
        "computational materials science",
        homepage="https://www.materialscloud.org",
    )

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
        ],
    )

    print(db.providers)
    print(db.get_provider("mcloud"))

