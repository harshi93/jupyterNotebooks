list1 = [5, 20, 15, 20, 25, 20, 50]

list1_length = len(list1)

exists = False

element = 20

for i in range(0, list1_length):
    if(i < list1_length):
        if (list1[i] == element):
            exists = True

for i in range(0, list1_length):
    list1_length = len(list1)
    if(i < list1_length):
        if (exists == True):
            comp = 0
            comp = list1[i]
            if(comp == 20):
                list1.remove(list1[i])
                list1 = list1

print(list1)