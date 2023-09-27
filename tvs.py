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
        tv = TVs(*vals)
        return tv


class TVs(Product):
    tvs = []

    @classmethod
    def remove_tv(cls, tv):
        cls.load_tvs()
        if tv in cls.tvs:
            cls.tvs.remove(tv)
            with open("tvs.txt", "w") as f:
                for tv in cls.tvs:
                    e = Encoder()
                    encoded_tv = e.encode(tv)
                    dump(encoded_tv, f)
                    f.write("\n")

    @classmethod
    def add_tv(cls, tvs) -> None:
        if type(tvs) != TVs:
            return None
        if tvs not in cls.tvs:
            with open("tvs.txt", "a") as f:
                e = Encoder()
                encoded_tv = e.encode(tvs)
                dump(encoded_tv, f)
                f.write("\n")

    @classmethod
    def load_tvs(cls) -> list:
        decoder = Decoder()
        try:
            cls.tvs = []
            with open("tvs.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_tv = decoder.decode(data, )
                    cls.tvs.append(decode_tv)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.tvs = []
        return cls.tvs

    def __init__(self, name: str, producer: int, cpu: int, year: int):
        Product.__init__(self, name)
        self.producer = producer
        self.cpu = cpu
        self.year = year

    def __str__(self):
        return f'{type(self).__name__}: {self.name} {self.producer} {self.cpu} {self.year}'

    def __eq__(self, obj):
        if type(self) == type(obj):
            return self.name == obj.name and self.producer == obj.producer and self.cpu == obj.cpu and self.year == obj.year
        return False
