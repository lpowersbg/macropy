import xml.etree.ElementTree as xml
import time
from datetime import datetime
import chymac

macro1 = "PlayClockIn"
macro2 = "PlayClockOut"
thresh = 10

xmlpath = "I:\\2019 Sports\\Databases\\Scorehub\\Bug Live Data.xml"
xmlpathtest = "C:\\Users\\ChyronHego\\Desktop\\Bug Live Data.xml"

pcin = False

def timestamp():
    dto = datetime.now()
    return(dto.strftime("[%Y%m%d %H:%M:%S]"))

print(timestamp(), 'Clock-O-Matic 5000 has begun!')

while(True):
    try:
        stats = xml.parse(xmlpath)
    except:
        print(timestamp(), 'Stats XML failed to open :(')
    try:
        root = stats.getroot()
    except:
        print(timestamp(), 'Invalid XML format')
    try:
        rawclock = root[9].text
    except:
        print(timestamp(), 'Entry 9 (Playclock) not found. The world weeps.')
    try:
        clock = int(root[9].text)
    #    print(pcin)
    #    print(clock)
        if(clock <= thresh and clock > 0 and pcin == False):
            chymac.chysend(macro1)
            pcin = True
        elif(clock <= 0 or clock > thresh and pcin == True):
            chymac.chysend(macro2)
            pcin = False
    except:
    #    pass
        print(timestamp(), 'No Data in Clock Field')
    time.sleep(0.5)

