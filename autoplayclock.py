import xml.etree.ElementTree as xml
import time
import chymac

macro1 = "PlayClockIn"
macro2 = "PlayClockOut"

xmlpath = "I:\\2019 Sports\\Databases\\Scorehub\\Bug Live Data.xml"
xmlpathtest = "C:\\Users\\ChyronHego\\Desktop\\Bug Live Data.xml"

pcin = False

while(True):
    stats = xml.parse(xmlpath)
    root = stats.getroot()
    rawclock = root[9].text
    try:
        clock = int(root[9].text)
    #    print(pcin)
        print(clock)
        if(clock <= 10 and clock > 0 and pcin == False):
            chymac.chysend(macro1)
            pcin = True
        elif(clock == 0 or clock > 10 and pcin == True):
            chymac.chysend(macro2)
            pcin = False
    except:
    #    pass
        print('noclock')
    time.sleep(1)