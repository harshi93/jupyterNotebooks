# TODO Creating subclasses
"""
Subclasses allow us to inherit attributes of parent class alongside giving the ability
to add new and override existing functionality. These are a good example of inheritance

Chain of inheritance or Method resolution order = looking for something in parent classes
when it can't find something in child classes
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


class Developer(Employee):
    """
    The use super function to access parent class is mostly useful in cases where you want to
    leverage single level inheritance

    In cases where we have to implement multi-level inheritance it makes more sense to leverage
    class names to access class methods for e.g. in multi-level inheritance we would use
    Employees.__init__() to access attributes of employees class rather using super().
    """

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# TODO Input


dev_1 = Developer('Harshit', 'Singh', '80000', 'Python')
dev_2 = Developer('Harjeet', 'Singh', '80000', 'Java')
mgr_1 = Manager('Avineshwar', 'Singh', '200000', [dev_1])

mgr_1.add_emp([dev_2])
mgr_1.remove_emp([dev_1])

# TODO print out dev 1 email
print(dev_1.email)

# TODO print out dev 2 programming language
print(dev_2.prog_lang)

# TODO print out manager email and number of employees under supervision
print(mgr_1.email)
print(mgr_1.print_emps())

# TODO verify class membership of manager
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))