import telnetlib
import time

msg2 = "\r\n"
ip = '127.0.0.1'
port = 48873

def chysend(msg):
    msg1 = ("E\\" + msg + "\\\\")
    tn = telnetlib.Telnet(bytes(ip, encoding='utf-8'), port)
    tn.write(msg1.encode('utf-8'))
    tn.write(msg2.encode('utf-8'))
    time.sleep(0.05)
