# ***************************************************
# *********check weather the number is greater*******
# ***************************************************

#number = input(' Enter a number :')
# number_int = 27           # converts the input as number.

# if(number_int > 50) :
#     print('The number entert is bigger than 50')

# if(number_int < 50) :
#     print('the number enterd is smaller than 50')

# print('End program')

#number > 50  # The number entert is bigger than 50.
#number <= 50 # The number is less than or equal to 50.


# number = 77

# if(number > 50):
#     print('The number is gerater than 50')
# else:
#     print('The number is smaller than 50')
# print('End the progaram')

# print('*********************************************')

# num = input('Enter a number  :')
# num1 = int(num)
# reminder = num1%2

# if(reminder == 0):
#     print('The number is even')
# else:
#     print('The number is odd')
# print('End the program')

# *******************************************************

# temp = input('\n Enter the tempreature  :')

# >= 35 : very hot
# 25 -35 : warm
# 15 - 25 : cold
# <= 15 : freezing
# temp = float(temp)

# if(temp >= 35):
#     print('its a very hot day')
# else:
#     if(temp >= 25):
#         print('its awarm day')
#     else:
#         if(temp >= 15):
#             print('its a cold day')
#         else:
#             print('its a freezhing day')
# print('End of program')


# if(temp >= 35):
#     print('\n its a very hot day \n')
# elif(temp >= 25):
#     print('\n its a warm day \n')
# elif(temp >= 15):
#     print('\n its a cold day \n')
# else :
#     print('\n its a freezing day \n')
# print('--------The End--------\n')


# *************************************************
# **************Interative statements**************
# *************************************************

# For loop : used when no of iterations are known
# while loop : used when no of iteration are unknown. but stop conditions are known

# Print your name 10 times

# for i  in range (10):       # we are giving number of iterations.
#     print(i, ': Aakash')         # iterative (repetitive) task.

# print('\n-------Step operator------\n')

# for i  in range (3,10,3):       # we are giving number of iterations.
#     print(i, ': Aakash')         # iterative (repetitive) task.

# print('*********************')

# for i  in range (10,3,-1):       # we are giving number of iterations.
#     print(i, ': Aakash')         # iterative (repetitive) task.

    
# for i in range(50):
#     if(i%2 !=0):
#         print(i,'\n: odd number')

# print('*****************************')


# for i in range(20,50):
#     if(i%2 !=0):
#         print(i,': odd number\n')

# for i in range(1,50,2):
#     print(i,': odd number')

# **************************************************
# ********************While loop********************
# **************************************************

num = 1
while(num < 10):
    print(num)
    num = num + 2
print('End of wwhile loop\n')

# num1 = 1
# while(num1 < 50):
#     if(num1 % 2 != 0):
#         num1 = num1 + 1
#         print(num1)
#           num1 = num1 + 1

# num = 1
# while(num < 50):
#     print(num)
#     num = num + 2
# print('End of wwhile loop\n')


# num2 = 1
# while(num2 < 50):
#     print(num2, end = ',')
#     num2 = num2 + 2
# print('End of while loop\n')

# **********************************************************
# *********************logical Operators********************
# **********************************************************

age = int(input('please Enter your age: '))
valid_id = input('Do you have a valid id card (y/n) : ')

if (valid_id == 'y'):
    valid_id = True    # only if the user types y.
else:
    valid_id = False   # only if the user types n.

# veryfing eligibility to vote
print('We are checking yiur Eligibility')

if (age >= 18):
    if(valid_id):
        print('\nYou are eligible to vote.')
    else:
        print('\nyou are note eligible to vote')
        print('\nyou need a valid id card for eligible to vote')

else:
    print('\nyou are note eligible to vote')
    print('\nyou need age 18 to eligible for vote')

print('\n-------------------------------------------\n')
