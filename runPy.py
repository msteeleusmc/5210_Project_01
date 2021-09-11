import subprocess
import sys

for scriptInstance in range(1,1000):
    sys.stdout = open('result%s.txt' % scriptInstance, 'w')
    subprocess.check_call(['python', 'main.py'], \
                          stdout=sys.stdout, stderr=subprocess.STDOUT)