#!/usr/bin/env python3

import os
import git

url = 'https://github.com/AETHER999/all_checks.py'
path = '/home/zebba/codigos/cloned_repos'

from git.exc import GitCommandError


# Lista de repositorios
repos = [

    "https://github.com/AETHER999/all_checks.py/blob/master/date_time.py",
    "https://github.com/AETHER999/all_checks.py/blob/master/free_memory.py",
    "https://github.com/AETHER999/all_checks.py/blob/master/google_guide_line.py",
    "https://github.com/AETHER999/all_checks.py/blob/master/inventory.py",
    "https://github.com/AETHER999/all_checks.py/blob/master/metronome.py",
    "https://github.com/AETHER999/all_checks.py/blob/master/planet_gravity.py",
    "https://github.com/AETHER999/all_checks.py/blob/master/practicas.py"
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
            git.Repo.clone_from(repo_url, repo_path)
            print(f"Repositorio clonado: {repo_url}")
        except Exception as e:
            print(f"Error al clonar {repo_url}: {e}")

if __name__ == "__main__":
    clone_repositories()
