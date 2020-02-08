#TODO Class Variables

"""
Reference: Class Objects

The way these objects work are whenever the instance variables are initialized
if the instance variables themselves don't have an attribute they go looking for
that variable in the class to which they belong and inherit the value from there
this will print the values that exist within the variable itself any value
that doesn't get listed out here but still returns a valid response will get
inherited from the class to which the object belongs
"""

Class Employee:

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
        return int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schaefer', 50000)
emp_2 = Employee('Test', 'User', 60000)


# TODO print out the value of class variable
print(Employee.raise_amount)

# TODO print out content of class object
print(emp_1.__dict__)

# TODO print out raise amount for employee 2
print(emp_2.raise_amount)

# TODO return amount after raise is applied for both employees

print(Employee.apply_raise(emp_1))
print(Employee.apply_raise(emp_2))
print(emp_1.apply_raise())
print(emp_2.apply_raise())

# TODO print out total number of employees
print(Employee.num_of_emps)
