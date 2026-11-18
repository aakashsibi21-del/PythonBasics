# **********************************************************************
# ************************ Multiple Inheritance ************************
# **********************************************************************

class Animal:
    def eat(self):
        print('\nAnimal is Eating')

class Walks:
    def walk(self):
        print('Animal is Walking')

class Dog(Animal,Walks):
    def bark(self):
        print('Barks\n')
    # def eat(self):
    #     print('\nThe Dog is Eating')
    # def walk(self):
    #     print('The Dog is Moving\n')

dog = Dog()

dog.eat()
dog.walk()
dog.bark()


class Camera:
    def photo(self):
        print('\nTakes Photo')

class Calls:
    def calling(self):
        print('Calling firnds')

class Smart_Phone(Camera,Calls):
    def internet(self):
        print('Browsing Internet\n')

phone = Smart_Phone()

phone.photo()
phone.calling()
phone.internet()

class MediaPlayer:
    def play_vedio(self):
        print('Playing vedio')

class InternetDevice:
    def connect_wifi(self):
        print('\nConnected Wifi')

class Smart_Tv(MediaPlayer,InternetDevice):
    def change_chanel(self):
        print('Changing Tv Chanel\n')

tv = Smart_Tv()

tv.connect_wifi()
tv.play_vedio()
tv.change_chanel()

