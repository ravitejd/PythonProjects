
# This file is a configuration for Python in Visual Studio Code.

# python -m venv env --- creating a virtual environment named 'env'
# env/bin/activate --- activating the virtual environment on Windows

# pip freeze > requirements.txt --- exporting the current environment packages to requirements.txt
# pip install -r requirements.txt --- installing packages from requirements.txt

import os
import json

file_path = 'tasks.json'

if not os.path.isfile(file_path):
    with open(file_path, 'w') as f:
        json.dump([], f)
    print(f"{file_path} created.")
else:
    print(f"{file_path} already exists.")