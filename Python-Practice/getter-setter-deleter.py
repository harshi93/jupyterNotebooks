# TODO Decorators

"""
The @property is decorator that basically lets us define a property as method
but access it as an attribute

"""


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

# TODO Input


emp_1 = Employee('John', 'Doe')
emp_1.first = 'James'

emp_2 = Employee('Jeena', 'Doe')
emp_2.fullname = 'Jessie Doe'

# TODO recreate emp 1 using new fullname, alongside leveraging setter


print(emp_1.email)
print(emp_1.fullname)

# TODO Delete a record using deleter


del emp_2.fullname