# **********************************************
# *********************set**********************
# **********************************************

# set values display not in order
# in set we cannot do operations using index values
# in set repetations are note allowdwd

# declaring a set
# method 1
# set1 = {}
# print(type(set1))
# # method 2
# set2 = {12, 13, 14, 2026, 'A', 67.8, True, 2026, '2026', 2026.0}
# print(type(set2))
# # method 3
# set3 = set()
# print(type(set3))

# print(set2)
# print('******************************************')

# roll = {1, 2, 3, 4, 5, 6}
# roll_odd = {1, 3, 5}
# roll_even = {2, 4, 5}
# random = {1, 5, 9, 4}

# random.add(2026)
# print(random)

# print(random.difference(roll_odd))
# print(roll_odd.difference(random))

# print(roll.issuperset(roll_odd))
# print(roll.issubset(roll_odd))
# print(roll.issuperset(random))
# print(roll.intersection(roll_odd))
# print(roll.issuperset(roll_odd))
# print(roll.discard(roll_odd))
# print(roll.intersection_update(roll_odd))

# *******************************************************
# ********************dictionary*************************
# *******************************************************

# declaring a set
# method 1
dict1 = {}
print(type(dict1))
# method 2
dict2 = {'key1' : 'value1', 'key2' : 'value2', 8 : '2027', True : 'yes'}
print(type(dict2))
# method 3
dict3 = dict()
print(type(dict3))

print(dict2)
print(dict2[8]) 

sample_dict = {1 : 'one', 0 : 'zero', 1 : True}
print(sample_dict)

# {1: True, 0: 'zero'} because true is the latest value assigned to key 1
# duplication of keys are note allowed 

print(dict2['key2'])       # value assiociated in key 2

student_dict = {'Name': 'Aakash',
                'Age': 21,
                'Course': 'BCA',
                'University': 'MG University',
                'District': 'Idukki'}

# print(the wholw dictionary)
print('\nWhole Dictionary\n')
print(student_dict)
print('\nkeys are')
print(student_dict.keys())
print('\nitems are')
print(student_dict.items())

student_dict['University'] = 'kearala Univesity'
print(student_dict)

# Create a new dictionary and stire avlues of a student 
# display all the informations you store 
# edit the informations in the dictionary

Personal = {'Name': 'Aakash',
                'Age': 21,
                'Birth Year': '2005',
                'phone': '9946754634',
                'email': 'flash123@gmail.com', 
                'Course': 'BCA',
                'University': 'kerala University',
                'District': 'Idukki',}
print(Personal)
key = input('Enter a Key : ')
details = input('Enter  Details : ')
#key = Personal.keys()
#Personal.keys() = details
Personal[key]=details
print(Personal)
