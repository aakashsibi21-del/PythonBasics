# ******************************************************
# *************** File handling ************************
# ******************************************************


#
file_path = "D:\\PGP_Data_Science_and_AIML\\Python\\test _file.txt"
relative_filepath = 'test _file.txt'


def read_file_filepath():
    file = open(file_path, 'r')                 # Assign a file into reading mode.
    content = file.read()                       # content of the file  is assigned to 'content'
    print(content)   
    # file.close()                   


def file_relative_filepath():
    file_1 = open(relative_filepath, 'r')
    content_1 = file_1.read()
    print(content_1)
    # file_1.close()

# file.read() will return all the values as a single string.

# print(type(content_1)) a single string

def file_relative_filepath1():
    file_ = open(relative_filepath, 'r')
    content_ = file_.readline()           # only the first line
    print(content_)
    print(type(content_))
    file_.close()
# file_relative_filepath1()

def file_relative_filepath1():
    file_ = open(relative_filepath, 'r')
    content_ = file_.readlines()           # read all lines and populates the list.
    print(content_)
    print(type(content_))
    for line in content_:
        print(line)
    file_.close()
# file_relative_filepath1()

# *******************************************************
# ************************ Write ************************
# *******************************************************

write_path = 'student.txt'

# opens a file in writting mode
# if the file didint exist erlier , now it will be created
# and opend the writing mode.


def write_file():
    file = open(write_path, 'w')
    file.write('Vishnu\n')
    file.write('gowthem\n')
    file.write('aakash\n')

    file.close()
write_file()


# def input_str(get_input):
#     file = open(write_path, 'w')
#     file.write(get_input)
#     file.close()
# input_str('vishnu')


# append data into the file
def append_file():
    file = open(write_path,'a')
    file.write('Keerthy\n')
    file.close()
append_file()


# generic function to uppend a file
def input_name(file_path, get_input):
    file = open(file_path, 'a',)
    file.write(get_input)
    file.close()
input_name('student.txt','BatMan\n')

#file assigning is more preferable methord.
def append_data(file_path,get_input):
    with open(file_path, 'a') as file:
        file.write(get_input)
append_data('student.txt', 'SuperMan')