print('Hello World')
print('''Aakash
puliyanmackal
thodupuzha''') 
# Different type o f data types
print(2026) # Initegr
print('2026') # String
print("2026") #String
# print ('2026") this code was wrong because of the uot

print(type(2026)) # int
print(type(2026.0)) # float
print(type('2026')) # string
print(type("2026")) # string

#Datatype of 2026 is < class int >

print('Datatyoe of 2026 is ', type(2026))
print('Datatyoe of 2026.0 is ', type(2026.0))
print("Datatyoe of '2026' is ", type('2026'))
print("Datatyoe of 'aakash' is ", type('aakash'))
print('Datatyoe of "2026" is ', type("2026"))

print('Datatyoe of True is ', type(True)) # bool
print('Datatyoe of "True" is ', type("True")) # string
print('*******************************************')
# print('Datatyoe of True is ', type(TRUE)) # Always start with the Capital Letter
# print('Datatyoe of true is ', type(true))

# *************************************
# ************Varibles*****************
# *************************************

my_name = "aakash"
place_of_birth = "thodupuzha"
age = 22
mobile_no = 8075906437
email = "aakashsibi807@gmail.com"
hight = "190 cm"
weight = "80 kg"
education = "bca"

print(mobile_no)
print('datatype of "mobile_no" is',type("mobile_no")) # datatpe of mobile_no

fred = 200
jhon = fred
print(jhon)

fred = 3
jhon = fred
print(jhon)

# get datatype of  varibles
print('datatype of ' ,my_name , 'is',type(my_name))
print('datatype of ',place_of_birth,'is',type(place_of_birth))
print('datatype of',age,'is',type(age))
print('datatype of',mobile_no,'is',type(mobile_no))
print('datatype of', email,'is',type(email))
print('datatype of',hight,'is',type(hight))
print('datatyoe of',weight,'is',type(weight))
print('****************************************')
# *************************************************
# ****************Data Type Coversion**************
# *************************************************

num1 = 1900
num2= 67.8

print('Datatype of',num1,'is',type(num1))
print('Datatype of',num2,'is',type(num2))

num3 = int(num2)    # converting float into int
num4 = float(num1)  # converting int into float

print('Datatype of',num3,'is',type(num3))
print('Datatype of',num4,'is',type(num4))
print('*******************************************')