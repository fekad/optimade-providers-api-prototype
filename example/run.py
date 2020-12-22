from optimade_providers_api import ProvidersAPI, db

app = ProvidersAPI(
    title="OPTIMADE Providers Index Meta-Database",
    description="The list of OPTIMADE providers keeps track of all reserved database-specific prefixes "
                "and the URLs to the index databases of all OPTIMADE database providers that participate "
                "in the OPTIMADE network."
)

# Injecting some data into the database

db.register_provider(
    id="cod",
    name="Crystallography Open Database",
    description="Open-access collection of crystal structures of organic, inorganic, metal-organics compounds "
                "and minerals, excluding biopolymers",
    homepage="https://www.crystallography.net/cod"
)

db.register_provider(
    id="tcod",
    name="Theoretical Crystallography Open Database",
    description="Open-access collection of theoretically calculated or refined crystal structures of organic, "
                "inorganic, metal-organic compounds and minerals, excluding biopolymers",
    homepage="https://www.crystallography.net/tcod"
)

db.register_provider(
    id="mcloud",
    name="Materials Cloud",
    description="Materials Cloud: A platform for Open Science built for seamless sharing of resources in "
                "computational materials science",
    homepage="https://www.materialscloud.org"
)

db.register_provider(
    id="odbx",
    name="open database of xtals",
    description="A public database of crystal structures mostly derived from ab initio structure prediction "
                "from the group of Dr Andrew Morris at the University of Birmingham https://ajm143.github.io",
    homepage="https://odbx.science"
)

db.register_database("mcloud",
    id="autowannier",
    name="Automated high-throughput Wannierisation",
    description="Validation results of an automated protocol for generating maximally-localized Wannier "
                "functions in a high-throughput framework.",
    homepage="https://materialscloud.org/discover/autowannier",
    api_versions=[{"version": "0.10",
                   "base_url": "https://dev-aiida-dev.materialscloud.org/autowannier/optimade/v0.10/"}]
)

db.register_database("mcloud",
    id="curated-cofs",
    name="CURATED covalent organic frameworks database",
    description="Database of experimentally reported Covalent-Organic Frameworks (COFs), provided with "
                "DFT-optimized geometry and DDEC partial charges for molecular simulations.",
    homepage="https://materialscloud.org/discover/curated-cofs",
    api_versions=[{"version": "0.10",
                   "base_url": "https://dev-aiida-dev.materialscloud.org/curated-cofs/optimade/v0.10/"}]
)

db.register_database("mcloud",
    id="optimade-sample",
    name="OPTIMADE Sample Database",
    description="Database with example structures for OPTIMADE tests.",
    homepage="https://materialscloud.org",
    api_versions=[{"version": "0.10",
                   "base_url": "https://dev-aiida-dev.materialscloud.org/optimade-sample/optimade/v0.10/"}]
)

db.register_database("mcloud",
    id="3dd",
    name="Three-dimensional crystals database",
    description="Curated set of relaxed three-dimensional crystal structures based on raw CIF data from the "
                "experimantal databases MPDS, COD, and ICSD.",
    homepage="https://materialscloud.org",
    api_versions=[{"version": "0.10",
                   "base_url": "https://dev-aiida-dev.materialscloud.org/3dd/optimade/v0.10/"}]
)

db.register_database("mcloud",
    id="hcofs-co2",
    name="COFs for CO2 capture and storage applications",
    description="A curated set of COFs with the highest Henry coefficient for CO2, where the full CO2 and N2 "
                "isotherm and the parasitic energy for the process have been computed.",
    homepage="https://materialscloud.org",
    api_versions=[{"version": "0.10",
                   "base_url": "https://dev-aiida-dev.materialscloud.org/hcofs-co2/optimade/v0.10/"}]
)

db.register_database("cod",
    id="cod",
    name="Crystallography Open Database",
    description="Open-access collection of crystal structures of organic, inorganic, metal-organics compounds "
                "and minerals, excluding biopolymers",
    homepage="https://www.crystallography.net/cod",
    api_versions=[{"version": "0.10",
                   "base_url": "http://www.crystallography.net/cod/optimade/v0.10.0/"}]
)

db.register_database("odbx",
    id="odbx",
    name="open database of xtals",
    description="A public database of crystal structures mostly derived from ab initio structure prediction "
                "from the group of Dr Andrew Morris at the University of Birmingham https://ajm143.github.io",
    homepage="https://odbx.science",
    api_versions=[{"version": "0.10",
                   "base_url": "https://optimade.odbx.science/v0.10/"},
                  {"version": "0.10.1",
                   "base_url": "https://optimade.odbx.science/v0.10/"}]
)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
