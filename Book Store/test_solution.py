from solution import Book, Textbook, Comic
import pytest

def test_create_book():
    book1 = Book('The wind in the willows', 3, 'Kenneth Grahame', 'Children\'s Literature', 14.99)
    book2 = Book('Sword Catcher', 0, 'Cassandra Clare', 'Young Adult', 24.99)
    book3 = Book('Serpent and Dove', 2, 'Shelby Mahurin', 'Fantasy', 15.99)

    assert book1.title == 'The wind in the willows'
    assert book1.genre == 'Children\'s Literature'
    assert book1.discount == None

    assert book2.title == 'Sword Catcher'
    assert book2.author == 'Cassandra Clare'
    assert book2.discount == None

    assert book3.title == 'Serpent and Dove'
    assert book3.price == 15.99
    assert book3.discount == None

def test_set_discount_25():
    book1 = Book('The wind in the willows', 3, 'Kenneth Grahame', 'Children\'s Literature', 20.00)

    assert book1.title == 'The wind in the willows'
    assert book1.genre == 'Children\'s Literature'
    assert book1.discount == None

    book1.set_discount(.25)
    book1.get_price()

    assert book1.discount == .25
    assert book1.price == 15

    book1 = Book('The wind in the willows', 3, 'Kenneth Grahame', 'Children\'s Literature', 20.00)

    assert book1.title == 'The wind in the willows'
    assert book1.genre == 'Children\'s Literature'
    assert book1.discount == None

    book1.get_price()

    assert book1.price == 20

def test_change_to_string():
    book2 = Book('Sword Catcher', 0, 'Cassandra Clare', 'Young Adult', 24.99)

    assert book2.__str__() == 'Title: Sword Catcher, Qty: 0, Author: Cassandra Clare, Price: $24.99'

def test_purchase_book():
    book2 = Book('Sword Catcher', 0, 'Cassandra Clare', 'Young Adult', 24.99)

    with pytest.raises(ValueError):
        book2.purchase()

    book1 = Book('The wind in the willows', 3, 'Kenneth Grahame', 'Children\'s Literature', 15.00)

    assert book1.title == 'The wind in the willows'
    assert book1.quantity == 3
    assert book1.author == 'Kenneth Grahame'

    book1.purchase()

    assert book1.quantity == 2
    assert book1.price == 15.00

    book1.set_discount(.50)
    assert book1.discount == .50
    book1.get_price()

    assert book1.price == 7.50

def test_class_textbook():
     book1 = Textbook('The wind in the willows', 3, 'Kenneth Grahame', 'Children\'s Literature', 15.00, 'idk')

     assert book1.topic == 'idk'
     assert book1.title == 'The wind in the willows'

     assert str(book1) == 'Title: The wind in the willows, Qty: 3, Author; Kenneth Grahame, Price: $15.00'
