import numpy as np

# Variable checks if the order is completed or not
order_filled = False
# Size of the array is established
rows, cols = (6, 6)
# Build the warehouse matrix 6 x 6
matrix_arry = [[0]*cols]*rows
#--matrix_arry = [[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18],
   #--            [19,20,21,22,23,24], [25,26,27,28,29,30], [31,32,33,34,35,36]]

# To search down add 6 to the array position
# To search left subtract 1 to the array position
# To search right add 1 to the array
# To search up subtract 6 from the array
# The above searches the neighborhood Up, Down, Left, Right

for row in matrix_arry:
    print(row)

