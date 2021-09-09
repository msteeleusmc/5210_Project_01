import numpy as np

# -----------------------------------------------------------------------------------
#                            Global Function
# -----------------------------------------------------------------------------------
def buildWareHouse(matrix_arry):
    # Assign shelf locations
    matrix_arry = layoutOne(matrix_arry)
    return matrix_arry

def layoutOne(matrix_arry):
    # Shelf position at 3, 8, 11, 13, 15, 17, 20, 27, 30, 34
    matrix_arry = [[-1, -1, 'D', -1, -1, -1], [-1, 'A', -1, -1, 'G', -1], ['E', -1, 'B', -1, 'I', -1],
                   [-1, 'C', -1, -1, -1, -1], [-1, -1, 'F', -1, -1, 'H'], [-1, -1, -1, 'J', -1, -1]]

    return matrix_arry

def fillOrder(matrix_arry, order, status):
    pass
    # Eventually run this until status is True because order is filled

def searchWareHouse(current_position, matrix_arry):
    pass
    # Use this to search for shelves


# -----------------------------------------------------------------------------------
#                         Executes Main Program
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # Variable checks if the order is completed or not
    order_filled = False

    # Size of the array is established
    rows, cols = (6, 6)

    # Build the warehouse matrix 6 x 6
    matrix_arry = [[-1] * cols] * rows
    matrix_arry = buildWareHouse(matrix_arry)

    # Take customer order
    customer_order = "fill order here"

    # Fulfill Order
    order_filled = fillOrder(matrix_arry, customer_order, order_filled)

    for row in matrix_arry:
        print(row)


# To search down add 6 to the array position
# To search left subtract 1 to the array position
# To search right add 1 to the array
# To search up subtract 6 from the array
# The above searches the neighborhood Up, Down, Left, Right


