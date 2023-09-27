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
        videogame = VideoGames(*vals)
        return videogame


class VideoGames(Product):
    videogames = []

    @classmethod
    def remove_videogame(cls, videogame) -> None:
        cls.load_videogames()
        if videogame in cls.videogames:
            cls.videogames.remove(videogame)
            with open("video_games.txt", "w") as f:
                for videogame in cls.videogames:
                    e = Encoder()
                    encoded_videogame = e.encode(videogame)
                    dump(encoded_videogame, f)
                    f.write("\n")

    @classmethod
    def add_videogame(cls, videogame):
        if type(videogame) != VideoGames:
            return None
        if videogame not in cls.videogames:
            with open("video_games.txt", "a") as f:
                e = Encoder()
                encoded_videogame = e.encode(videogame)
                dump(encoded_videogame, f)
                f.write("\n")

    @classmethod
    def load_videogames(cls) -> list:
        decoder = Decoder()
        try:
            cls.videogames = []
            with open("video_games.txt") as f:
                for line in f:
                    data = loads(line)
                    decode_videogame = decoder.decode(data, )
                    cls.videogames.append(decode_videogame)
        except (JSONDecodeError, FileNotFoundError):
            cls.videogames = []
        return cls.videogames

    def __init__(self, name: str, release_date: int, genre: str, price: int):
        Product.__init__(self, name)
        self.release_date = release_date
        self.genre = genre
        self.price = price

    def __str__(self) -> str:
        return f'{type(self).__name__}: {self.name} {self.release_date} {self.genre}'

    def __eq__(self, obj) -> bool:
        if type(self) == type(obj):
            return self.name == obj.name and self.release_date == obj.release_date and self.genre == obj.genre
        return False
