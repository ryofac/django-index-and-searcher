import json

from django.core.files.storage import FileSystemStorage

from buscador.types import Config

file_path = "buscador/config/config.json"

storage = FileSystemStorage()


def get_json_config_from_file():
    with storage.open(file_path, "r") as file:
        data = json.load(file)
    return data


def update_json_config_file(new_data):
    with storage.open(file_path, "w") as file:
        json.dump(new_data, file, indent=4)


def get_config() -> Config:
    return get_json_config_from_file()
