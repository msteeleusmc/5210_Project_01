import random
import time
import csv
import os

# -----------------------------------------------------------------------------------
#                            Global Function
# -----------------------------------------------------------------------------------
def buildWareHouseOne(matrix_arry):
    # Assign shelf locations
    matrix_arry = layoutOne(matrix_arry)
    return matrix_arry

def buildWareHouseTwo(matrix_arry):
    # Assign shelf locations
    matrix_arry = layoutTwo(matrix_arry)
    return matrix_arry

def layoutOne(matrix_arry):
    # Shelf position at 3, 8, 11, 13, 15, 17, 20, 27, 30, 34
    matrix_arry = [[1, 2, 'D', 4, 5, 6], [7, 'A', 9, 10, 'G', 12], ['E', 14, 'B', 16, 'I', 18],
                   [19, 'C', 21, 22, 23, 24], [25, 26, 'F', 28, 29, 'H'], [31, 32, 33, 'J', 35, 36]]

    return matrix_arry

def layoutTwo(matrix_arry):
    # Shelf position for layout 2
    matrix_arry = [[1, 2, 'A', 4, 'P', 6], ['D', 8, 'B', 10, 'M', 12], ['E', 14, 'F', 16, 'K', 18],
                   ['C', 20, 'H', 22, 23, 'O'], ['G', 26, 'J', 28, 29, 'Q'], ['I', 32, 33, 34, 'N', 36]]

    return matrix_arry

def fillOrder(shelf_list):
    # Make a new order list
    new_order = []
    # For loop will make a random range to assign list elements
    for i in range(0,random.randint(1,len(shelf_list)-1)):
        new_order.append(shelf_list[i])

    # Shuffle the order of the list
    random.shuffle(new_order)

    return new_order

def searchWareHouseOne(matrix_arry, status, path_list):
    #begin search
    shelf_list = ['A','B','C','D','E','F','G','H','I','J']
    # Random order generator
    order = fillOrder(shelf_list)
    row = 0
    col = 0

    # Change while loop back to status check once traversal complete
    while status is False:
        status, row, col = searchNeighbors(matrix_arry, row, col, order, status, path_list)

    return status

def searchWareHouseTwo(matrix_arry, status, path_list):
    #begin search
    shelf_list = ['A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q']
    # Random order generator
    order = fillOrder(shelf_list)
    row = 0
    col = 0

    # Change while loop back to status check once traversal complete
    while status is False:
        status, row, col = searchNeighbors(matrix_arry, row, col, order, status, path_list)

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

def searchNeighbors(matrix_arry, row, col, shelf_list, status, path_list):
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
        # Check if shelfs in order
        for j in directionList:
            for i in shelf_list:
                if j == i:
                    # Remove all integers
                    directionList = [x for x in directionList if not isinstance(x, int)]

        # Remove all integers
        #directionList = [x for x in directionList if not isinstance(x, int)]
        # assign the new position based on random choice
        new_position = random.choice(directionList)

        # Edit the list of remaining shelves
        for i in shelf_list:
            if new_position == i:
                shelf_list.remove(i)

        # Update the path list to track visited nodes
        path_list.append(new_position)

        # Assign new row and col
        for i in range(0,5):
            for j in range(0,5):
                if new_position == matrix_arry[i][j]:
                    row = i
                    col = j

        # Update the status to True if no shelves remain in list
        if len(shelf_list) == 0:
            return True, row, col;

        # Status remains False if shelves are still in list
        return False, row, col;
    else:
        # Assign the position based on random choice
        new_position = random.choice(directionList)

        for i in range(0, 5):
            for j in range(0, 5):
                if new_position == matrix_arry[i][j]:
                    row = i
                    col = j

        # Add the node to the path list
        path_list.append(new_position)

        # Return status is False to continue loop
        return False, row, col;

# -----------------------------------------------------------------------------------
#                         Executes Main Program
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # Start timer
    start = time.time()

    # Variable checks if the order is completed or not
    order_filled = False

    # Size of the array is established
    rows, cols = (6, 6)

    # =======================================================================
    #                           Layout 1
    # =======================================================================

    # Create a list to store the path
    path_list = []

    # Build the warehouse matrix 6 x 6
    matrix_arry = [[-1] * cols] * rows
    matrix_arry = buildWareHouseOne(matrix_arry)

    # This will be the end as the order status will be changed to True
    order_filled = searchWareHouseOne(matrix_arry, order_filled, path_list)

    # End timer
    end = time.time()

    # Final runtim is end - start
    final_runtime = (end - start)
    # Format time to 10 decimal places
    final_runtime = "Run Time: {:.10f}".format(final_runtime)

    # Calculate scores (35-n)*(-1)+n*3=35+4*n
    # = 35 + 4n
    final_score = 35 + 4*len(path_list)

    # Write to csv file
    data = [len(path_list), final_runtime, path_list, final_score]
    # Make csv header
    header = ['List Size', 'Run Time', 'Nodes Visited', 'Brute Force Score']
    # File path
    csv_path = 'layout_01.csv'

    if os.path.exists(csv_path):
        with open('layout_01.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()
    else:
        with open('layout_01.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer. writerow(header)
            writer.writerow(data)
            f.close()

    #=======================================================================
    #                           Layout 2
    #=======================================================================
    # Start timer
    start = time.time()

    # Variable checks if the order is completed or not
    order_filled2 = False

    # Clear path list
    path_list2 = []

    # Build the warehouse matrix 6 x 6
    matrix_arry = []
    matrix_arry = [[-1] * cols] * rows
    matrix_arry = buildWareHouseTwo(matrix_arry)

    # This will be the end as the order status will be changed to True
    order_filled2 = searchWareHouseTwo(matrix_arry, order_filled2, path_list2)

    # End timer
    end = time.time()

    # Final runtim is end - start
    final_runtime = (end - start)
    # Format time to 10 decimal places
    final_runtime = "Run Time: {:.10f}".format(final_runtime)

    # Calculate scores (35-n)*(-1)+n*3=35+4*n
    # = 35 + 4n
    final_score = 35 + 4 * len(path_list2)

    # Write to csv file
    data = [len(path_list2), final_runtime, path_list2, final_score]
    # Make csv header
    header = ['List Size', 'Run Time', 'Nodes Visited', 'Brute Force Score']
    # File path
    csv_path = 'layout_02.csv'

    if os.path.exists(csv_path):
        with open('layout_02.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()
    else:
        with open('layout_02.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)
            f.close()

# To search down add 6 to the array position
# To search left subtract 1 to the array position
# To search right add 1 to the array
# To search up subtract 6 from the array
# The above searches the neighborhood Up, Down, Left, Right