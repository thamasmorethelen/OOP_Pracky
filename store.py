class Store:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def discribe_store(self):
        print(f"{self.name} is a {self.type} that strives to serve its costumer base with the utmost professionalism.")

    def store_open(self):
        print(f"{self.name} is open!")


if __name__ == "__main__":
    store = Store("Safeway", "Grocery")
    store.discribe_store()
    store.store_open()
    store_1 = Store("Tacos Galore!", "Food Truck")
