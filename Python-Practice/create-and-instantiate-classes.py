# TODO Create Classes

class Employee:
    """
    init can be viewed as constructor, we can class instances whatever we want
    but by convention we should refer them as self

    Quick Note: pass statement - (the statement is used to simply ignore the code block)

    instance variable contain data that is unique to each instance
    """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# TODO Instantiate Classes


""" This is how class objects are instantiated """

emp_1 = Employee('Corey', 'Schaefer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# TODO Create Instance Variables

""" The below mentioned is an example of instance variable, these both will have unique addresses """
print(emp_1);
print(emp_2);

""" Here self is getting passed in automatically """
print(emp_1.fullname())

# TODO Create Class Variables

""" This a class variable and so we need to explicitly, pass in the instance """
Employee.fullname(emp_1);
Employee.fullname(emp_2);
