from field import *
"""
import time
time_list=[]
curr_time=int(time.time()%60)
print curr_time

for i in range(0,4):
	curr_time=int(time.time() % 60)
	time_list.append(curr_time+i)

print time_list 


	
while()
	StartTime=0; #Epoch Timestamp from the pc
	duration= 0; #Initialize
	if(all conditions are still ok)

		while()
			if(all conditions are still ok)
				pump run;
				if(StartTime==0)
					StartTime=currentTime;
				level increase(boiler tank);
				if(v position is v2)
					level decrease(con tank);
				if(level of boiler tank achieved)
					pump off;
					StopTime=currenttime;
					duration=StopTime-StartTime;
					break;
			else
				pump stop;
				StopTime;
				duration=StopTime-StartTime;
				break;
	else;
	if(duration != 0)
		log duration;
"""
while True:
	while True:
		
		startTime=0
		duration=0
		if 200 <= n <= 220 and (v1_1 == 1 or v1_2 == 1):
			pump=1
			if startTime==0:
				startTime=time.time()
				#fill_tank(levelB1)
				#calctemp()
				
			if levelB1 == 1:
				valve2=1
				pump=0
				stopTime=time.time()
				duration=stopTime-startTime
				break
			
			#if valve2==1:
	
				#empty_tank()
		else:
			pump=0
			stopTime=0
			duration=stopTime-startTime
			break			
#def calctemp():
print duration

