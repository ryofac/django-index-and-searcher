import json

from buscador.types import Config

file_path = "buscador/config/config.json"


def get_json_config_from_file():
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def update_json_config_file(new_data):
    with open(file_path, "w") as file:
        json.dump(new_data, file, indent=4)


config: Config = get_json_config_from_file()
