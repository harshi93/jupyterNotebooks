array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


array_length = len(array)

target_array = []

operand2 = 0

for i in range(0, array_length):
    operand1 = array[i]
    for j in range(0, array_length):
        if(j != i):
            second_element = array[j]
            operand2 = second_element + operand1
            if(operand2 == targetSum):
                operand1_element_exists = False
                second_element_exists = False
                if operand1 in target_array:
                    operand1_element_exists = True
                else:
                    operand1_element_exists = False
                if(operand1_element_exists == False):
                    target_array.append(operand1)
                if second_element in target_array:
                    second_element_exists = True
                else:
                    second_element_exists = False
                if (second_element_exists == False):
                    target_array.append(second_element)
            operand2 = 0
            j += 1
        else:
            print(target_array)
