import os
import sys
from importlib import import_module
from django.db import models


def get_all_snippets(directory):
    snippets_to_register = []
    current_directory = directory
    for filename in os.listdir(os.path.join(current_directory, "snippets")):
        if filename.endswith(".py") and not filename.startswith("__"):
            # Извлеките имя модуля без расширения .py
            module_name = "home.snippets." + filename[:-3]
            try:
                # Импортируйте модуль
                module = import_module(module_name)
                # Найдите классы сниппетов в модуле и добавьте их в список
                for name, obj in vars(module).items():
                    if isinstance(obj, type) and issubclass(obj, models.Model):
                        snippets_to_register.append(obj)
            except Exception as e:
                sys.stderr.write(f"Failed to import {module_name}: {e}\n")
    return snippets_to_register
