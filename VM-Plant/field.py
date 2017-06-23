#!/usr/bin/python
from config import *
from itertools import count
from pymodbus.client.sync import ModbusTcpClient
import random as rd
from random import *
import numpy as np
import time
import sys
import csv
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

client = ModbusTcpClient(FIELD_IP, FIELD_PORT)
client.connect()

#opc_client = ModbusTcpClient(OPC_IP,OPC_PORT)
#opc_client.connect()

client.write_register(SumpLow, 1.0)
client.write_register(ValvePos_S, 1.0)
client.write_register(ValvePos_CT, 0.0)
client.write_register(Pump,  0.0)
client.write_register(LevelBoiler, 20.0)
client.write_register(TempBoiler, 30.0)
client.write_register(Heater,  0.0)
client.write_register(SteamOutlet, 0.0) 
client.write_register(CTankLevel,20.0)
client.write_register(SafeValve,0.0)

SumpLow        = float(client.read_holding_registers(SumpLow, 1).registers[0])
valve1_1       = float(client.read_holding_registers(ValvePos_S, 1).registers[0])
valve1_2       = float(client.read_holding_registers(ValvePos_CT, 1).registers[0])
pump           = client.read_holding_registers(Pump, 1).registers[0]
levelB1        = client.read_holding_registers(LevelBoiler, 1).registers[0]
tempB1         = client.read_holding_registers(TempBoiler, 1).registers[0]
heater   	   = client.read_holding_registers(Heater, 1).registers[0]
valve2   	   = client.read_holding_registers(SteamOutlet, 1).registers[0]
level2   	   = client.read_holding_registers(CTankLevel, 1).registers[0]
safety_valve   = client.read_holding_registers(SafeValve, 1).registers[0]

#--------------Logic of Filling the SUMP continuously-----------
value_SumpLow=20
data_lst=[]
#Simulation will run according to the sim time
current_lst=[]
for i in range(0,SIM_TIME):

	while  True:
		
		
		for i in range(0,50):
			if i <= value_SumpLow:
				SumpLow=1 #low level feedback becomes 1
				
			else:
				SumpLow=0 #low level feedback becomes 0
		break        	
	#Segment of Code of Operation of plant by checking pump logic------

	value_SumpLow=20  #Initializing low level set point of sump
	value_levelB1=20  #constant for low level of boiler
	value_CTankLow=20 #constant for low level of condensed tank 
	valve1_1=1        #By default open as for a 3 way valve one side should be opened
	value_tempB1=30
	if SumpLow == 0:            
		valve1_1=1
	elif SumpLow==1 and level2==0:
		valve1_1=0
	
	#Computing pump current
	power=2000
	current_lst=[]
	#for x in range(0,60):
	fluc_vol=rd.randrange(180,240)
	current=power/fluc_vol #I=P/V
	current_lst.append(current)
	current_data=np.array(current_lst)


	fluc_v=fluc_vol         #flutuating voltage
	

	startTime=0
	duration=0
	i=0
	#Noting Pump operation time of on and not on
	
	if 200 <= fluc_v and fluc_v <= 220 and (valve1_1 == 1 or valve1_2 == 1):
		pump=1
		if startTime==0:
			startTime=time.time()		
	if levelB1 >= value_levelB1: #(and 150<=tempB1<=20):)
			pump=0
			time_list=[]
			time.sleep(rd.randrange(0,4))
			stopTime=time.time()
			for i in range(0,SIM_TIME):
				duration=stopTime-startTime
			 	time_list.append(duration)

			# print duration 
	
	else:
		pump=0
		stopTime=0
		duration=stopTime-startTime
	
	def boileraction(): #Function turns on the heater when condition is met
		if levelB1 >= value_levelB1 and tempB1 >= value_tempB1:
			heater=1
		if levelB1 >=544:
			heater=0
		return heater
	
	def boileraction1(tempB1): #Function Computes the Temperature of boiler
		if levelB1 >=value_levelB1 and tempB1 >= value_tempB1:
			tempB1=tempB1=tempB1+(3.0*heat_coefficient)/(3.0*levelB1)
		if levelB1 >=544:
			tempB1=tempB1-1
		if levelB1 >= 990:
			valve2=0
			valve1_2=0
			valve1_1=0
			safety_valve=1

		return tempB1 
	
	def boileraction2(levelB1): #Function Computes the Level of Boiler
		if levelB1 >= value_levelB1 and tempB1 >= value_tempB1:
			levelB1=levelB1+4
		if levelB1 >=990:
			levelB1=990

		return levelB1
	
	if tempB1 >= 112 and tempB1 <= 130: 
		level2=level2+10
		valve2=1
		safety_valve=0
	
	if tempB1 >= 90 and tempB1 <= 130 and levelB1 >= 990:
		safety_valve=1 
		valve1_1=0
		valve1_2=0
		valve2=0
		level2=860


	if tempB1 > 130 and tempB1 < 170:
		level2=level2+10
		valve2=1
		valve1_1=1
		valve1_2=0
		safety_valve=0
	
	if tempB1 >= 170 and tempB1 <= 200:
		safety_valve=1
		valve2=0
		level2=level2-4
		valve1_2=1
		valve1_1=0	
	
	if tempB1 > 200:
		
		valve1_1=0
		


	heater=boileraction()
	tempB1=boileraction1(tempB1)
	levelB1=boileraction2(levelB1)


	client.write_register(SumpLow, SumpLow)
	client.write_register(ValvePos_S, valve1_1)
	client.write_register(ValvePos_CT, valve1_2)
	client.write_register(Pump, pump)
	client.write_register(LevelBoiler, levelB1)
	client.write_register(TempBoiler, tempB1)
	client.write_register(Heater, heater)
	client.write_register(SteamOutlet, valve2)
	client.write_register(CTankLevel, level2)
	client.write_register(SafeValve, safety_valve)
	
	
	
	cSumplow=SumpLow
	# data_lst.append(cSumplow)
	cvalv1_1=valve1_1
	# data_lst.append(cvalv1_1)
	cvalv1_2=valve1_2
	# data_lst.append(cvalv1_2)
	cpump=pump
	# data_lst.append(cpump)
	clevb=levelB1
	# data_lst.append(clevb)
	ctemb=tempB1
	# data_lst.append(ctemb)
	cheat=heater
	# data_lst.append(cheat)
	cvalve2=valve2
	# data_lst.append(cvalve2)
	ctankl=level2
	# data_lst.append(ctankl)
	csaftety=safety_valve
	# data_lst.append(csaftety)
	data_lst.append([cSumplow,cvalv1_1,cvalv1_2,cpump,clevb,ctemb,cheat,cvalve2,ctankl,csaftety])



	# print data_lst
	printvalues(SumpLow, valve1_1, valve1_2, pump, levelB1, tempB1, heater, valve2, level2,safety_valve)
		#sys.exit()
da=np.array(data_lst)
out = open('out.csv', 'w')
for row in data_lst:
    for column in row:
        out.write('%d,' % column)
    out.write('\n')
out.close()

print current_lst
# print data_lst
# print time_list
# print da
# print field_data
