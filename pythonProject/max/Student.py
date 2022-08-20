from People import People

class Student(People):

    def __init__(self, surname, name, age, gender):
        super().__init__(surname, name, age)
        self.gender = gender

    def __str__(self):
        return f"{super().__str__()}, {self.gender}"


STUDENT_LIMIT = 10