# **********************************************************************
# ************************ encapsulation********************************
# **********************************************************************


class BankAcccount:
    def __init__(self, owner_name, bank_balance, account_type):
        self.owner_name = owner_name
        self.__bank_balance = bank_balance
        self._account_type = account_type

    #to get tye bvalue of a private property
    @property
    def bank_balance(self):
        return self.__bank_balance

    @property
    def account_type(self):
        return self._account_type

    
    # to update the value of a private atribute
    @bank_balance.setter
    def bank_balance(self, deposite_atm):
        if deposite_atm <= 0:
            raise 'Deposite amount cannot be zerro or negative values'
        self.__bank_balance = self.__bank_balance + deposite_atm

    @account_type.setter
    def account_type(self, type):
        if type not in ["Fixed","current","savings"]:
            raise 'You have entered a wrong account type'
        self._account_type = type

        
    


bank = BankAcccount('Aakash', 2500, 'Savings')

print(bank.bank_balance)
print(bank.account_type)


# syntax: class.setter function + new value
bank.bank_balance = 50
print(bank.bank_balance)

bank.account_type = 'current'
print(bank.account_type)

print('\n******************************************\n')



class Employee:
    def __init__(self, Emp_name, department, salary):
        self.Emp_name = Emp_name
        self._department = department
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, update):
        if update <= 0:
            raise 'salary cannot  be Zero or negative'
        self.__salary = self.__salary + update

Emp = Employee('Aakash', 'Data Science', 10000)


print(Emp.salary) 

class Manager(Employee):
    def display_destails(self):
        print('\nName       : ',self.Emp_name,'\nDepartment : ',self._department)

Manage = Manager('Aakash', 'Data Science', 10000)
Manage.display_destails()

manager = Manage.display_destails()
print('current Salary ',Emp.salary)
Emp.salary = 5000
print('Updated salary ',Emp.salary,'\n')
print('\n*******************************************')


class Vehicle:
    def __init__(self, vehicle_name, rental_type, rental_price):
        self.vehicle_name = vehicle_name
        self._rental_type = rental_type
        self.__rental_price = rental_price

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, update):
        if update <=0:
            raise 'Rental Price Cannot be Zero or Negative.'
        self.__rental_price =  update

    def display_details1(self):
        print('\nVehicle Name : ',self.vehicle_name,'\nRental Type : ',self._rental_type,'\n')

veh = Vehicle('BMW','Manuel', 10000)
veh.display_details1()

class Car(Vehicle):
    def calculate_rent(self,days):
        self.rental_price = (self.rental_price) * (days)

    def display_details1(self):
        print('\nVehicle Name : ',self.vehicle_name,'\nRental Type : ',self._rental_type,'\nRental Price : ', self.rental_price)

car = Car('toyota','day wise', 2000)
car.display_details1()



class Bike(Vehicle):
    def calculate_rent(self,days):
        self.days = days
        self.rental_price = self.rental_price * days

    def display_details1(self):
        print('\nVehicle Name : ',self.vehicle_name,'\nRental Type : ',self._rental_type,'\nRental Price : ', self.rental_price)

bike = Bike('Yamaha','day wise', 2500)
bike.calculate_rent(5)
bike.rental_price = 1000
bike.calculate_rent(5)
bike.display_details1()
