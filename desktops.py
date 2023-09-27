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
        desktop = Desktops(*vals)
        return desktop


class Desktops(Product):
    desktops = []

    @classmethod
    def remove_desktop(cls, desktop) -> None:
        cls.load_desktops()
        if desktop in cls.desktops:
            cls.desktops.remove(desktop)
            with open("desktops.txt", "w") as f:
                for desktop in cls.desktops:
                    e = Encoder()
                    encoded_desktop = e.encode(desktop)
                    dump(encoded_desktop, f)
                    f.write("\n")

    @classmethod
    def add_desktops(cls, desktop) -> None:
        if type(desktop) != Desktops:
            return None

        if desktop not in cls.desktops:
            with open("desktops.txt", "a") as f:
                e = Encoder()
                encoded_desktop  = e.encode(desktop)
                dump(encoded_desktop , f)
                f.write("\n")

    @classmethod
    def load_desktops(cls) -> list:
        decoder = Decoder()

        try:
            cls.desktops = []
            with open("desktops.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_desktop  = decoder.decode(data, )
                    cls.desktops.append(decode_desktop )
        except (JSONDecodeError, FileNotFoundError):
            cls.desktops = []
        return cls.desktops

    def __init__(self, name: str, producer: str, cpu: int, year: int):
        Product.__init__(self, name)
        self.producer = producer
        self.cpu = cpu
        self.year = year

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.name} {self.producer} {self.cpu} {self.year}'

    def __eq__(self, obj) -> bool:
        if type(self) == type(obj):
            return self.name == obj.name and self.producer == obj.producer and self.cpu == obj.cpu and self.year == obj.year
        return False
