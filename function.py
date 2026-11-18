# *******************************************
# ****************Function*******************
# *******************************************


def display_sum(num1, num2):
    sum = num1 + num2
    print("the sum of" ,num1, 'and' ,num2,  "is ",sum)

# anfunction will have
# 1. function name : mandatory
# 2. input(s)
# 3. Body of a function(wheather function actually does)
# 4. put
# while we define input varibles in the function definiction, we are 
# creating a new varible with scope within the function


# call the function // invocting the function.
# display_sum(10,11)
# display_sum(2026,8)
# display_sum(6.8,4.6)
# display_sum('happy',' diwali')
def display_custom():
    print('we will display the sum of the  numbers you enter')
    num1 = float(input('Enter a Number : '))
    num2 = float(input('Enter a Number : '))
    sum = num1 + num2
    print("the sum of" ,num1, 'and' ,num2,  "is ",sum)
# display_custom()

def display_custom():
    print('we will display the sum of the  numbers you enter')
    num1 = float(input('Enter a Number : '))
    num2 = float(input('Enter a Number : '))
    display_sum(num1,num2)
# display_custom()

def Greeting():
    name = input(' Enter Your Name : ')
    a = 'Hi, '
    b = ' Good after noon. '
    c = ' how are you?'
    greet = a + name + b + c
    print(greet)
# Greeting()

def Greeting():
    name = input('Enter Your Name : ')
    print('Hi ',name, '\nGood Morning. How are You?')
# Greeting()


# num = int(input('Enter a number : '))
# print('Multiplication Table of ', num)
# for i in range(1,11):
#     print(i,'x' ,num, '=',(i*num))
# print('\n*******************************\n')


# *******************************************************
# Function to display multiplication table of any number.
# *******************************************************

def display_multiplication_table():
    print('We will display the multiplication table of the number you enter ')
    num = int(input('Enter a number : '))
    print('Multiplication Table of ', num)
    for i in range(1,11):
        # print(i,'x' ,num, '=',(i*num))
        print(f"{i} x {num} = {i*num}")
    print('\n*******************************\n')

# display_multiplication_table()          # Invoke the function(Calling the function)


# eng = int(input('Enter the score'))
# maths = int(input('Enter the score'))
# physics = int(input('Enter the score'))
# cpp = int(input('Enter the score'))
# java = int(input('Enter the score'))

scores = (55,65,33,95,85)

def sum_of_score():
   sum1  = 0
   for i in range(len(scores)):
         sum1+= scores[i]
   print('sum of scores',sum1)
   return sum1
# sum_of_score()

def average_Scores():
    sum1 = sum_of_score()
    count1 = len(scores)
    avg = sum1/count1
    print('Average = ',avg)
    return avg
# average_Scores()


def largest():
    latgest_score = max(scores)
    print('Largest Score = ', latgest_score)
    return latgest_score

def Smallest():
    Smallest_Score = min(scores)
    print('Smallest_Score = ',Smallest_Score)
    return Smallest_Score

def Student_perfomance():
    sum_of_score()
    average_Scores()
    largest()
    Smallest()
# Student_perfomance()


# ****************************************************
# *************Operational Arguments******************
# ****************************************************

# def calculate_exponent(num,exp = 2):
#     print(num**exp)
# calculate_exponent(5)
# calculate_exponent(5,3)

# def create_wish(name, wish = 'good day'):
#     print(f'Hi{name},{wish}')
# create_wish('Vishnu')
# create_wish(' vishnu', 'Happy birthday')


# ***********************************************************
# ***********************************************************
# ***********************************************************

# def divide(num,den):
#     result = num/den
#     print(f'the answer is {result}')

# divide(23,2)
# divide(5565,56)
# # RuntimeError
# # divide('A','B')          # TypeError
# divide(345,0)              # ZeroDevisionError


# Exeption handling
# We write specific criteria so that code flow is not interrupted
# we write potential runtime error making code inside 'try'Block
# and we except will be caught by the 'except'block

# Rewriting the function with exeption block
# def divide_new(num,den):
#     try:
#         result = num/den
#         print(f'the answer is {result}')
#     except:
#         print('There is a problem ')

# divide_new(23,2)
# divide_new(5565,56)
# # RuntimeError
# divide_new('A','B')          # TypeError
# divide_new(345,0)   
# divide_new(55,5)           # ZeroDevisionError



# def divide_new1(num,den):
#     try:
#         result = num/den
#         print(f'the answer is {result}')
#     except Exception as e:
#         print(f'There is a problem : {e}')

# divide_new1(23,2)
# divide_new1(5565,56)
# # RuntimeError
# divide_new1('A','B')          # TypeError
# divide_new1(345,0)   
# divide_new1(55,5)

def divide_new2(num,den):
    try:
        result = num/den
        print(f'the answer is {result}')
    except TypeError:
        print('please make sure you enter numbers')
    except ZeroDivisionError:
        print('please make sure to give a non zero value as denominatior')
    except Exception as e:
        print(f'There is a problem {e}')

divide_new2(23,2)
divide_new2(5565,56)
# RuntimeError
divide_new2('A','B')          # TypeError
divide_new2(345,0)   
divide_new2(55,5)