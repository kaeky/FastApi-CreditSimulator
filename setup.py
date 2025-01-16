from setuptools import setup, find_packages

setup(
    name="PythonFastApi",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "alembic",
        "sqlalchemy",
        "uvicorn",
        "python-decouple"
        "strawberry-graphQL"
        # Agrega otras dependencias necesarias
    ],
    entry_points={
        "console_scripts": [
            "run-app=main:main",  # Reemplaza "main:main" si tu función de inicio está en otro lugar
        ]
    },
)
