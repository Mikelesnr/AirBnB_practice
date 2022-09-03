import json
from models.base_model import BaseModel

class FileStorage:

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        json_object = {}
        # fill dictionary with elements __objects
        for key in self.__objects:
            json_object[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w') as file_name:
            json.dump(json_object, file_name, indent=2)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF8") as file_name:
                for key, value in json.load(file_name).items():
                    attri_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attri_value
        except FileNotFoundError:
            pass

