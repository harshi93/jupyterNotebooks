array = [0,1,21,33,45,45,61,71,72,73]
target = 33


def binarySearch(array, target):
    # Write your code here.
    left_ptr = 0
    right_ptr = len(array) - 1
    middle_ptr = int((left_ptr + right_ptr) / 2)
    middle_ptr_value = array[middle_ptr]

    target_value_index = 0

    element_exists = False

    if target in array:
        element_exists = True
    else:
        binarySearchResults = -1
        return binarySearchResults

    if(element_exists == True):
        def middlePointerComparator(middle_ptr_value,middle_ptr,left_ptr,right_ptr):

            if (middle_ptr_value > target):
                right_ptr = middle_ptr - 1
                middle_ptr = int((left_ptr + right_ptr) / 2)
                middle_ptr_value = array[middle_ptr]
                return middlePointerComparator(middle_ptr_value, middle_ptr, left_ptr, right_ptr)


            elif (middle_ptr_value < target):
                left_ptr = middle_ptr + 1
                middle_ptr = int((left_ptr + right_ptr) / 2)
                middle_ptr_value = array[middle_ptr]
                return middlePointerComparator(middle_ptr_value, middle_ptr, left_ptr, right_ptr)


            else:
                target_value_index = middle_ptr
                return target_value_index




    index_value = middlePointerComparator(middle_ptr_value,middle_ptr,left_ptr,right_ptr)

    return index_value


binarySearchResults = binarySearch(array, target)

print(binarySearchResults)