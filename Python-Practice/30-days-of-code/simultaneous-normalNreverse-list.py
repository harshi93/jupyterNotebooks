list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list1_length = len(list1)

reverse_index = len(list2) - 1

for i in range(0, list1_length):
    if (i < list1_length):
        print(list1[i], end=" ")
    if(reverse_index >= 0):
        print(list2[reverse_index])
        reverse_index = reverse_index - 1