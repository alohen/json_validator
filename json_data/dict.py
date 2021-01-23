def create_json_dict_parser(schema):
    return lambda data: JsonDict(data, schema)


class JsonDict(object):
    def __init__(self, data, schema):
        self.schema = schema
        self.validate(data)
        self.data = self.parse(data)

    def validate(self, data: dict):
        for field, config in self.schema.items():
            if field not in data:
                if not config["allowEmpty"]:
                    raise ValueError("field '{}' is empty".format(field))
                return

            config["parser"](data[field])

    def parse(self, data: dict):
        parsed_data = dict()
        for key, config in self.schema.items():
            if key not in data:
                continue
            parsed_data[key] = config["parser"](data[key])

        return parsed_data

    def set(self, key: str, value):
        if key not in self.schema:
            raise KeyError("key not in schema")

        self.data[key] = self.schema[key]["config"]["parser"](value)

    def get(self, key: str):
        if key not in self.schema:
            return KeyError("key not in schema")

        if key not in self.data:
            return None

        return self.data[key]

    def get_raw(self):
        return {key: value.get_raw() for key, value in self.data.items()}

    def __eq__(self, other) -> bool:
        if self.schema != other.schema:
            return False

        for key in self.schema:
            if key in self.data and key not in other.data:
                return False

            if key not in self.data and key in other.data:
                return False

            if self.data[key] != other.data[key]:
                return False

        return True

    def __ne__(self, other):
        return not self.__eq__(other)
