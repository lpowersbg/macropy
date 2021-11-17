#import xml.etree.ElementTree as XML
import xml.etree.ElementTree as ET
import time
import chymac

con = "PlayClockIn"
coff = "PlayClockOut"
playClock = "nothing"


while(1):
    score = ET.parse("I:\\2019 Sports\\Databases\\Scorehub\\Bug Live Data.xml")
    root = score.getroot()
    clock = int(root.find('playclock').text)
    if clock <= 9:
        if playClock != "on":
            chymac.chysend(con)
            playClock = "on"
    elif clock > 9:
        if playClock != "off":
            chymac.chysend(coff)
            playClock = "off"
    time.sleep(1)