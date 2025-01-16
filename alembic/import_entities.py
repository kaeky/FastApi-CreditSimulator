import sys
import os
from pathlib import Path

# Obtener el directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Agregar la ruta de src para poder importar los módulos de entidades
sys.path.append(str(BASE_DIR / "src"))

# Lista para almacenar las clases de las entidades
entities = []

# Función para importar todas las entidades de todos los módulos
def import_entities():
    # Recorrer todos los directorios de los módulos dentro de src
    for module_dir in os.listdir(BASE_DIR / "src"):

        module_path = BASE_DIR / "src" / module_dir

        # Verificar que sea un directorio y que tenga la carpeta 'entities'
        if module_path.is_dir() and (module_path / "entities").exists():
            entities_path = module_path / "entities"
            for root, dirs, files in os.walk(entities_path):
                for file in files:
                    if file.endswith(".py") and file != "__init__.py":
                        module_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
                        module_path = module_path.replace(os.sep, ".")[:-3]  # Eliminar ".py"
                        print(f"Importando {module_path}")
                        # Intentamos importar el módulo
                        print(f"src.{module_dir}.entities.{module_path}")
                        try:
                            module = __import__(f"{module_path}", fromlist=["*"])
                            # Si tiene una clase que herede de Base, la agregamos a la lista de entidades
                            for attr_name in dir(module):
                                attr = getattr(module, attr_name)
                                if isinstance(attr, type) and hasattr(attr, "__tablename__"):
                                    entities.append(attr)
                        except ImportError as e:
                            print(f"Error importando {module_path}: {e}")
