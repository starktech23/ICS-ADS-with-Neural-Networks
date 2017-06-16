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
level2= client.read_holding_registers(L2L, 1).registers[0]
#--------------Logic of Filling the SUMP continuously-----------


value_lowlevel=20
value_levelB1=20
value_lowlevel2=20
Sump_Tank = 1
#Simulation will run according to the sim time
for i in range(0,SIM_TIME):

	while  True:
		
		
		for i in range(0,50):
			if i <= value_lowlevel:
				lowlevel=1
				
			else:
				lowlevel=0
		break        	
	#Segment of Code of Operation of plant by checking pump logic------
	value_lowlevel=20 #constant for low level sensor of sump
	value_levelB1=20#constant for low level of boiler
	value_lowlevel2=20#constant for low level of condensed tank 
	valve1_1=1 #By default open as for a 3 way valve one side should be opened
	
	if lowlevel == 0:            
		valve1_1=1
	elif lowlevel==1 and level2==0:
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
	#Noting Pump operation time of on and not on
	time_list=[]
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
			time_list.append(duration)
			print duration
			
	else:	
		pump=0
		stopTime=0
		duration=stopTime-startTime
		
		#sys.exit()
	
	if levelB1 >= value_levelB1 and levelB1: 
		heater=1
		tempB1=tempB1+(3.0*heat_coefficient)/(3.0*levelB1) 
		levelB1=levelB1+4	
	
	if tempB1 >=112 and tempB1 <= 130: 
		valve2=1
		level2=level2+10
		# levelB1=levelB1+2

	if tempB1 > 130: 
		heater=0
		tempB1=tempB1-2
	if level2 >= levelB1+3:
		valve1_1=0
		valve1_2=1



	
	




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
	if valve2 == 1:
		client.write_register(V2, valve2)
	else:
		client.write_register(V2, valve2)
	client.write_register(L2L, level2)




	printvalues("field",lowlevel, valve1_1, valve1_2, pump, levelB1, tempB1, heater, valve2, level2)
		#sys.exit()

#print time_list