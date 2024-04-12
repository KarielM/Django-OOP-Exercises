from solution import Uber, Van, Car, XL
import pytest

def test_creating_uber_1():
    ride1 = Uber(5, False)

    assert ride1.distance == 5
    assert ride1.is_hot == False

def test_creating_uber_2():
    ride1 = Uber(7, True)

    assert ride1.distance == 7
    assert ride1.is_hot == True

def test_uber_fare_method_1():
    ride1 = Uber(7, True)

    assert ride1.fare(5, 5) == 14

def test_uber_fare_method_2():
    ride1 = Uber(9, True)

    assert ride1.fare(9, 9) == 18

def test_uber_fare_method_3():
    ride1 = Uber(7, False)

    assert ride1.fare(9, 9) == 7

def test_uber_capacity_check_1():
    ride1 = Uber(2, True)

    with pytest.raises(ValueError):
        ride1.capacity_check(4,5)

def test_uber_capacity_check_2():
    ride1 = Uber(2, True)

    assert ride1.capacity_check(4, 2) == True

def test_class_xl():
    ride1 = XL(2, True)

    assert ride1.capacity == 6

def test_class_van():
    ride1 = Van(2, True)

    assert ride1.capacity == 8

def test_class_car():
    ride1 = Car(2, True)

    assert ride1.capacity == 4

def test_uber_method_with_xl_1():
    ride1 = XL(2, True)

    assert ride1.capacity_check(ride1.capacity, 5) == True

def test_uber_method_with_xl_2():
    ride1 = XL(2, True)

    with pytest.raises(ValueError):
        ride1.capacity_check(ride1.capacity, 7)

def test_uber_method_with_van_1():
    ride1 = Van(2, True)

    assert ride1.capacity_check(ride1.capacity, 7) == True

def test_uber_method_with_van_2():
    ride1 = Van(2, True)

    with pytest.raises(ValueError):
        ride1.capacity_check(ride1.capacity, 9)

def test_car_method_with_car_1():
    ride1 = Car(2, True)

    assert ride1.capacity_check(ride1.capacity, 3) == True

def test_car_method_with_car_2():
    ride1 = Car(2, True)

    with pytest.raises(ValueError):
        ride1.capacity_check(ride1.capacity, 9)

def test_xl_fare():
    ride1 = XL(7, False)

    assert ride1.fare(6, 2) == 21


def test_van_fare():
    ride1 = Van(7, True)

    assert ride1.fare(6, 3) == 28

def test_car_fare():
    ride1 = Car(2, True)

    assert ride1.fare(2, 4) == 2

