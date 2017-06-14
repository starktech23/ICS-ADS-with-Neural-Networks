from config import *
from pymodbus.client.sync import ModbusTcpClient
import random as rd
from random import *
import numpy as np
import time
import sys
while True:
	
	sump = int(raw_input("Inlet Water is coming into sump(0,1): "))
	
	if sump == 1:
		for i in range(0,100):
		#print i
			if i == 20:
				ll=1
				#print "Tank has 20 litres of water"
			
		#print i
			if i == 90:
				hl=1
				#print "Tank has 50 litres of water"
				
				break
	else:
		ll=0
		hl=0
		sys.exit()
	break

#tank_time = 
if hl == 1:
	v1_1=1

power=2000
current=[]

for x in range(0,60):
	fluc_vol=rd.randrange(180,240)
	#print fluc_vol
	current.append(fluc_vol)
	
	current_data=np.array(current)
	#print current_data
	
	c=rd.choice(current_data)
	#print c
n=fluc_vol
print n
if 200 <= n <= 220 and (v1_1==1 or v1_2==1):
	p=1
	print p
else:
	p=0
	print p
