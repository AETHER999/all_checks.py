#!/usr/bin/env python3

import os
import git
from git.exc import GitCommandError

# Lista de repositorios
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

# Carpeta donde se guardarán los repositorios clonados
CLONE_FOLDER = "cloned_repos"

def clone_repositories():
    # Crear la carpeta si no existe
    if not os.path.exists(CLONE_FOLDER):
        os.makedirs(CLONE_FOLDER)

    # Clonar cada repositorio
    for repo_url in repos:
        # Obtener el nombre del repositorio
        repo_name = repo_url.split("/")[-1].split(".git")[0]

        # Clonar el repositorio
        repo_path = os.path.join(CLONE_FOLDER, repo_name)
        try:
            git.repo.clone_from(repo_url, repo_path)
            print(f"Repositorio clonado: {repo_url}")
        except Exception as e:
            print(f"Error al clonar {repo_url}: {e}")

if __name__ == "__main__":
    clone_repositories()
