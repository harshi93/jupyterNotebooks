#TODO Print Pattern using Hash
a = "#"
l = 5
for i in range(0,l):
    print(a)
    if i == l-1:
        break
    print(a, end="")
    for y in range(0,i):
       print(a, end="")