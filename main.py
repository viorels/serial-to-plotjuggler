import socket
import json
import serial
from math import sin, cos

UDP_IP = "127.0.0.1"
UDP_PORT = 9870
testvar = 0.0
msg = {}
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

s = serial.Serial('/dev/ttyUSB0', 115200)


def test():
    global testvar
    x = sin(testvar / 10)
    x1 = cos(testvar / 10)
    x2 = cos(testvar / 10) + 2
    x = x.__str__() + ',' + x1.__str__() + ',' + x2.__str__()
    s.write(bytes(x + '\n\r', encoding='ascii'))
    testvar += 0.01


while 1:
    test()
    line = s.readline()
    line = line.split(bytes(',', encoding='ascii'))
    num_list = []
    for o in line:
        num_list.append(float(o))
    msg = {'var': num_list}
    sock.sendto(bytes(json.dumps(msg), encoding="utf-8"), (UDP_IP, UDP_PORT))
