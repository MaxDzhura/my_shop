class NegativeNum(Exception):
    def __init__(self, value, message):
        super().__init__()
        self.value = value
        self.message = message

    def __str__(self):
        return f"{self.value},{self.message}"



class Product:
    def __init__(self, price, name, gab):
        self.price = price
        self.name = name
        self.gab = gab

    def __str__(self):
        return f"{self.price},{self.name},{self.gab}"


class Customer:
    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone


    def __str__(self):
        return f"{self.surname}, {self.name}, {self.phone}"


class Order:
    def __init__(self, Customer):
        self.Customer = Customer
        self.cart = []
        self.quantities = []


    def addproduct(self, Product, quantities ):
        self.cart.append(Product)
        self.quantities.append(quantities)


    def totalprice(self):
        total = 0
        for i, item in enumerate(self.cart):
            total += item.price * self.quantities[i]
        return total


    def __str__(self):
        res = f"{self.Customer}\n"
        for i,item in enumerate(self.cart):
            tmp = f"{item} X {self.quantities[i]} = {self.quantities[i] * item.price}\n"
            res += tmp
        res+= f"{self.totalprice()}"
        return res





pr1 = Product(1000, "tv", "120см")
pr2 = Product(700, "phone", "12см")

cust1 = Customer("Stasikov", "Djony", "847474")
cust2 = Customer("Hitsov", "Ben", "10707446")

ord1 = Order(cust1)
ord2 = Order(cust2)

ord1.addproduct(pr1,3)
ord1.addproduct(pr2,2)

ord2.addproduct(pr2,2)
ord2.addproduct(pr1,2)


print(ord2)
