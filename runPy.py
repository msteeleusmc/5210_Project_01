import subprocess
import sys
import pandas as pd

print("Running main.py...\n\n")
for scriptInstance in range(1,1000):
    #sys.stdout = open('results.csv', 'w')
    subprocess.check_call(['python', 'main.py'])

# Create dataset
csv_data = pd.read_csv("project_01.csv")

min_value = csv_data.min(axis=0)
max_value = csv_data.max(axis=0)

print("Shortest Path:\n", min_value)
print("\n\nLongest Path:\n", max_value)

# Calculate Average

# Show the program is completed
print("\nProgram completed")

# Print the results


