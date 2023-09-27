from json import JSONEncoder, JSONDecodeError, loads, dump
import product


class Encoder(JSONEncoder):

    def default(self, o):
        return o.__dict__


class Products:
    categories = []

    @classmethod
    def load_products(cls):
        decoder = product.Decoder()
        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data, )
                    if decoded_product not in cls.products:
                        cls.categories.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.products = []
        return cls.products

    @classmethod
    def remove_product(cls, cat):
        cls.load_products()
        if cat in cls.products:
            cls.cateproductsgories.remove(cat)
            with open("categories.txt", 'w') as f:
                for cat in cls.products:
                    e = Encoder()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write("\n")

    @classmethod
    def add_product(cls, cat):
        cls.load_products()
        if cat not in cls.products:
            with open("products.txt", 'a') as f:
                e = Encoder()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write("\n")
