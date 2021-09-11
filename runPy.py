import subprocess
import sys

for scriptInstance in range(1,1001):
    sys.stdout = open('results.txt', 'w')
    subprocess.check_call(['python', 'main.py'], \
                          stdout=sys.stdout, stderr=subprocess.STDOUT)