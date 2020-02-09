#TODO Regular Methods
"""
Regular methods in a class automatically take instance as the first argument
by convention this referred to as self.

Class methods takes class as the first argument

You use a decorator to convert a regular method into class method
"""
import datetime

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay;


# TODO Class Methods
    """ 
    The decorator @classmethod converts a regular method into class method
    by telling function that accept first argument as class name instead
    of instance variable
    """


    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount;

    """ 
    The below style of taking and processing information using classmethods
    is referred to as alternative constructor method. The alternative constructor 
    method is way to leverage classmethods to provide ways to create class objects
    
    Alternative constructor method usually start with 'from' 
    """

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


# TODO Static Methods

    """
    The regular methods pass instance variable automatically class methods pass class 
    name as instance automatically, static methods pass nothing they act like function and 
    because of their connection with classes they are referred to as class methods
    """

    @staticmethod
    def is_workday(day):
        if day.weekday() > 5 and day.weekday() <= 7:
            return False
        return True


# TODO Input
emp_1 = Employee('Corey', 'Schaefer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
new_emp_3 = Employee.from_string(emp_str_3)


my_date = datetime.date(2020, 7, 2)

# TODO print raise amount for a class objects
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# TODO print applied raise amount for class objects
print(Employee.apply_raise(emp_1))
print(Employee.apply_raise(emp_2))
print(Employee.set_raise_amt(10))
#print(emp_1.set_raise_amt(20))
#print(emp_2.set_raise_amt(30))

# TODO add new employees to the class and print output using alternative constructor methods
print(new_emp_1.email)
print(new_emp_2.pay)
print(new_emp_3.first)

# TODO print for whether given day is a workday or not
print(Employee.is_workday(my_date))

