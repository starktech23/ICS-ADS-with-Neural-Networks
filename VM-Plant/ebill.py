import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.ticker as ticker
import matplotlib.cm as cm
import pandas as pd
# import print_options
import itertools
# from origionalfield import time_list
power=2 #2kw=2000W
time=pd.read_csv('time.csv')
timr=time.dropna(how="all",axis=1)
time_list=timr.drop_duplicates().values.tolist()
time_list = [ y for y in itertools.chain.from_iterable(time_list)]
for i in time_list:
	if i == 0:
		time_list.remove(i)

# print_options.set_float_precision(2)
time_list_hr=[] #in hr
for j in time_list:
	tmp=(j % 6)
	time_list_hr.append(tmp)
# time_list_hr.sort()
# print ["{0:0.2f}".format(i) for i in time_list_hr]

energy_per_day=[]
for i in time_list_hr:
	energy=i*power
	energy_per_day.append(energy)
# print ["{0:0.2f}".format(i) for i in energy_per_day]
sum_energy=0
for i in energy_per_day:
	sum_energy=sum_energy+i
X = 10*np.random.rand(5,3)
e=180
plt.plot(energy_per_day)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.ylim(0,13)
plt.xlim(0,180)
# plt.ticklabel_format(style='sci', axis='x', scilimits=(0,2))
plt.xticks(range(e))
plt.grid()
plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*e+1*m
margin = m/plt.gcf().get_size_inches()[0]

plt.gcf().subplots_adjust(left=margin, right=5.-margin)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
plt.savefig(__file__+".png",dpi=24)
# plt.figure(figsize=(20,100))
plt.title("Electricity Consumed")
plt.xlabel("Days")
# plt.xticklabels(rotation = (45), fontsize = 10, va='bottom', ha='left')
plt.ylabel("Energy kw/hr")

plt.show()

print "Total Electricity Consumed: "+str("{0:.2f}".format(sum_energy))
money=sum_energy*10
print "Electricity Bill: "+str("{0:.2f}".format(money))