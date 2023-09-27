from ast import Str
from json import JSONEncoder, JSONDecoder, loads


class Encoder(JSONEncoder):
    def default(self, o: str) -> str:
        return o.__dict__


class Decoder(JSONDecoder):
    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        cat = Category(*vals)
        return cat


class Category:
    def __init__(self, name: Str) -> object:
        self.name = name

    def __eq__(self, other) -> bool:
        if type(other) == type(self):
            return self.name == other.name
        else:
            return False

    def __hash__(self):
        return hash(self.name)
