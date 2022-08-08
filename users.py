class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'The users first name is {self.first_name} and their last name is {self.last_name}')

    def greet_user(self):
        print(f'Greetings {self.first_name}!')


if __name__ == "__main__":
    user_1 = User('Nimbus', 'Nephele')
    user_2 = User('Kitty', 'Cat')
    user_3 = User('Asajj', "Ventress")
    user_4 = User('Obi-Wan', 'Kenobi')
    user_5 = User('Dr.', 'Seuss')
