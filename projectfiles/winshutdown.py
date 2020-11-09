import os

try:
    os.system('shutdown /s')
except:
    while True:
        print('Failed to shutdown system!')