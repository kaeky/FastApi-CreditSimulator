import importlib
from pathlib import Path
from fastapi import APIRouter

def register_routers() -> APIRouter:
    main_router = APIRouter()
    base_path = Path(__file__).resolve().parent.parent

    # Buscar carpetas dentro de `src/` (excluyendo `config`)
    for module in base_path.iterdir():
        if module.is_dir() and module.name != "config":
            controllers_path = module / "controllers"
            if controllers_path.exists():
                # Buscar archivos que terminen en `_routes.py` dentro de la carpeta `controllers`
                for route_file in controllers_path.glob("*_routes.py"):
                    module_name = f"src.{module.name}.controllers.{route_file.stem}"
                    try:
                        module_router = importlib.import_module(module_name)
                        print(f"Importando {module_router}")
                        if hasattr(module_router, "router"):
                            main_router.include_router(
                                getattr(module_router, "router"),
                                prefix=f"/{module.name}",
                                tags=[module.name.capitalize()]
                            )
                    except Exception as e:
                        print(f"Error al importar {module_name}: {e}")
    return main_router
