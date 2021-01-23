def create_json_list_parser(parser):
    return lambda data: JsonList(data, parser)


class JsonList(object):
    def __init__(self, data, node_parser):
        self.validate(data, node_parser)
        self.data = self.parse(data, node_parser)
        self.node_parser = node_parser

    @staticmethod
    def validate(data, nodes_type):
        if type(data) is not list:
            raise Exception("given value is not list")

        [nodes_type(node) for node in data]

    @staticmethod
    def parse(data, nodes_type):
        return [nodes_type(node) for node in data]

    def get_all(self):
        return [self.node_parser(node) for node in self.data]

    def get_by_index(self, index: int):
        if len(self.data) <= index:
            raise Exception("index out of bounds")
        return self.node_parser(self.data[index])

    def append(self, node_data):
        parsed_data = self.node_parser(node_data)
        self.data.append(parsed_data)
