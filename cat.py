class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_eating(self):
        print(f"{self.name} is eating.")

    def done_eating(self):
        self.is_eating = False

    def outside(self):
        if self.is_eating:
            print(f"{self.name} is still eating and can't be outside!")
        else:
            print(f"{self.name}, age {self.age}, is outside.")


if __name__ == "__main__":
    cat_1 = Cat('Nimbus', 1)
    # cat_1.is_eating()
    # cat_1.outside()
    # cat_1.done_eating()
    # cat_1.outside()
    print(f"My cat's name is {cat_1.name} and is {cat_1.age} year old")
