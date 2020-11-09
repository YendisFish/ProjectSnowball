import os

try:
    os.system('shutdown now')
except:
    print('Failed to shutdown system!')