## Virtual environments in Python let you keep packages separate for each project. This avoids conflicts (e.g., one project needs requests 2.25, another needs 2.31).
A virtual environment is a folder with its own Python interpreter and its own site-packages (installed libraries).

## WHY USE?
Different projects can use different package versions
No pollution of your system/global Python
Easy to delete/recreate
Reproducible: share requirements.txt or pyproject.toml
Safer: pip install won't break other projects

## Main ways 
# 1. venv — built-in (recommended for most beginners)
- Create:
python -m venv myenv          

- Activate (Windows):
myenv\Scripts\activate

- Activate (macOS/Linux):
source myenv/bin/activate

- Now pip install goes only into this env:
pip install requests numpy

- Deactivate:
deactivate

- Save packages:
pip freeze > requirements.txt

- Install from file:
pip install -r requirements.txt

# 2. virtualenv— third-party, very similar to venv but sometimes faster/more features
- Install once globally:
pip install virtualenv

- Create:
virtualenv myenv
(rest same as venv)

# 3. Poetry— modern all-in-one (popular in 2025)
Install once:
pip install poetry

- In project folder:
poetry new myproject          # or cd into existing folder
poetry init                   # interactive setup

- Add packages:
poetry add requests pandas
 ## Poetry auto-creates virtual env + pyproject.toml + poetry.lock (same versions)

- Run commands inside env:
poetry run python script.py
poetry shell                 
 ## advantages: clean lockfile, no manual venv management, better dependency resolution

# 4. pipenv— another all-in-one (Pipfile + lock)
 ## Creates Pipfile & Pipfile.lock
 ## Still used, but Poetry is more active/favored in recent years.

- Install:
pip install pipenv

- In project:
pipenv install requests
pipenv shell


### cheat-sheet (venv style)
# create
python -m venv .venv
# activate
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows
# install
pip install flask
# list
pip list
# exit
deactivate
