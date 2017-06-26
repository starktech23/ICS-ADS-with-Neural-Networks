val=20
def increment(level):
	level=level+10
	
	print level
	if level>60:
		print level 
		return level
	result = increment(level)
	return result

def decrement(level):
	
	level=level-val
	print level
	if level < 20:
		print level
		return
	decrement(level)
	return

level  = increment(0)
print level
decrement(level)