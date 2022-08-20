
class Grouplimit(Exception):
    def __init__(self, value, message):
        super().__init__()
        self.value = value
        self.message = message

    def __str__(self):
        return f"{self.value},{self.message}"


class People:

    def __init__(self, surname, name, age):
        self.surname = surname.strip().title()
        self.name = name.strip().title()
        self.age = age

    def __str__(self):
        return f"{self.surname}--{self.name}--{self.age}"