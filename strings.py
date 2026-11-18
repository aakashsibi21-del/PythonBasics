string1 = 'dfghjkhgfdsdfghjklkjhgfdfghjhgfdsdfghjhgfd'

string2 = 'python'
string3 = 'programming'

print(string1)     
print(string2)
print(string3)
print("\n")
print(string2,string3)

# by default python print a new line at te end.

print(string2, end='&')
print(string3, end='&')
print("\n",end='&')
print(string2,string3,end='&')

# \n new line
# \t new tab
# end = end line
print('\t', string2, string3)
print('**********************************************')
# *************************************************************
# *********************string contcatenuation******************
# *************************************************************

s1 = 'ict'
s2 = 'Academy'
s3 = 'of'
s4 = 'kerala'

print(s1 + s2 +s3 +s4)   # ictAcademyofkerala
print(s1, s2, s3, s4)    # ict Academy of kerala

combined_string = s1 +' '+ s2 +' '+ s3 +' '+ s4
print(combined_string)
print('******************************************8')

print(s1)
print(s1 + s1 + s1 + s1 + s1)
print((s1 +' ') * 5)
print((s1 +'\t ') * 5)
print((s1 +'\n') * 5)

print('****************************************')

print(string3)
print(string3[0])   # to print 0th index value

print(string3[5])
print(string3[10])
#print(string3[11]) we cannot go beyond maximum index of a string

string1 = 'dfghjkhgfdsdfghjklkjhgfdfghjhgfdsdfghjhgfd'
print(string1[-1])   # last value of a string
print(string1[-5])   # start from last index

print('************************************')

# **************************************************
# *******************Slicing************************
# **************************************************

s1 = ('Trivandrum')
print(s1)
print(s1[-4])      # will disply 7th character
print('print index 6 =',s1[6])
print('print index 0 to 5 =',s1[0:5])     # Slicing. start index = 0, end index = 4. = triva
print('print index 6 to 10 =',s1[6:10])    # Slice drum

# print(s1[10])       there is no index value stored as
#                     10 but in slice the last value was excluded

print('print index 4 to 7 =',s1[4:7])

print(s1[:5])          # print from start index till 5.
print(s1[:6])          # print from start index from 6.
print(s1[0:])          # print from 0th index to end index

# step Operation for take values from 2 steps = tia.
print('step operation with 2 = ',s1[0:5:2])      
print('step operation with 2 = ',s1[:5:2])     

# step opertion take values from 3 steps = tvd.
print('step operation with 3 = ',s1[0:8:3])   

String_demo ='Welcome to a diverse array of programs designed to empower you with'
print(String_demo[5:])
print(String_demo[5::2])
print('*******************************************')

print(s1)
print(s1[::-1])   # reversing the string using slicing methord.
print(s1[::-2])   # step operation from backword.

# **************************************************
# ********************Function**********************
# **************************************************

print(s1)
print(s1.lower())        # covert into lowercase.
print(s1.upper())        # covert into uppercase.
print(s1.swapcase())     # covert into uppercase into lower case and lower case into upper case.
print(s1.capitalize())   # convert bfirst letter will be uppercase.

 