#TODO  Given a two-digit integer n. Return the sum of its digits.


def addTwoDigits(n):
    for n in range(10,99):
        i = list(str(n))
        i = int(i[0]) + int(i[1])
        print(i)