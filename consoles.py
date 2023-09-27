from json import JSONEncoder, JSONDecoder, JSONDecodeError, dump, loads
from product import Product


class Encoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Decoder(JSONDecoder):

    def decode(self, obj, **kwargs):
        data = loads(obj)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        console = Consoles(*vals)
        return console


class Consoles(Product):
    consoles = []

    @classmethod
    def remove_console(cls, console) -> None:
        cls.load_consoles()
        if console in cls.consoles:
            cls.consoles.remove(console)
            with open("consoles.txt", "w") as f:
                for console in cls.consoles:
                    e = Encoder()
                    encoded_console = e.encode(console)
                    dump(encoded_console, f)
                    f.write("\n")

    @classmethod
    def add_console(cls, console) -> None:
        if type(console) != Consoles:
            return None

        if console not in cls.consoles:
            with open("consoles.txt", "a") as f:
                e = Encoder()
                encoded_console = e.encode(console)
                dump(encoded_console, f)
                f.write("\n")

    @classmethod
    def load_consoles(cls) -> list:
        decoder = Decoder()

        try:
            cls.consoles = []
            with open("consoles.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_console = decoder.decode(data, )
                    cls.consoles.append(decode_console)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.consoles = []
        return cls.consoles

    def __init__(self, name: str, producer: str, releasedate: int, price: int):
        Product.__init__(self, name)
        self.producer = producer
        self.releasedate = releasedate
        self.price = price

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.name} {self.producer} {self.releasedate} {self.price}'

    def __eq__(self, obj) -> bool:
        if type(self) == type(obj):
            return self.name == obj.name and self.producer == obj.producer and self.releasedate == obj.releasedate and self.price == obj.price
        return False
