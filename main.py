from order import Order
from categories import Categories
from videogames import VideoGames
from desktops import Desktops
from consoles import Consoles
from tvs import TVs
from json import loads
import os


def app():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_all_products():
    display_products()
    app()
    get_products()


def generate_choices() -> dict:
    categories = Categories.load_categories()
    choices = {}
    for index, category in enumerate(categories):
        print(f'{index + 1}. {category.name}')
        choices[index + 1] = category.name
    return choices


def set_categories():
    def add_category():
        category = input("Insert a new category:\n\t")
        Categories.add_category(category)
        app()
        set_categories()

    def remove_category():
        category = input(
            "Insert a category you want to remove:\n\t")
        Categories.remove_category(category)
        app()
        set_categories()

    def display_categories():
        categories = Categories.load_categories()
        if categories:
            for category in categories:
                print(category.name)
        else:
            print("No categories found")
        app()
        set_categories()

    print('\n1. Add a category\n2. Remove a category\n3. Display all the categories called\n4. Back to the main menu\n')
    option = int(input("Enter an option: "))
    actions = {1: add_category, 2: remove_category,
               3: display_categories, 4: menu}
    action = actions.get(option, error_handler)
    action()


def add_new_product(category: str) -> VideoGames | Desktops | TVs | Consoles:
    if category == "Video_Games":
        name = input("Name: ")
        release_date = int(input("Release Date: "))
        genre = input("Genre: ")
        price = int(input("Price: "))
        return VideoGames(name, release_date, genre, price)

    elif category == "Desktops":
        name = input("Name: ")
        producer = input("Producer: ")
        cpu = input("CPU type: ")
        year = int(input("year: "))
        return Desktops(name, producer, cpu, year)

    elif category == "TVs":
        name = input("Name: ")
        producer = input("Producer: ")
        type = input("LED/LCD/other: ")
        size = int(input("Size(in cm): "))
        return TVs(name, producer, type, size)

    elif category == "Consoles":
        name = input("Name: ")
        producer = int(input("Producer: "))
        releasedate = int(input("Release Date: "))
        price = int(input("Price: "))
        return Consoles(name, producer, releasedate, price)


def display_products():
    categories = Categories.load_categories()
    for category in categories:
        with open(f"{category.name.lower()}.txt", "r") as file:
            print(
                f"You have the following products {category.name} :")
            for i, line in enumerate(file):
                data = loads(line)
                print(f"%d. %s" % (i, data))
        print("\n\n")


def to_orders():
    def place_order():
        name = input("Full Name: ")
        address = input("Address: ")
        new_order = Order(name, address)
        print("\nAvailable products:\n")
        display_products()
        options = generate_choices()
        choice = int(input("Choose a category: "))
        product = add_new_product(options.get(choice, error_handler))
        if product in VideoGames.load_videogames():
            new_order.add_product_to_order(product)
        elif product in Desktops.load_desktops():
            new_order.add_product_to_order(product)
        elif product in Consoles.load_consoles():
            new_order.add_product_to_order(product)
        elif product in TVs.load_tvs():
            new_order.add_product_to_order(product)
        else:
            print("Product not available.")
        print("\nCurrent order:\n")
        new_order.load_products_from_order()
        for product in new_order.products:
            print(product)
        app()
        to_orders()

    def display_orders():
        files = [f for f in os.listdir('orders')]
        if not files:
            print("You have no orders")
            app()
            to_orders()
        print("You have the following orders:")
        for file in files:
            n_order = Order.load_order(file)
            print(n_order, '\n')
        app()
        to_orders()

    print("\n1. Place a new order\n2. Display all orders\n3. Back to the main menu\n")
    option = int(input("Enter an option: "))

    actions = {1: place_order, 2: display_orders,
               3: menu}

    action = actions.get(option, error_handler)
    action()


def get_products():
    def add_product():
        choices = generate_choices()
        category = int(input("Enter the category of your product: "))
        obj = add_new_product(choices.get(category, error_handler))
        VideoGames.add_videogame(obj)
        Desktops.add_desktops(obj)
        TVs.add_tv(obj)
        Consoles.add_console(obj)
        print("New product added")
        app()
        get_products()

    def remove_product():
        options_menu = generate_choices()
        category = int(input("Enter the category of your product: "))
        if category == 1:
            with open('video_games.txt', "r") as file:
                print("The following products are in this category:")
                for i, line in enumerate(file):
                    data = loads(line)
                    print(f"%d. %s" % (i, data))
        elif category == 2:
            with open('desktops.txt', "r") as file:
                print("The following products are in this category:")
                for i, line in enumerate(file):
                    data = loads(line)
                    print(f"%d. %s" % (i, data))
        elif category == 3:
            with open('tvs.txt', "r") as file:
                print("The following products are in this category:")
                for i, line in enumerate(file):
                    data = loads(line)
                    print(f"%d. %s" % (i, data))
        elif category == 4:
            with open('consoles.txt', "r") as file:
                print("The following products are in this category:")
                for i, line in enumerate(file):
                    data = loads(line)
                    print(f"%d. %s" % (i, data))
        obj = add_new_product(options_menu.get(category, error_handler))
        print(obj)
        VideoGames.remove_videogame(obj)
        Desktops.remove_desktop(obj)
        TVs.remove_tv(obj)
        Consoles.remove_console(obj)
        print("Product removed")
        app()
        get_products()

    print("\n1. Add a product\n2. Remove a product\n3. Display all the products\n4. Back to the main menu\n")
    option = int(input("Enter an option: "))

    actions = {1: add_product, 2: remove_product,
               3: display_all_products, 4: menu}

    action = actions.get(option, error_handler)
    action()


def error_handler():
    print("Action not permitted")
    app()
    menu()


def close_application():
    print("Application closes")


def menu():
    print("\n1. Categories\n2. Products\n3. Orders\n4. Exit\n")
    option = int(input("Enter an option: "))

    actions = {1: set_categories, 2: get_products,
               3: to_orders, 4: close_application}

    action = actions.get(option, error_handler)
    action()


if __name__ == "__main__":
    menu()
