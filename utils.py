import json


def create_file_parser(parser):
    return lambda file_path: JsonFile(file_path, parser)


class JsonFile(object):
    def __init__(self, file_path, parser):
        self.file_path = file_path
        self.parser = parser

    def load(self):
        if self.data:
            raise Exception("file already loaded")
        self.__load()

    def write(self):
        if not self.data:
            raise Exception("file not loaded")

        self.__write()

    def create(self):
        self.__write()

    def reload(self):
        self.__load()

    def __write(self):
        with open(self.file_path, "w") as json_file:
            json_file.write(json.dumps(self.data.get_raw()))

    def __load(self):
        with open(self.file_path, "r") as json_file:
            file_text = json_file.read()

        json_data = json.loads(file_text)
        self.data = self.parser(json_data)
