'''System module'''
import unittest
from src.car import Car

class TestCar(unittest.TestCase):
    '''
    This essentially test the function car
    '''
    # pass
    def test_number_of_wheels(self):
        '''
        This takes in the number of wheels and check if it is the same amount
        '''
        my_car = Car('Delorean DMC-12', 100000) # create car
        self.assertEqual(my_car.wheels, 4) # test if correct


    def test_on_and_off(self):
        '''
        Takes in the current engine mode from the car and checks it,
         later it checks it again after changing it
        '''
        my_other_car = Car('Delorean DMC-12', 100000)
        self.assertEqual(my_other_car.engine, 'OFF')
        my_other_car.change_engine_mode()
        self.assertEqual(my_other_car.engine, 'ON')


    def test_damage_control(self):
        '''
        Takes in a car and damages it by two ticks,
         checks if it has two as it's damage variable
        '''
        my_third_car = Car('Delorean DMC-12', 100000)
        my_third_car.damage_car()
        my_third_car.damage_car()
        self.assertEqual(my_third_car.damage, 2)

    def test_discounting(self):
        '''
        Takes in the price of the car,
         decreases it and checks the new price
        '''
        my_forth_car = Car('Delorean DMC-12', 100000)
        my_forth_car.price_reduction()
        self.assertEqual(my_forth_car.price, 80000)

    def test_crash_evaluation(self):
        '''
        Takes in all the values and after the crashed
         method checks for new damage, engine and price
        '''
        my_fifth_car = Car('Delorean DMC-12', 100000, 0, 'ON')
        my_fifth_car.crashed()
        self.assertEqual(my_fifth_car.price, 15000)
        self.assertEqual(my_fifth_car.damage, 5)
        self.assertEqual(my_fifth_car.engine, 'OFF')
