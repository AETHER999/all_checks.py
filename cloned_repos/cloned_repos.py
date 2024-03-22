# all_checks.py
import os
from github import Repo

repos = [
    "https://github.com/AETHER999/auto-update.py.git",
    "https://github.com/AETHER999/date_time.py.git",
    "https://github.com/AETHER999/free_memory.py.git",
    "https://github.com/AETHER999/google_guide_line.py.git",
    "https://github.com/AETHER999/inventory.py.git",
    "https://github.com/AETHER999/metronome.py.git",
    "https://github.com/AETHER999/planet_gravity.py.git",
    "https://github.com/AETHER999/practicas.py.git"
]

# script.py

# Ruta al archivo repos.py
REPOS_FILE = "all_checks.py"

# Carpeta donde se guardarán los repositorios clonados
CLONE_FOLDER = "cloned_repos"

def clone_repositories():
    # Crear la carpeta si no existe
    if not os.path.exists(CLONE_FOLDER):
        os.makedirs(CLONE_FOLDER)

    # Importar la lista de repositorios
    from repos import repos

    # Clonar cada repositorio
    for repo_url in repos:
        # Obtener el nombre del repositorio
        repo_name = repo_url.split("/")[-1].split(".git")[0]

        # Clonar el repositorio
        repo_path = os.path.join(CLONE_FOLDER, repo_name)
        Repo.clone_from(repo_url, repo_path)

        print(f"Repositorio clonado: {repo_url}")

if __name__ == "__main__":
    clone_repositories()
