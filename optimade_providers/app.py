from fastapi import FastAPI

from ._version import __version__
from .routers import providers, databases


class ProvidersAPI(FastAPI):

    def __init__(self, title="OPTIMADE Providers Index Meta-Database", description=""):
        super().__init__(title=title, description=description, version=__version__,
                         openapi_url="/api/openapi.json", docs_url="/api/docs", redoc_url="")

        self.include_router(providers, prefix="/providers", tags=["Providers"])
        self.include_router(databases, prefix="/databases", tags=["Databases"])


if __name__ == "__main__":
    import uvicorn

    app = ProvidersAPI(
        title="OPTIMADE Providers Index Meta-Database",
        description="The list of OPTIMADE providers keeps track of all reserved database-specific prefixes "
                    "and the URLs to the index databases of all OPTIMADE database providers that participate "
                    "in the OPTIMADE network."
    )

    uvicorn.run(app, host="0.0.0.0", port=8000)
