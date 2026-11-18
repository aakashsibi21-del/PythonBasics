# list is a datatype used to store a collection of values 
# since it is combination of other data types () int, float, 
# Stinrg, boolean), we call it as a derived dataype

#  te is no restriction pn terms of datatypes in a list

# declare a list
# name = ''
# print(type(name))

# methord 1
# list_names1 = []
# print(type(list_names1))

# # Methord 2
# list_names2 = ['Aakash', 'Ajith', 'vishnu']
# print(type(list_names2))

# list_names3 = list()
# print(type(list_names3))

# print(list_names2[0])
# print(list_names2[1])
# print(list_names2[2])

# list with multiple datatyes (Heterogenous)
# lst_1 = ['Aakash', 21, 'thodupuzha', 2026, 'MG University', 190.5, list_names2]
# print(type(lst_1))

# print('\n',(lst_1[0]))       # display value at inex = 0
# print(type(lst_1[0]))        # display the datatypes of index = 0

# print('\n',(lst_1[1]))       # display value at inex = 1
# print(type(lst_1[1]))        # display the datatypes of index = 1

# print('\n',(lst_1[2]))       # display value at inex = 2
# print(type(lst_1[2]))        # display the datatypes of index = 2

# print('\n',(lst_1[3]))       # display value at inex = 3
# print(type(lst_1[3]))        # display the datatypes of index = 3

# print('\n',(lst_1[4]))       # display value at inex = 4
# print(type(lst_1[4]))        # display the datatypes of index = 4

# print('\n',(lst_1[5]))       # display value at inex = 5
# print(type(lst_1[5]),'\n')   # display the datatypes of index = 5


# list_1 = [1, 7, 3]
# list_2 = [False, True, False]

# print(list_1 + list_2)       # list contcatunation

# list_1.sort()                # sort in Assending order
# print(list_1)

# list_1.sort(reverse= True)   # sort in Decending order
# print(list_1)

# list_names2.sort(reverse= True)
# print(list_names2)

# list_names2.extend(list_1)   # Extend list with values of another list
# print(list_names2)
# print(list_names2[3])

# list_2.append(list_1)        # List_1 was added the last value of list_2
# print(list_2)
# print(list_2[3])

# list_1.append('A')
# print(list_1)

# list_1.reverse()             #  just Reverse the list not sort it
# print(list_1)

# # *************count**********
# print('\nno of false = ',list_2.count(False))
# print('\nno of true',list_2.count(True))
# print('\nno of x = ',list_2.count('x'),'\n')

# # Value of last index 
# # len(list_2) 
# # print('total number of elements in list',list_2, 'is', len(list_2))

# len(list_2[-1])
# print(list_2[len(list_2)-1])

# print('******************************************\n')
# print('before clear')
# print(list_2)

# list_2.clear()

# print('adter clear')
# print(list_2)

# print('\n***********************************\n')

# print('before inserting value = ',list_1) # [7,3,1, 'a']
# # inorder to do [7,3,1 ,'a'] = [7,3,1 ,100,'a'] nee dto add one number
# list_1.insert(2,100)
# print('\n adter inserting value = ',list_1,'\n')  # ['A', 1, 100, 3, 7] 


# list_1.insert(3, list_names2)
# print('\n adter inserting value = ',list_1,'\n')  # ['A', 1, 100, 3, 7] 
# print('*****************************\n')
# print('removig 3 ',list_1)
# list_1.remove(list_names2)
# print('after removing 3 ',list_1,'\n')
# print('*******************************\n')

# # to remove the last value in a list
# list_1.pop()
# print(list_1)

# ****************************************************
# **********************tuple*************************
# ****************************************************

# tuple is a datatype used to store a collection of values 
# since it is combination of other data types () int, float, 
# Stinrg, boolean), we call it as a derived dataype

#  te is no restriction pn terms of datatypes in a tuple
# a touple can store various type of data

# Touple Ones it is defined the values cannot be changed 

# list = mutable(can make changes )
# tuple = immutable (cannot make changes)


# declaring a tuple
tuple1 = ()
tuple2 = (2026, 'Nov', 2.45, False, [8, True, 9.8] )
tuple3 = tuple()

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

print(tuple2[2])

print(tuple2.count('Nov'))
print(tuple2.index('Nov'))

print(tuple2)
# print (list_2) 