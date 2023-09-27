from json import JSONEncoder


class Encoder(JSONEncoder):

    def default(self, o: object) -> object:
        return o.__dict__


class Product:
    products = []

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'

    def __hash__(self) -> hash:
        return hash(self.name)
