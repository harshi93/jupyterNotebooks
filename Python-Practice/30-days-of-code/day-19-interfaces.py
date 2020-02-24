"""
Interfaces is object oriented concept, where a class implements specific set of methods and properities so that
other part of your application know how to interact with your class

interfaces help standardize interacting with code without dictating how specific parts are implemented

we are going to use abstract classes to define interfaces(simply because there are multiple ways to achieve inheritance)

The divisor = what is in the left (what is being used to divide)
The dividend = What is the center (what needs to be divided)
The Quotient = what is on the top (the times thing that needed to be divided got divided by thing that was used to divide)
The Remainder = what is left after dividing

integer quotient operation is referred to as division
integer remainder operation is referred to as modulus

An integer is a divisor of n if it divides n with no remainder, this can be achieved using modulus operator


range method by default includes the first variable and excludes the last variable
"""


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        running_total = 0
        for i in range(1, n + 1):
            if n % i == 0:
                running_total += i
        return running_total


#TODO take user input for last element
n = int(input())

my_calculator = Calculator()


s = my_calculator.divisorSum(n)


print("I implemented: " + type(my_calculator).__bases__[0].__name__)

#TODO print output of divisorSum function
print(s)