class Book:
    def __init__(self, title, quantity, author, genre, price, discount = None):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.genre = genre
        self.price = price
        self.discount = discount

    def set_discount(self, newDiscount):
        self.discount = newDiscount

    def get_price(self):
        if self.discount != None:
            self.price -= self.price*self.discount
        else:
            self.price = self.price

    def __str__(self):
        return f'Title: {self.title}, Qty: {self.quantity}, Author: {self.author}, Price: ${self.price}'

    def purchase(self):
        if self.quantity > 0:
            self.get_price()
            self.quantity -= 1
        else:
            raise ValueError
        
class Textbook(Book):
    def __init__(self, title, quantity, author, genre, price, discount, topic):
        super().__init__(title, quantity, author, genre, price, discount)
        self.topic = topic

class Comic(Book):
    def __init__(self, title, quantity, author, genre, price, discount, publisher):
        super().__init__(title, quantity, author, genre, price, discount)
        self.publisher = publisher