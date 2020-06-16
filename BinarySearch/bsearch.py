#Write a function that takes in a sorted array of integers and a target integer
#and returns the index of the number in the array if it matches with the target


#recursive solution
def binarySearch(array, target):
    def binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left+right) // 2
    targetMatch = array[middle]
    if target == targetMatch:
        return middle
    elif target < targetMatch:
        return binarySearchHelper(array, target, left, middle-1)
    else:
        return binarySearchHelper(array,target,middle+1,right)


#iterative solution
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left+right) // 2
        targetMatch = array[middle]
        if target == targetMatch:
            return middle
        elif target < targetMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1