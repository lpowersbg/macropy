import xml.etree.ElementTree as ET
import time
import chymac

macro = "PlayClock"
score = ET.parse("I:\\2019 Sports\\Databases\\Scorehub\\Bug Live Data.xml")
root = score.getroot()

while(1):
    clock = root.find('playclock').text)
    if clock < 10 & clock > 0: chymac.chysend(macro)
    time.sleep(1)