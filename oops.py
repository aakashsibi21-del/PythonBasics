# name1 = 'Aakash'
# age1 = 22

# name2 = 'vishnu'
# age2 = 21

# name3 = 'ajith'
# age3 = 23

# name4 = 'jerin'
# age4 = 24

# name5 = 'Dhanesh'
# age5 = 26

# print('Name : ',name1)
# print('Age  : ', age,'\n' )

# print('Name : ',name2)
# print('Age  : ',age2,'\n' )

# print('Name : ',name3)
# print('Age  : ', age3,'\n' )

# print('Name : ',name4)
# print('Age  : ', age4,'\n' )

# print('Name : ',name5)
# print('Age  : ', age5,'\n' )


# class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

std_1 = Student('Aakash', 21)
std_2 = Student('Vishnu', 22)
std_3 = Student('Batman', 25)
std_4 = Student('Superman', 31)
std_5 = Student('Spderman', 34)


print('student : ',std_1.name,'\nAge     : ',std_1.age,'\n')
print('student : ',std_2.name,'\nAge     : ',std_2.age,'\n')
print('student : ',std_3.name,'\nAge     : ',std_3.age,'\n')
print('student : ',std_4.name,'\nAge     : ',std_4.age,'\n')
print('student : ',std_5.name,'\nAge     : ',std_5.age,'\n')
print('\n***********************************************\n')

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

book1 = Book('Balarama','Vishnu',2026)
book2 = Book('kalikudukka','jerin',2023)
book3 = Book('House of Dragons','Robert Martin',2018)
book4 = Book('Harry potter','Ajith',2008)
book5 = Book('orikkal','O.V Vijayan',2014)

print('Book Name    : ',book1.name,'\nAuthor Name  : ',book1.author,'\nPublish Year : ',book1.year,'\n')
print('Book Name    : ',book2.name,'\nAuthor Name  : ',book2.author,'\nPublish Year : ',book2.year,'\n')
print('Book Name    : ',book3.name,'\nAuthor Name  : ',book3.author,'\nPublish Year : ',book3.year,'\n')
print('Book Name    : ',book4.name,'\nAuthor Name  : ',book4.author,'\nPublish Year : ',book4.year,'\n')
print('Book Name    : ',book5.name,'\nAuthor Name  : ',book5.author,'\nPublish Year : ',book5.year,'\n')
print('\n***********************************************\n')

# ***********************************************************
# ************************ Methord **************************
# ***********************************************************

class Employee:
    def __init__(self, name, emp_id, job_role, join_year):
        self.name = name
        self.emp_id = emp_id
        self.job_role = job_role
        self.join_year = join_year
    def display_details(self):
        print('Emp Name  : ',self.name,'\nEmp_Id    : ',self.emp_id,
              '\nJob Role  : ',self.job_role,'\nJoin Date : ',self.join_year,'\n')

Emp_1 = Employee('Aakash', 1001, 'HR Manager', '2014')
Emp_2 = Employee('Jerin', 4021, 'HR', '2015')
Emp_3 = Employee('Vishnu', 5451, 'Team Head', '2021')
Emp_4 = Employee('Ajith', 3451, 'Tester', '2016')
Emp_5 = Employee('BatMan', 2341, 'Developer', '2024')

Emp_1.display_details()
Emp_2.display_details()
Emp_3.display_details()
Emp_4.display_details()
Emp_5.display_details()

print('******************************************\n')

# print('Emp Name  : ',Emp_1.name,'\nEmp_Id    : ',Emp_1.emp_id,
#       '\nJob Role  : ',Emp_1.job_role,'\nJoin Date : ',Emp_1.join_date,'\n')

# print('Emp Name  : ',Emp_2.name,'\nEmp_Id    : ',Emp_2.emp_id,
#       '\nJob Role  : ',Emp_2.job_role,'\nJoin Date : ',Emp_2.join_date,'\n')

# print('Emp Name  : ',Emp_3.name,'\nEmp_Id    : ',Emp_3.emp_id,
#       '\nJob Role  : ',Emp_3.job_role,'\nJoin Date : ',Emp_3.join_date,'\n')

# print('Emp Name  : ',Emp_4.name,'\nEmp_Id    : ',Emp_4.emp_id,
#       '\nJob Role  : ',Emp_4.job_role,'\nJoin Date : ',Emp_4.join_date,'\n')

# print('Emp Name  : ',Emp_5.name,'\nEmp_Id    : ',Emp_5.emp_id,
#       '\nJob Role  : ',Emp_5.job_role,'\nJoin Date : ',Emp_5.join_date,'\n')

# ************************************************************
# ********************* Class Atribute ***********************
# ************************************************************


class Employee:
    # Class Atribute
    age = 25
    def __init__(self, name, emp_id, job_role, join_year):
        self.name = name
        self.emp_id = emp_id
        self.job_role = job_role
        self.join_year = join_year

    def display_details(self):
        print('Emp Name  : ',self.name,'\nEmp_Id    : ',self.emp_id,
              '\nJob Role  : ',self.job_role,'\nJoin Date : ',self.join_year,'\n')

Emp_1 = Employee('Aakash', 1001, 'HR Manager', '2014')
Emp_2 = Employee('Jerin', 4021, 'HR', '2015')
Emp_3 = Employee('Vishnu', 5451, 'Team Head', '2021')
Emp_4 = Employee('Ajith', 3451, 'Tester', '2016')
Emp_5 = Employee('BatMan', 2341, 'Developer', '2024')

Emp_1.display_details()
Emp_2.display_details()
Emp_3.display_details()
Emp_4.display_details()
Emp_5.display_details()

# Accessing class Atribute.
print(Employee.age)

print('******************************************\n')




class Student1:
    count = 0
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

        # Incriment count by 1, when class has initilized
        Student1.count = Student1.count + 1
    def display_count():
        print('Total Number Of Students : ',Student1.count,'\n')
    def display_student1(self):
        print('\nstudent : ',self.name,'\nAge     : ',self.age,'\nHeight : ',self.height,'\n')

std_1 = Student1('Aakash', 21, 141)
std_2 = Student1('Vishnu', 22, 134)
std_3 = Student1('Batman', 25, 123)
std_4 = Student1('Superman', 31, 167)
std_5 = Student1('Spderman', 34, 188)

Student1.display_count()

std_1.display_student1()
std_2.display_student1()
std_3.display_student1()
std_4.display_student1()
std_5.display_student1()




# print('student : ',std_1.name,'\nAge     : ',std_1.age,'\nHeight : ',std_1.height)
# print('student : ',std_2.name,'\nAge     : ',std_2.age,'\nHeight : ',std_1.height)
# print('student : ',std_3.name,'\nAge     : ',std_3.age,'\nHeight : ',std_1.height)
# print('student : ',std_4.name,'\nAge     : ',std_4.age,'\nHeight : ',std_1.height)
# print('student : ',std_5.name,'\nAge     : ',std_5.age,'\nHeight : ',std_1.height)
# print('\n***********************************************\n')


# *******************************************************
# ***************** Inheritance *************************
# *******************************************************

print('******************* Inheritance *************************')

# class Animal:
#     def __init__(self, eat, sleep):
#         self.eat = eat
#         self.sleep = sleep

# class Dog(Animal):
#     def __init__(self, eat, sleep):
#         super().__init__(eat, sleep)
#         self.speak = 'Bow'



# class Cat(Animal):
#     def __init__(self, eat, sleep):
#         super().__init__(eat, sleep)
#         self.speak = 'Meow'


# dog = Dog(eat ='eat', sleep= 'sleep')
# cat = Cat(eat='eat',sleep='sleep')

# print(dog.speak,dog.eat,dog.sleep)
# print(cat.speak,cat.eat,cat.sleep)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('The Animal is Eating ')

class Dog(Animal):
    def bark(self):
        print('Dog Speak Woof Woof')
        # self.speak = 'Bow Bow'
        
    def display_Dog(self):
        print('\nThe Animal Name  is : ',self.name,'\nItsAge  is : ',self.age)

#use superkey() only when the child class need their own attribute or valuse to store or display

class Cat(Animal):
    # def __init__(self, name, age):
    #     super().__init__(name, age)  

    def Meow(self):
        print('Cat Speak Meow Meow\n')
        # self.speak = 'Meow Meow'
    def Display_Cat(self):
        print('\nThe Animal Name  is : ',self.name,'\nIts Age  is : ',self.age,)
        # self.eat()
        # self.Meow()
        # print('\nName  : ',self.name,'\nAge   : ',self.age,'\nSpeak : ',self.speak,'\n')


dog = Dog(name ='Dog', age= 7)
cat = Cat(name='Cat', age= 4)


def display_all():
   dog.display_Dog()
   dog.eat()
   dog.bark()
   cat.Display_Cat()
   cat.eat()
   cat.Meow()
   print("\n*****************************************\n")

display_all()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print('Name   : ', self.name, '\nAge    : ', self.age)
class Student2(Person):
    def __init__(self, name, age):
        super().__init__(name, age )
        self.course = 'Python'
    def show_course(self):
        print('Course : ',self.course,'\n')

pers = Student2(name = 'Aakash', age = 22)

pers.display()
pers.show_course()
print('\n\n')


# *******************************************************************
# ************************* Abstraction *****************************
# *******************************************************************

from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposite(self):
        pass

    @abstractmethod
    def loan(self):
        pass

class SBI(Bank):
    def deposite(self):
        print('Deposite is excluded')

    def loan(self):
        print('Loan is applied')

    def profit(self):
        print('Profit')

sbi = SBI()
sbi.deposite()
sbi.loan()
sbi.profit()
print('\n*****************************************\n')


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.length * self.width
        print(rectangle_area)


class Circle(Shape):
    def __init__(self,radius):
        self.radious = radius

    def area(self):
        circle_radius = 3.14 * self.radious * self.radious
        print(circle_radius)

rec = Rectangle(23,12)
cir = Circle(23)

rec.area()
cir.area()

        

