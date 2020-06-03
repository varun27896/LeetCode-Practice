def smallestDiff(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0 #initialising pointer for the first array
    idxTwo = 0 #pointer for the second array
    smallest = float("inf") #to make it easier while checking the value condition
    current = float("inf")  #value of the absolute difference
    smallestPair = [] #empty array that stores the two numbers from the arrays
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1 #increment the pointer because the sorted first array will have numbers greater than the previous one and they will be less farther to the other numbers in the second array
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair

