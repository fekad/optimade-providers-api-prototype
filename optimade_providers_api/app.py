from fastapi import FastAPI

from .database import db
from .routers import providers
from ._version import __version__


class ProvidersAPI(FastAPI):
    def __init__(self, title="OPTIMADE Providers Index Meta-Database", description=""):
        super().__init__(
            title=title,
            description=description,
            version=__version__,
            openapi_url="/schema",
            docs_url="/docs",
            redoc_url="",
        )

        self.include_router(providers, prefix="", tags=["Providers"])


if __name__ == "__main__":
    import uvicorn

    db.register_provider(
        id="mcloud",
        name="Materials Cloud",
        description="Materials Cloud: A platform for Open Science built for seamless sharing of resources in "
        "computational materials science",
        homepage="https://www.materialscloud.org",
    )

    db.register_database(
        "mcloud",
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

    app = ProvidersAPI(
        title="OPTIMADE Providers Index Meta-Database",
        description="The list of OPTIMADE providers keeps track of all reserved database-specific prefixes "
        "and the URLs to the index databases of all OPTIMADE database providers that participate "
        "in the OPTIMADE network.",
    )

    uvicorn.run(app, host="0.0.0.0", port=8000)
    # open: http://0.0.0.0:8000/mcloud/autowannier
