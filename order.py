from json import JSONEncoder, JSONDecoder, JSONDecodeError, dump, loads

from videogames import VideoGames
from desktops import Desktops
from consoles import Consoles
from tvs import TVs


class Encoder(JSONEncoder):
    @staticmethod
    def custom(category: VideoGames | Desktops | Consoles | TVs, customer: str, address: str, _id: str):
        category.__dict__['category'] = type(category).__name__
        category.__dict__['customer'] = customer
        category.__dict__['address'] = address
        category.__dict__['id'] = _id
        return category.__dict__


class Decoder(JSONDecoder):
    def decode(self, obj: dict, **kwargs) -> VideoGames | Desktops | Consoles | TVs:
        data = obj
        values = []
        for i in data.keys():
            if i != 'category' and i != 'customer' and i != 'address' and i != 'id':
                values.append(data[i])
        cat = eval(f'{data["category"]}{*values,}')
        return cat

    @staticmethod
    def custom_decode(obj: dict) -> list:
        data = obj
        vals = []
        for key in data.keys():
            vals.append(data[key])
        return vals


class Order:
    def __init__(self, customer: str, address: str, products: list = None, _id: str = None) -> None:
        if products is None:
            products = []
        self.products = products
        self.customer = customer
        self.address = address

    @classmethod
    def load_order(cls, file: str):
        decoder = Decoder()
        products = []
        try:
            with open(f'orders/{file}', 'r') as f:
                for line in f:
                    data = loads(line)
                    decoded_order = decoder.custom_decode(data)
                    products.append(decoder.decode(data, ))
                return Order(decoded_order[5], decoded_order[6], products, decoded_order[-1])
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.categories = []
            print(e)

    def __eq__(self, other) -> bool:
        return self.customer == other.customer and self.address == other.address

    def __str__(self) -> str:
        string = f'\n\nCustomer name: {self.customer}\nCustomer address: {self.address}'
        self.load_products_from_order()
        for product in self.products:
            string += f"\n{product}\n"
        return string + "\n\t"

    def add_product_to_order(self, product: VideoGames | Desktops | Consoles | TVs) -> None:
        self.products.append(product)
        VideoGames.remove_videogame(product)
        Desktops.remove_desktop(product)
        Consoles.remove_console(product)
        TVs.remove_tv(product)

        with open(f'orders/order{self}', 'a') as f:
            e = Encoder()
            dump(e.custom(product, self.customer, self.address), f)
            f.write('\n')

    def load_products_from_order(self) -> list:
        decoder = Decoder()
        self.products = []
        try:
            with open(f'orders/order{self}') as f:
                for line in f:
                    data = loads(line)
                    decoded_data = decoder.decode(data, )
                    self.products.append(decoded_data)
            return self.products

        except (JSONDecodeError, FileNotFoundError) as e:
            print(e)
