from config import *
from pymodbus.client.sync import ModbusTcpClient
import random as rd
from random import *
import numpy as np
import time
import sys

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

client = ModbusTcpClient(FIELD_IP, FIELD_PORT)
client.connect()


power=2000
current=[power//rd.randrange(180,240) for x in range(0,60)]
current_data=np.array(current)

client.write_register(HL, 90.0)
client.write_register(LL, 20.0)
client.write_register(V1_1, 0.0)
client.write_register(V1_2, 0.0)
client.write_register(P,  0.0)
client.write_register(L1, 10.0)
client.write_register(T1, 30.0)
client.write_register(H,  0.0)
client.write_register(V2, 0.0)
client.write_register(L2, 10.0)
client.write_register(L2L,10.0)

print "Simulation will start when the time is 0, 25, 50 ,75"
to = 0
while 1:
    toot = int(time.time())%100
    if to == toot - 1:
        print toot
    to = toot
    # print to
    if to == 0 or to == 25 or to == 50 or to == 75:
        break
#while True:
hl = float(client.read_holding_registers(HL, 1).registers[0])
ll = float(client.read_holding_registers(LL, 1).registers[0])
v1_1 = float(client.read_holding_registers(V1_1, 1).registers[0])
v1_2 = float(client.read_holding_registers(V1_2, 1).registers[0])
p  = client.read_holding_registers(P, 1).registers[0]
l1 = client.read_holding_registers(L1, 1).registers[0]
t1 = client.read_holding_registers(T1, 1).registers[0]
h  = client.read_holding_registers(H, 1).registers[0]
v2 = client.read_holding_registers(V2, 1).registers[0]
l2 = client.read_holding_registers(L2, 1).registers[0]
l2l= client.read_holding_registers(L2L, 1).registers[0]




client.write_register(HL, hl)
client.write_register(LL, ll)
client.write_register(V1_1, v1_1)
client.write_register(V1_2, v1_2)
client.write_register(P, p)
client.write_register(L1, l1)
client.write_register(T1, t1)
client.write_register(H, h)
client.write_register(V2, v2)
client.write_register(L2, l2)
client.write_register(L2L, l2l)




printvalues("field", hl, ll, v1_1, v1_2, p, l1, t1, h, v2, l2, l2l)
sys.exit()