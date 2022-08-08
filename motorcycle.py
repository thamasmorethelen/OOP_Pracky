class Motorcycle:

    def __init__(self, make, model, year):
        self.make = make
        self. model = model
        self.year = year
        self.odometer = 0

    def descriptive_name(self):
        desc_name = f'{self.make} {self.model} {self.year}'
        return desc_name.title()

    def read_odometer(self):
        return f"This motorcycle has {self.odometer} miles on it."

    def update_omometer(self, miles):
        self.odometer = miles


if __name__ == "__main__":
    moto_1 = Motorcycle('hond', 'CB750', 1977)
    print(moto_1.descriptive_name())
