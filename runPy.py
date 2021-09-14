import subprocess
import sys
import pandas as pd
import csv

print("Running main.py...\n")
print("Beginning Layout 1\n")
# =======================================================================
#                           Layout 1
# =======================================================================
for scriptInstance in range(1,1000):
    #sys.stdout = open('results.csv', 'w')
    subprocess.check_call(['python', 'main.py'])

# Create dataset
csv_data = pd.read_csv("layout_01.csv")

# Sort the data into new csv file
sorted_data = csv_data.sort_values(by=["List Size"], ascending=True)
sorted_data.to_csv('sorted_01.csv', index=False)
# Create dataframe of the sorted csv file
csv_data = pd.read_csv("sorted_01.csv")

# Record the min and max number of nodes visited for all 1000 iterations
min_value = csv_data['List Size'].iloc[0]
max_value = csv_data['List Size'].iloc[-1]
# Record the actual paths taken
min_path = csv_data['Nodes Visited'].iloc[0]
max_path = csv_data['Nodes Visited'].iloc[-1]

# Record path scores
# Use formula (35-n)*(-1)+n*3
# = 35+4n
min_score = csv_data['Brute Force Score'].iloc[0]# 35 + 4*min_value
max_score = csv_data['Brute Force Score'].iloc[-1]# 35 + 4*max_value

# Record the average of the scores column
score_average = csv_data['Brute Force Score'].mean()

# Print to terminal, all of the answers
print("****** LAYOUT 1 ******")
print("Average Brute Force Score:\n", score_average)
print("Average Final Score:\n")
print("\nShortest Path:\n", min_value)
print(min_path)
print("Brute Force Score:\n", min_score)
print("Actual Score:\n")

print("\nLongest Path:\n", max_value)
print(max_path)
print("Brute Force Score:\n", max_score)
print("Actual Score:\n")

print("\nBeginning Layout 2\n")
# =======================================================================
#                           Layout 2
# =======================================================================

# Create dataset
csv_data = pd.read_csv("layout_02.csv")

# Sort the data into new csv file
sorted_data = csv_data.sort_values(by=["List Size"], ascending=True)
sorted_data.to_csv('sorted_02.csv', index=False)
# Create dataframe of the sorted csv file
csv_data = pd.read_csv("sorted_02.csv")

# Record the min and max number of nodes visited for all 1000 iterations
min_value = csv_data['List Size'].iloc[0]
max_value = csv_data['List Size'].iloc[-1]
# Record the actual paths taken
min_path = csv_data['Nodes Visited'].iloc[0]
max_path = csv_data['Nodes Visited'].iloc[-1]

# Record path scores
# Use formula (35-n)*(-1)+n*3
# = 35+4n
min_score = csv_data['Brute Force Score'].iloc[0]# 35 + 4*min_value
max_score = csv_data['Brute Force Score'].iloc[-1]# 35 + 4*max_value

# Record the average of the scores column
score_average = csv_data['Brute Force Score'].mean()

# Print to terminal, all of the answers
print("****** LAYOUT 2 ******")
print("Average Brute Force Score:\n", score_average)
print("Average Final Score:\n")
print("\nShortest Path:\n", min_value)
print(min_path)
print("Brute Force Score: ", min_score)
print("Actual Score:\n")

print("\nLongest Path:\n", max_value)
print(max_path)
print("Brute Force Score: ", max_score)
print("Actual Score:\n")

# Show the program is completed
print("\nProgram completed")

# Print the results


