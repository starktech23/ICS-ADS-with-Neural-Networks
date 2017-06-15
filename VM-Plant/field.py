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

client = ModbusTcpClient(FIELD_IP, FIELD_PORT)
client.connect()

client.write_register(LL, 1.0)
client.write_register(V1_1, 1.0)
client.write_register(V1_2, 0.0)
client.write_register(P,  0.0)
client.write_register(L1, 20.0)
client.write_register(T1, 30.0)
client.write_register(H,  0.0)
client.write_register(V2, 0.0)
#client.write_register(L2, 10.0)
client.write_register(L2L,20.0)
"""
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
"""
#while True:

lowlevel = float(client.read_holding_registers(LL, 1).registers[0])
valve1_1 = float(client.read_holding_registers(V1_1, 1).registers[0])
valve1_2 = float(client.read_holding_registers(V1_2, 1).registers[0])
pump     = client.read_holding_registers(P, 1).registers[0]
levelB1  = client.read_holding_registers(L1, 1).registers[0]
tempB1   = client.read_holding_registers(T1, 1).registers[0]
heater   = client.read_holding_registers(H, 1).registers[0]
valve2   = client.read_holding_registers(V2, 1).registers[0]
lowlevel2= client.read_holding_registers(L2L, 1).registers[0]
#--------------Logic of Filling the SUMP continuously-----------


value_lowlevel=20
value_levelB1=20
value_lowlevel2=20
Sump_Tank = 1
for i in range(0,SIM_TIME):

#while True:
	while  True:
		
		
		for i in range(0,50):
			if i <= value_lowlevel:
				lowlevel=1
				
			else:
				lowlevel=0
		break
	#----------------------------------------------------------------
		#Funtion to fill tank
		 # def fill_tank(check_amount):
		 # 	for i in range(0,100):
		 # 		if i <= check_amount:
		 # 			lowlevel2=1
		 # 		else:
		 # 			lowlevel2=0
		#Function to empty tank
	"""
		def empty_tank(check_amount):
			for i in count():
	    		if i >= check_amount:
	    				break

	"""         	
	#Segment of Code of Operation of plant by checking pump logic------
	value_lowlevel=20
	value_levelB1=20
	value_lowlevel2=20
	valve1_1=1#By default open
	if lowlevel == 0:            
		valve1_1=1
	elif lowlevel==1 and lowlevel2==0:
		valve1_1=0
	#Computing pump current
	power=2000
	current_lst=[]
	for x in range(0,60):
		fluc_vol=rd.randrange(180,240)
		current=fluc_vol//power #I=V/P
		current_lst.append(current)
		current_data=np.array(current)

	n=fluc_vol#flutuating voltage
	#print n

	startTime=0
	duration=0
	i=0
	#for i in range(0,4):

	if 200 <= n and n <= 220 and (valve1_1 == 1 or valve1_2 == 1):
		pump=1
		if startTime==0:
			
			startTime=time.time()		

		if levelB1 >= value_levelB1: #(and 150<=tempB1<=20):)
			
			pump=0
			time.sleep(rd.randrange(0,5))
			stopTime=time.time()
			#print stopTime
			duration=stopTime-startTime
			print duration
			
	else:	
		pump=0
		stopTime=0
		duration=stopTime-startTime
		#sys.exit()
	
	if levelB1 >= value_levelB1:
		heater=1
		tempB1=tempB1+(3.0*heat_coefficient)/(3.0*levelB1)
		levelB1=levelB1+10
	else:
		heater=0
		tempB1 = tempB1 - (3.0*heat_coefficient2)/(3.0*levelB1)
	if tempB1 >=112 and tempB1 <= 130:
		valve2=1
	if tempB1 > 130:
		safety_valve=1

	if valve2 == 1:
		
		if lowlevel2 >= value_lowlevel2:
			valve1_2=1
		else:
			valve1_2=0


	# for i in range(0,SIM_TIME):
	# 	if i%2==0:
	# 		plantwithvalve1_1open()
	# 	else:
	# 		plantwithvalve1_2open()	


	client.write_register(LL, lowlevel)
	client.write_register(V1_1, valve1_1)
	client.write_register(V1_2, valve1_2)
	client.write_register(P, pump)
	client.write_register(T1, tempB1)
	client.write_register(H, heater)
	client.write_register(V2, valve2)
	client.write_register(L2L, lowlevel2)




	printvalues("field",lowlevel, valve1_1, valve1_2, pump, levelB1, tempB1, heater, valve2, lowlevel2)
		#sys.exit()
