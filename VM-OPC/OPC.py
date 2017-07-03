#!/usr/bin/python
from config import *
from itertools import count
from pymodbus.client.sync import ModbusTcpClient
import random as rd
from random import *
import numpy as np
import time
import sys
import time
import logging
import os
import subprocess

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

field_client = ModbusTcpClient(FIELD_IP, FIELD_PORT)
field_client.connect()
opc_client = ModbusTcpClient(OPC_IP, OPC_PORT)
opc_client.connect()

data_lst=[]
#Simulation will run according to the sim time
def openIDS_TrainNN():
    try:
        subprocess.call(["xdotool key ctrl+t"])
        subprocess.call(["python","ids_train.py"])
    except ImportError:
        print 'Command not executed'
        os.exit(1)

#time.sleep(2)
for i in range(0,SIM_TIME):
	time.sleep(2)
	SumpLow      = field_client.read_holding_registers(SumpLow, 1).registers[0] #float(field_client.read_holding_registers(SumpLow, 1).registers[0])
	valve1_1     = float(field_client.read_holding_registers(ValvePos_S, 1,).registers[0])
	valve1_2     = float(field_client.read_holding_registers(ValvePos_CT, 1).registers[0])
	pump         = field_client.read_holding_registers(Pump, 1).registers[0]
	levelB1      = field_client.read_holding_registers(LevelBoiler, 1).registers[0]
	tempB1       = float(field_client.read_holding_registers(TempBoiler, 1).registers[0])
	heater       = field_client.read_holding_registers(Heater, 1).registers[0]
	valve2       = field_client.read_holding_registers(SteamOutlet, 1).registers[0]
	level2       = field_client.read_holding_registers(CTankLevel, 1).registers[0]
	safety_valve = field_client.read_holding_registers(SafeValve, 1).registers[0]

	cSumplow=float(SumpLow)
	cvalv1_1=float(valve1_1)
	cvalv1_2=float(valve1_2)
	cpump=float(pump)
	clevb=float(levelB1)
	ctemb=float(tempB1)
	cheat=float(heater)
	cvalve2=float(valve2)
	ctankl=float(level2)
	csaftety=float(safety_valve)
	
	data_lst.append([cSumplow,cvalv1_1,cvalv1_2,cpump,clevb,ctemb,cheat,cvalve2,ctankl,csaftety])
	printvalues(SumpLow, valve1_1, valve1_2, pump, levelB1, tempB1, heater, valve2, level2)
	
print "Data Logged..."
Data = np.array(data_lst,"\n")
np.save("mal_test_data", Data)

out = open('mal_log.csv', 'w')
for row in data_lst:
    for column in row:
        out.write('%.2f,' % column)
    out.write('\n')
out.close()
#openIDS_TrainNN()