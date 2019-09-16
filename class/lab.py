#!/usr/bin/env python3

class Animal(object):
    owner = 'jack'

    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def make_sound(self):
        pass

    @classmethod
    def get_owner(cls):
        return cls.owner
    
    @classmethod
    def set_owner(cls,name):
        cls.owner = name


    @staticmethod
    def order_animal_food():
        print('ording...')
        print('ok')

class Dog(Animal):
    def make_sound(self):
        print(self.get_name()+'is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name()+'is making sound miu miu miu...')


if __name__ == '__main__':
    Animal.order_animal_food()
    




