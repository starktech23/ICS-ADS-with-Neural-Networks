from config import *
from itertools import count
from pymodbus.client.sync import ModbusTcpClient
import random as rd
from random import *
import numpy as np
import time
import sys



power=2000
current_lst=[]
for x in range(0,60):
	fluc_vol=rd.randrange(180,240)
	current=fluc_vol//power #I=V/P
	current_lst.append(current)
	current_data=np.array(current)

#c=rd.choice(current_data)
#print c
n=fluc_vol#flutuating voltage
print n

	
levelB1=0	
startTime=0
duration=0
i=0
for i in range(0,4):

	if 200 <= n and n <= 220: #(#(valve1_1 == 1 or valve1_2 == 1))
		pump=1
		if startTime==0:
			
			startTime=time.time()
			#print startTime
			

		#fill_tank(value_levelB1)
	#calctemp()

		if levelB1 == 0: #(and 150<=tempB1<=20):)
			valve2=1
			pump=0
			time.sleep(rd.randrange(0,5))
			stopTime=time.time()
			#print stopTime
			duration=stopTime-startTime
			print duration
	
#break
#break
#if valve2==1:

#empty_tank()
else:	
	pump=0
	stopTime=0
	duration=stopTime-startTime
sys.exit()