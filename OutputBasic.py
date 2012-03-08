import threading
import time

#this function is called repeatedly updating the DMX values, but it is responsible for the actual DMX output loop thread
dmx_levels = []
#for i in range(0, 511):
#    dmx_levels.append(0)
    
enabled = True

def SetDMX(dmx):
    global dmx_levels
    dmx_levels = dmx

def enable():
    global enabled
    enabled = True
    dmx_thread = threading.Thread(target=send_dmx)
    dmx_thread.daemon = True
    dmx_thread.start()
    
def disable():
    global enabled
    enabled = False

def send_dmx():
#this is where we would actually send the data to the DMX device in a timed loop defined below.
    global enabled, dmx_levels
    while enabled:
#        for d in range(0,512):
##            print "DMX: " + str(d) + " - " + str(dmx_levels[d])
        time.sleep(1)

