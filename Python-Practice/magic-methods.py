# TODO Special/Magic Methods
"""
Magic methods allow us to emulate built-in behavior in python and also allow us to perform operator overloading

special methods are always surrounded by double underscore or dunder

__init__, __repr__, __str__, are some of the most commonly used magic methods

__repr__ should be used providing unambiguous representation of object and are often used for debugging purposes
the method is meant for use by other developers

__str__ is meant to be readable representation of object, and is used to display information to end user
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
        return int(self.pay * self.raise_amount)

    def __repr__(self):

        """ The repr gives you value + origin, for e.g. repr would print UUID("something") """

        return "Employee('{}', '{}')".format(self.first, self.last)

    def __str__(self):

        """ The str gives just value, for e.g. str would print 'something' """
        return "{} - {}".format(self.fullname(), self.email)


emp_1 = Employee('Corey', 'Schaefer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(repr(emp_1))
print(str(emp_1))