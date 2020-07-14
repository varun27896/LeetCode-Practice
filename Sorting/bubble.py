def bubblesort(array):
    isSorted = False
    counter = 0 
    while not isSorted:
        isSorted = True #assuming the array is sorted
        for i in range(len(array) - 1 - counter): # -1 to check only the value and the one before it and counter to leave the ones that are sorted assuming they are the largest
            if array[i] > array[i+1]:
                swap(i,i+1, array)
                isSorted = False #if it enters this condition, it is obviously not sorted
        counter += 1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

#Time complexity : O(n^2) because of the number of iterations. If the array was sorted : O(n)
#Space complexity: O(1)