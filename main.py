import numpy as np

# -----------------------------------------------------------------------------------
#                            Global Variable
# -----------------------------------------------------------------------------------
mCount = list(range(0, 36))

# -----------------------------------------------------------------------------------
#                            Global Function
# -----------------------------------------------------------------------------------
def buildWareHouse(matrix_arry):
    # Assign shelf locations
    matrix_arry = layoutOne(matrix_arry)
    return matrix_arry

def layoutOne(matrix_arry):
    # Shelf position at 3, 8, 11, 13, 15, 17, 20, 27, 30, 34
    matrix_arry = [[1, 2, 'D', 4, 5, 6], [7, 'A', 9, 10, 'G', 12], ['E', 14, 'B', 16, 'I', 18],
                   [19, 'C', 21, 22, 23, 24], [25, 26, 'F', 28, 29, 'H'], [31, 32, 33, 'J', 35, 36]]

    return matrix_arry

def fillOrder(matrix_arry, order, status):
    pass
    # Eventually run this until status is True because order is filled

def searchWareHouse(matrix_arry, status):
    #begin search
    shelf_list = ['A','B','C','D','E','F','G','H','I','J']
    row = 0
    col = 0

    current_position = 0

    # Change while loop back to status check once traversal complete
    #--while status is False:
    while row < 6:
        if col <= 5:
            status = searchNeighbors(matrix_arry, row, col, status)
            col += 1
        else:
            row += 1
            col = 0
        # Must make a condition that toggles True/False
        #--status = True

    return status
    """
    for i in range(0,6):
        for j in range(0,6):
            if isinstance(matrix_arry[i][j], str):
                print('string')
            else:
                print('integer')
    """

def searchUp(matrix_array, row, col):
    # temp variable starts as -1 in case we try to move out of bounds.
    # if row is not 0 then the temp variable will return new value.
    temp = -1
    if row > 0:
        temp = matrix_array[row - 1][col]
        return temp
    else:
        return temp

def searchDown(matrix_array, row, col):
    temp = -1
    if row < 5:
        temp = matrix_array[row + 1][col]
        return temp
    else:
        return temp

def searchLeft(matrix_array, row, col):
    temp = -1
    if col > 0:
        temp = matrix_array[row][col -1]
        return temp
    else:
        return temp

def searchRight(matrix_array, row, col):
    temp = -1
    if col < 5:
        temp = matrix_array[row][col + 1]
        return temp
    else:
        return temp

def searchNeighbors(matrix_arry, row, col, status):
    mUp = 0
    mDown = 0
    mLeft = 0
    mRight = 0

    mUp = searchUp(matrix_arry, row, col)
    mDown = searchDown(matrix_arry, row, col)
    mLeft = searchLeft(matrix_arry, row, col)
    mRight = searchRight(matrix_arry, row, col)

    print(mUp, mDown, mLeft, mRight)

    # Use this to search for shelves


# -----------------------------------------------------------------------------------
#                         Executes Main Program
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # Variable checks if the order is completed or not
    order_filled = False

    # Size of the array is established
    rows, cols = (6, 6)

    # mCount will be used to record the path location
    #for i in mCount:
    #    mCount[i] = mCount[i] + 1
    #    print(mCount[i])

    # Build the warehouse matrix 6 x 6
    matrix_arry = [[-1] * cols] * rows
    matrix_arry = buildWareHouse(matrix_arry)

    # This will be the end as the order status will be changed to True
    order_filled = searchWareHouse(matrix_arry, order_filled)

    # Need to record the number of nodes visited, shortest/longest path, average time to csv file or DB



# To search down add 6 to the array position
# To search left subtract 1 to the array position
# To search right add 1 to the array
# To search up subtract 6 from the array
# The above searches the neighborhood Up, Down, Left, Right


