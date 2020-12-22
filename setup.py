from setuptools import setup, find_packages

setup(
    name='optimade_providers_api',
    version='0.2.0',
    author='Adam Fekete',
    author_email='adam@fekete.co.uk',
    description='This is an prototype implementation of the OPTIMADE\'s providers API',
    keywords='optimade, database',
    url='https://github.com/fekad/optimade-providers-api-prototypei',
    project_urls={
        'Documentation': 'https://fekad.github.io/optimade-providers-api-prototype/',
        'Source Code': 'https://github.com/fekad/optimade-providers-api-prototype',
    },
    packages=find_packages(),
    install_requires=['fastapi'],
    extras_require={
        'tests': ['pytest'],
    },
    test_require=['pytest'],
    python_requires='>=3.8'
)
