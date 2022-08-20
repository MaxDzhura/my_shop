#--------------------ДЕКОРАТОРЫ----------------------

def tags(tag):
    def decorator(func):
        def wrapper(name,surname):
            return f"<{tag}>{func(name,surname)}</{tag}>"     # ЭТО ДЕКОРАТОР С ПАРАМЕТРАМИ, НА ОСНОВЕ ЗАМЫКАНИЯ

        return wrapper
    return decorator


@tags("i")
@tags("b")
@tags("p")
def get_text(name, surname):
    return f"Your name is {name}--- {surname}"

print(get_text("Maksim", "Dzhura"))


#--------------------ДЕСКРИПТОРЫ КЛАССА----------------------ЧЕРЕЗ СВОЙСТВО PROPERTY-----


class Rectangle:

    def __init__(self, a, b):

        self.a = a
        self.b = b

    @property
    def a(self):                                         # Это по сути ГЕТТЕР
        return self.__a


    @a.setter
    def a(self, value):                           # А Это по сути СЕТТЕР      (СЕТТЕРЫ И ГЕТТЕРЫ МЕТОДЫ ДОЛЖНЫ НАЗЫВАТЬСЯ КАК И ПАРАМЕТР ИЗМЕНЯЕМОГО ПАРАМЕТРА С ИНИТА)
        if not  isinstance(value, (int, float)):
            raise TypeError()
        if value < 0:
            raise ValueError()
        self.__a = value

    @a.deleter
    def a(self):
        pass


    def area(self):
        return self.__a * self.b


    def __str__(self):
        return f"{self.__a} x {self.b}"

x = Rectangle(5,10)

x.a = 10
print(x.area())
print(x)

