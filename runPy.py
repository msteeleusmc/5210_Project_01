import subprocess
import sys
import pandas as pd
import csv

print("Running main.py...\n\n")

for scriptInstance in range(1,1000):
    #sys.stdout = open('results.csv', 'w')
    subprocess.check_call(['python', 'main.py'])

# Create dataset
csv_data = pd.read_csv("project_01.csv")

# Sort the data into new csv file
sorted_data = csv_data.sort_values(by=["List Size"], ascending=True)
sorted_data.to_csv('sorted.csv', index=False)
# Create dataframe of the sorted csv file
csv_data = pd.read_csv("sorted.csv")

# Record the min and max number of nodes visited for all 1000 iterations
min_value = csv_data['List Size'].iloc[0]
max_value = csv_data['List Size'].iloc[-1]
# Record the actual paths taken
min_path = csv_data['Nodes Visited'].iloc[0]
max_path = csv_data['Nodes Visited'].iloc[-1]

# Record path scores
# Use formula (35-n)*(-1)+n*3
# = 35+4n
min_score = csv_data['Score (35 + 4n)'].iloc[0]# 35 + 4*min_value
max_score = csv_data['Score (35 + 4n)'].iloc[-1]# 35 + 4*max_value

# Record the average of the scores column
score_average = csv_data['Score (35 + 4n)'].mean()

# Print to terminal, all of the answers
print("****** LAYOUT 1 ******")
print("Average Score:\n", score_average)
print("\nShortest Path:\n", min_value)
print(min_path)
print("Score: ", min_score)

print("\nLongest Path:\n", max_value)
print(max_path)
print("Score: ", max_score)

# Show the program is completed
print("\nProgram completed")

# Print the results


