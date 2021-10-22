import xml.etree.ElementTree as ET
import time
import chymac

con = "PlayClockOn"
coff = "PlayClockOff"
score = ET.parse("I:\\2019 Sports\\Databases\\Scorehub\\Bug Live Data.xml")
root = score.getroot()

while(1):
    clock = root.find('playclock').text
    if clock <= 10 & clock > 0: chymac.chysend(con)
    if clock <= 0: 
        time.sleep(2)
        chymac.chysend(coff)
    if clock > 10: chymac.chysend(coff)
    time.sleep(1)