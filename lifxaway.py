import lazylights
import time
import os
import pyping
import sys
import math
import binascii
from colour import Color


#------------------------------------------------------------------------------------------------------------
# I use this to manually create a bulb using IP and MAC address.
def createBulb(ip, macString, port = 56700):
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
#------------------------------------------------------------------------------------------------------------




# This is the Main loop
#while True:

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0



#These are my two bulbs. I get the values ahead of time from my router info page
myBulb1 = createBulb('10.0.0.4','D0:73:D5:00:C1:4F')  #Bulb for left  side of screen
#myBulb2 = createBulb('10.10.10.1','XX:XX:XX:XX:XX:XX')  #Bulb for right side of screen
myPhone = "10.0.0.11"
#lazylights requires a 'set' of bulbs as input so I put each one in its own set
bulbs1=[myBulb1]


while True:
    
    # test call
    status = (ping("10.0.0.11"))

    if status==True:
        print "***True"
        c = Color("green")
        print c
        lazylights.set_state(bulbs1,c.hue*360,(c.saturation),c.luminance,3500,(500),False)

    if status==False:
        c = Color("yellow")
        print "***False"
        lazylights.set_state(bulbs1,c.hue*360,(c.saturation),c.luminance,3500,(500),False)


   # lazylights.set_state(bulbs1,c.hue*360,(c.saturation),c.luminance,KELVIN,(DURATION),False)
