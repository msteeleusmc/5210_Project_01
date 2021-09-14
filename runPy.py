import subprocess
import sys
import pandas as pd
import csv

def calculateScore():
    pass

print("Running main.py...\n\n")
for scriptInstance in range(1,10):
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

# Print to terminal, all of the answers
print("Shortest Path:\n", min_value)
print(min_path)
print("\nLongest Path:\n", max_value)
print(max_path)

# Calculate Average


# Show the program is completed
print("\nProgram completed")

# Print the results


