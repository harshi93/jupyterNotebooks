#TODO Create Classes

class Employee:
    # init can be viewed as constructor, we can class instances whatever we want but by convention
    # we should refer them as self
    # pass statement - (the statement is used to simply ignore the code block)
    def __init__(self, first, last, name, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#TODO Instantiate Classes
emp_1 = Employee('Corey', 'Schaefer', 50000) # this is how class objects are instantiated
emp_2 = Employee('Test', 'User', 60000)

#TODO Create Instance Variables
    # instance variable contain data that is unique to each instance,
    # the below mentioned is an example of instance variable
print(emp_1);
print(emp_2); # these both will have unique addresses
print(emp_1.fullname()) # here self is getting passed in automatically

# TODO Create Class Variables
Employee.fullname(emp_1); # because this a class variable we need to explicitly
Employee.fullname(emp_2); # pass in the instance