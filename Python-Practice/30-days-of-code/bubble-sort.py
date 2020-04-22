array = [8,5,2,9,5,6,3]


def bubbleSort(array):
    # Write your code here.

    array_length = len(array) - 1

    for i in range(0, array_length):
        j = i + 1
        item1 = array[i]
        item2 = array[j]

        swapped = False

        if (item1 > item2):
            array[i] = item2
            array[j] = item1

            item1 = 0
            item2 = 0

            swapped = True

        if (swapped == True):
            bubbleSort(array)

    return array

bubbleSort(array)

array = bubbleSort(array)

print(array)

