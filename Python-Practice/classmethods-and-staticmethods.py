#TODO Regular Methods
"""
Regular methods in a class automatically take instance as the first argument
by convention this referred to as self.

Class methods takes class as the first argument

You use a decorator to convert a regular method into class method
"""

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
        return cls.raise_amount;



# TODO Static Methods


# TODO Input
emp_1 = Employee('Corey', 'Schaefer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# TODO Output
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.apply_raise(emp_1))
print(Employee.apply_raise(emp_2))
print(Employee.set_raise_amt(10))

#print(emp_1.set_raise_amt(20))
#print(emp_2.set_raise_amt(30))