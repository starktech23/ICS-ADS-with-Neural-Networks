#!/usr/bin/python
from config import *
from itertools import count
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

field_client = ModbusTcpClient(FIELD_IP, FIELD_PORT)
field_client.connect()
opc_client = ModbusTcpClient(OPC_IP, OPC_PORT)
opc_client.connect()

#

# SumpLow  = opc_client.read_holding_registers(SumpLow, 1).registers[0] #float(field_client.read_holding_registers(SumpLow, 1).registers[0])
# valve1_1 = float(opc_client.read_holding_registers(ValvePos_S, 1,).registers[0])
# valve1_2 = float(opc_client.read_holding_registers(ValvePos_CT, 1).registers[0])
# pump     = opc_client.read_holding_registers(Pump, 1).registers[0]
# levelB1  = opc_client.read_holding_registers(LevelBoiler, 1).registers[0]
# tempB1   = opc_client.read_holding_registers(TempBoiler, 1).registers[0]
# heater   = opc_client.read_holding_registers(Heater, 1).registers[0]
# valve2   = opc_client.read_holding_registers(SteamOutlet, 1).registers[0]
# level2   = opc_client.read_holding_registers(CTankLevel, 1).registers[0]
#--------------Logic of Filling the SUMP continuously-----------
value_SumpLow=20

#Simulation will run according to the sim time
for i in range(0,SIM_TIME):
	SumpLow  = field_client.read_holding_registers(SumpLow, 1).registers[0] #float(field_client.read_holding_registers(SumpLow, 1).registers[0])
	valve1_1 = float(field_client.read_holding_registers(ValvePos_S, 1,).registers[0])
	valve1_2 = float(field_client.read_holding_registers(ValvePos_CT, 1).registers[0])
	pump     = field_client.read_holding_registers(Pump, 1).registers[0]
	levelB1  = field_client.read_holding_registers(LevelBoiler, 1).registers[0]
	tempB1   = field_client.read_holding_registers(TempBoiler, 1).registers[0]
	heater   = field_client.read_holding_registers(Heater, 1).registers[0]
	valve2   = field_client.read_holding_registers(SteamOutlet, 1).registers[0]
	level2   = field_client.read_holding_registers(CTankLevel, 1).registers[0]
	




	printvalues(SumpLow, valve1_1, valve1_2, pump, levelB1, tempB1, heater, valve2, level2)
	# while  True:
		
		
	# 	for i in range(0,50):
	# 		if i <= value_SumpLow:
	# 			SumpLow=1
				
	# 		else:
	# 			SumpLow=0
	# 	break        	
	# #Segment of Code of Operation of plant by checking pump logic------

	# value_SumpLow=20  #constant for low level sensor of sump
	# value_levelB1=20  #constant for low level of boiler
	# value_CTankLow=20 #constant for low level of condensed tank 
	# valve1_1=1        #By default open as for a 3 way valve one side should be opened
	
	# if SumpLow == 0:            
	# 	valve1_1=1
	# elif SumpLow==1 and level2==0:
	# 	valve1_1=0
	
	# #Computing pump current
	# power=2000
	# current_lst=[]
	# for x in range(0,60):
	# 	fluc_vol=rd.randrange(180,240)
	# 	current=power//fluc_vol #I=P/V
	# 	current_lst.append(current)
	# 	current_data=np.array(current)


	# fluc_v=fluc_vol         #flutuating voltage
	

	# startTime=0
	# duration=0
	# i=0
	# #Noting Pump operation time of on and not on
	# time_list=[]
	# if 200 <= fluc_v and fluc_v <= 220 and (valve1_1 == 1 or valve1_2 == 1):
	# 	pump=1
	# 	if startTime==0:
	# 		startTime=time.time()		
	# if levelB1 >= value_levelB1: #(and 150<=tempB1<=20):)
	# 		pump=0
	# 		time.sleep(rd.randrange(0,2))
	# 		stopTime=time.time()
	# 		#print stopTime
	# 		duration=stopTime-startTime
	# 		time_list.append(duration)

	# 		# print duration 
	
	# else:
	# 	pump=0
	# 	stopTime=0
	# 	duration=stopTime-startTime
	
	# # def boileraction(heater): #Function turns on the heater when condition is met
	# # 	if levelB1 >= value_levelB1:
	# # 		heater=1
	# # 	return heater
	
	# # def boileraction1(tempB1): #Function Computes the Temperature of boiler
	# # 	if levelB1 >=value_levelB1:
	# # 		# tempB1=tempB1=tempB1+(3.0*heat_coefficient)/(3.0*levelB1)
	# # 		return tempB1 
	
	# # def boileraction2(): #Function Computes the Level of Boiler
	# # 	if levelB1 >= value_levelB1:
	# # 		# levelB1=levelB1+4
	# # 		return levelB1
	
	# if tempB1 >= 112 and tempB1 <= 130: 
	# 	# level2=level2+10
	# 	valve2=1
	
	# if tempB1 > 130 and tempB1 < 170:
	# 	# level2=level2+10
	# 	valve2=1
	# if tempB1 >= 170:
	# 	safety_valve=1
	# 	valve2=0
	# 	# level2=level2-4
	# 	valve1_2=1
	# 	valve1_1=0	
	

	# heater=boileraction(heater)
	# tempB1=boileraction1(tempB1)
	# levelB1=boileraction2()
	# levelB1=response.registers
	# print response.registers

	# opc_client.write_register(SumpLow, SumpLow)
	# opc_client.write_register(ValvePos_S, valve1_1)
	# opc_client.write_register(ValvePos_CT, valve1_2)
	# opc_client.write_register(Pump, pump)
	# opc_client.write_register(LevelBoiler, levelB1)
	# opc_client.write_register(TempBoiler, tempB1)
	# opc_client.write_register(Heater, heater)
	# opc_client.write_register(SteamOutlet, valve2)
	# opc_client.write_register(CTankLevel, level2)




	printvalues(SumpLow, valve1_1, valve1_2, pump, levelB1, tempB1, heater, valve2, level2)
		#sys.exit()

#Code will be completed shortly