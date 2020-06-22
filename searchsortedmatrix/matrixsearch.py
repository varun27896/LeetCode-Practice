#2d array of distinct sorted integers and a target integer that is given.
#write a function that returns an array of the row and column indices of the
#target integer if it is contained in the matrix otherwise [-1,-1]

def searchMatrix(matrix, target):
    row = 0 #initializing the first element in matrix array as 0
    col = len(matrix[0]) - 1 #setting the last value of the array as the column
    while row < len(matrix) and col >= 0: #as long as the value of the row is less than the length of the matrix and column is always greater that 0 to avoid negative values we start a loop
        if matrix[row][col] > target: #if the value of the matrix is greater than the target, we can eliminate the columns to the right side of it because they will be greater
            col -= 1
        elif matrix[row][col] < target: #similarly if its lesser then we eliminate the ones to the left and increment the row
            row += 1
        else:
            return [row,col] #if there is a match we return the indices of the row and col

    return [-1,-1] 