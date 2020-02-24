# TODO Given a sorted (in ascending order) integer array nums of n elements and a target value,
#  write a function to search target in nums. If target exists, then return its index, otherwise return -1.


"""
if nums is a list then to print complete list you just do
print(nums). If you want index number for elements in nums then print(nums.index(i))


In Binary Search algorithm

There is a left pointer, a right pointer and a middle pointer. The left pointer points to first element
The right pointer points to last element. The middle pointer indices is average of sum of indices smallest
and largest. We compare the target element with middle element

if left pointer is larger than right pointer it basically means the target element
does not exist
"""

#array = [0,1,21,33,45,45,61,71,72,73]
array = [1, 5, 23, 111]
target = 111

def checkIfTargetExists(target,array):
    targetExists = False

    if target in array:
        targetExists = True

    return targetExists

targetExists = checkIfTargetExists(target,array)

def binarySearch(target,array,targetExists):

    if targetExists == True:

        def calcInitialLRPointer(array):
            left_pointer = min(array)
            left_pointer_index = array.index(left_pointer)

            right_pointer = max(array)
            right_pointer_index = array.index(right_pointer)

            return left_pointer_index,right_pointer_index

        left_pointer_index, right_pointer_index = calcInitialLRPointer(array)



        def calcMiddlePointer(left_pointer_index, right_pointer_index):

            middle_pointer_index = (left_pointer_index + right_pointer_index) / 2

            middle_pointer_index = int(middle_pointer_index)

            middle_pointer = array[middle_pointer_index]

            return middle_pointer

        middle_pointer = calcMiddlePointer(left_pointer_index,right_pointer_index)


        if target == middle_pointer:
            def targetVsMiddlePtrEqualityCheck(middle_pointer):
                global target_index
                target_index = array.index(middle_pointer)

                print("The target index is: %s" % middle_pointer, "This is from equality condition")
                return target_index


        elif (target < middle_pointer):

            def targetIsSmallerCheck(middle_pointer, left_pointer_index):

                right_pointer_index = (array.index(middle_pointer) - 1)

                middle_pointer_index = (left_pointer_index + right_pointer_index) / 2

                middle_pointer_index = int(middle_pointer_index)

                middle_pointer = array[middle_pointer_index]

                if target == middle_pointer:

                    targetVsMiddlePtrEqualityCheck(middle_pointer)

                elif target < middle_pointer:

                    targetIsSmallerCheck(middle_pointer,left_pointer_index)

                else:

                    targetIsLargerConfirmation(middle_pointer,right_pointer_index)

                return middle_pointer

            middle_pointer = targetIsSmallerCheck(middle_pointer, left_pointer_index)

            print(middle_pointer)


        else:

            def targetIsLargerConfirmation(middle_pointer, right_pointer_index):

                left_pointer_index = (array.index(middle_pointer) + 1)

                middle_pointer_index = (left_pointer_index + right_pointer_index) / 2

                middle_pointer_index = int(middle_pointer_index)

                middle_pointer = array[middle_pointer_index]

                if target == middle_pointer:

                    targetVsMiddlePtrEqualityCheck(middle_pointer)

                elif target < middle_pointer:

                    targetIsSmallerCheck(middle_pointer, left_pointer_index)

                else:
                    targetIsLargerConfirmation(middle_pointer, right_pointer_index)

                return middle_pointer

            middle_pointer = targetIsLargerConfirmation(middle_pointer, right_pointer_index)

    else:
        return (target, "not found in the supplied array")

