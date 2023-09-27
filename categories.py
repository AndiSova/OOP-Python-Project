from json import JSONEncoder, JSONDecodeError, loads, dump
import category


class Encoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Categories:
    categories = []

    @classmethod
    def load_categories(cls):
        decoder = category.Decoder()

        try:
            with open("categories.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_category = decoder.decode(data)
                    if decoded_category not in cls.categories:
                        cls.categories.append(decoded_category)
        except (JSONDecodeError, FileNotFoundError):
            cls.categories = []
        return cls.categories

    @classmethod
    def remove_category(cls, name: str):
        cat = category.Category(name)
        cls.load_categories()
        if cat in cls.categories:
            cls.categories.remove(cat)
            with open("categories.txt", 'w') as f:
                for cat in cls.categories:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write("\n")

    @classmethod
    def add_category(cls, name: str):
        cat = category.Category(name)
        cls.load_categories()
        if cat not in cls.categories:
            with open("categories.txt", 'a') as f:
                e = Encoder()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write("\n")
