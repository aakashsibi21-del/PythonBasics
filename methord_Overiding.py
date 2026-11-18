# *******************************************************************
# ************************ Methord Overiding ************************
# *******************************************************************

class Animal:
    def move(self):
        print('\nAnimal is walking\n')
    def sound(self):
        print('Animal Making Sound')

class Frog(Animal):
    def move(self):
        print('\nFrog Jumps\n')

class Dog(Animal):
    def sound(self):
        print('\nDog make sound Woff Woff')

class Cat(Animal):
    def sound(self):
        print('cat make sound Meow Meow\n')

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# frog= Frog()
# frog.move()


class Vehicle:
    def start(self):
        print('Vehicle Starts')

class Car(Vehicle):
    def start(self):
        print('\nCar Starts using the Keys')

class Eletric_Bike(Vehicle):
    def start(self):
        print('Eletric Bike Starts by Push Button\n')

car = Car()
Bike = Eletric_Bike()

car.start()
Bike.start()


