class Library():
    def __init__(self, title, author, genre, checked_out=False, is_overdue=False):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out
        self.is_overdue = is_overdue
        

    def create_book(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def check_out(self, book):
        if book in self.books:
              self.checked_out = True
        elif book.checked_out == True:
            raise ValueError
        else:
            raise ValueError
        
    def check_in(self, title):
        if title in self.books:
             self.checked_out = False
        

class Book(Library):
        def __init__(self, overdue_fee = None):
             self.overdue_fee = overdue_fee