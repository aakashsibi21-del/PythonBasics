class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print('Person Name : ',self.name,'\nAge : ',self.age)

class Employee(Person):
    def __init__(self, name, age, emp_id, salary, join_year):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary
        self.join_year = join_year
    def display_Emp(self):
        print('Employee Name : ',self.name,'Employee Age : ', self.age,
               '\nEmployee Id',self.emp_id,'\nSalary : ', self.salary,'\nJoin Year : ', self.join_year)

class Father(Person):
    def __init__(self, name, age, no_of_child):
        super().__init__(name, age)
        self.no_of_child =no_of_child
    def display_Father(self):
        print('',self.name, self.age, self.no_of_child)

class Son(Person):
    def __init__(self, name, age, father_name, mother_name):
        super().__init__(name, age)
        self.father = father_name
        self.mother_name = mother_name
    def display_son(self):
        print(self.name, self.age, self.father, self.mother_name)

class Husband(Person):
    def __init__(self, name, age, wife_name, marrage_year):
        super().__init__(name, age)
        self.wife_name = wife_name
        self.marrage_year = marrage_year
    def display_husband(self):
        print(self.name, self.age, self.wife_name, self.marrage_year)

person = Person('BatMan', 22)
emp = Employee('BatMan','22', 1214, 500000, 2026)
father = Father('BatMan', 22, 5)
son = Son('BatMan',22,'Sibi','Swapna')
hus = Husband('BatMan', 22 ,'BatWomen','15/8/2031')

person.display_person()
emp.display_Emp()
father.display_Father()
son.display_son()
hus.display_husband()
print('\n**************************************************\n')


class Employee1:
    def __init__(self):
        pass
    def claculate_salary(self):
        print('Employee Salary : ')

class FullTime_Employee(Employee1):
    def calculate_salary(self):
        print('Full time employee recives a fixed monthly salary')

class Part_time_employye(Employee1):
    def calculate_salary(self):
        print('Part time employee salary is based on working hours')

class Freelancer(Employee1):
    def calculate_salary(self):
        print('Freelance salary is based on complete projects')

emp1 = Employee1()
full = FullTime_Employee()
part = Part_time_employye()
Free = Freelancer()

emp1.claculate_salary()
full.calculate_salary()
part.calculate_salary()
Free.calculate_salary()

from abc import ABC, abstractmethod

class BankAccount(ABC):
    

    def __init__(self, Account_Holder, Account_Type, Balance):
        self.Account_Holder = Account_Holder
        self._Account_type = Account_Type
        self.__Balance = Balance

    def calculate_interest(self):
        pass


    @property
    def Balance(self):
        return self.__Balance

    @Balance.setter
    def Balance(self, Deposite):
        if Deposite <= 0:
            raise 'Deposite Amount Cannot be A Zero or Negative Number'
        self.__Balance = self.__Balance + Deposite
        print('Deposite successfully : ', Deposite,'\nBalance : ', self.Balance)

    @Balance.setter
    def Balance(self, withdraw):
        if withdraw <= 0:
            print( 'Deposite Amount Cannot be A Zero or Negative Number')
        if withdraw >= self.Balance:
            print('Insufficent Balance')
        self.__Balance = self.__Balance - withdraw
        print('Deposite successfully : ', withdraw,'\nBalance : ', self.Balance)
    

class SavingsAccont(BankAccount):
    def __init__(self, Account_Holder, Account_Type, Balance):
        super().__init__(Account_Holder, Account_Type, Balance)

    def calculate_interest(self, rate):
        self.intrest = rate
        self.intrest = self.Balance * (5 /100)

    def display_details(self):
        print('Account Holder : ',self.Account_Holder,'\nAccount Type : ',self._Account_type,
              '\nBalance Amount : ',self.Balance,self.intrest)
    

class CurrentAccount(BankAccount):
    def __init__(self, Account_Holder, Account_Type, Balance):
        super().__init__(Account_Holder, Account_Type, Balance)

    def calculate_interest(self, rate):
        self.intrest = rate
        self.intrest = self.Balance * (rate/100)

    def display_details(self):
        print('Account Holder : ',self.Account_Holder,'\nAccount Type : ',self._Account_type,
              '\nBalance Amount : ',self.Balance,self.intrest)



# bank = BankAccount()
savings = SavingsAccont('Rahul', 'Savings',10000)
savings.calculate_interest(0.5)
print(savings.Balance)
curr = CurrentAccount('Ashbi', 'current',20000)
curr.calculate_interest(0.2)
curr.display_details()

