def create_json_string_parser(validator):
    return lambda data: JsonString(data, validator)


class JsonString(object):
    def __init__(self, data, validator):
        self.validator = validator
        self.data = {}
        self.set(data)

    def validate(self, data):
        self.validator(data)

    def set(self, data):
        self.validate(data)
        self.data = data

    def get(self):
        return self.get_raw()

    def get_raw(self):
        return self.data

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return not self.__eq__(other)
