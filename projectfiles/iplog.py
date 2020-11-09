import os
import subprocess

try:
    print('Linux Try')
    ip = os.system('sudo wget http://ipecho.net/plain -O - -q > iplog.txt')
    print(ip)
except:
    print('Linux Try Failed')
