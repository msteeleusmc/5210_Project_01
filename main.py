import random

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

    # Change while loop back to status check once traversal complete
    while status is False:
        if col <= 5:
            status = searchNeighbors(matrix_arry, row, col, shelf_list, status)
            col += 1
        elif row > 5:
            row = 0
            col = 0
        else:
            row += 1
            col = 0

    print("Order filled")
    return status


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
    # temp variable starts as -1 in case we try to move out of bounds.
    # if row is not 5 then the temp variable will return new value.
    temp = -1
    if row < 5:
        temp = matrix_array[row + 1][col]
        return temp
    else:
        return temp

def searchLeft(matrix_array, row, col):
    # temp variable starts as -1 in case we try to move out of bounds.
    # if col is not 0 then the temp variable will return new value.
    temp = -1
    if col > 0 and row <= 5:
        temp = matrix_array[row][col -1]
        return temp
    else:
        return temp

def searchRight(matrix_array, row, col):
    # temp variable starts as -1 in case we try to move out of bounds.
    # if col is not 5 then the temp variable will return new value.
    temp = -1
    if col < 5 and row <= 5:
        temp = matrix_array[row][col + 1]
        return temp
    else:
        return temp

def searchNeighbors(matrix_arry, row, col, shelf_list, status):
    # Call direction functions to check 4 neighbors and store values
    mUp = searchUp(matrix_arry, row, col)
    mDown = searchDown(matrix_arry, row, col)
    mLeft = searchLeft(matrix_arry, row, col)
    mRight = searchRight(matrix_arry, row, col)

    # Make a list of values if > -1.
    directionList = []
    if mUp != -1:
        directionList.append(mUp)
    if mDown != -1:
        directionList.append(mDown)
    if mLeft != -1:
        directionList.append(mLeft)
    if mRight != -1:
        directionList.append(mRight)

    # Check if any elements in list is a string aka shelf
    char_found = False
    for i in directionList:
        if isinstance(i, str):
            char_found = True
            break

    # Remove integers if shelves are in the list
    if char_found is True:
        directionList = [x for x in directionList if not isinstance(x, int)]
        new_position = random.choice(directionList)

        for i in shelf_list:
            if new_position == i:
                shelf_list.remove(i)

        print(shelf_list)

        if len(shelf_list) == 0:
            return True

        return False
    else:
        new_position = random.choice(directionList)
        return False

    print("current position: ", new_position)



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