# Example3: functions

def func1 (x,y):
	#Sums two numbers
	z = x + y
	return z
a = 4
b = 7 
c = func1 (a,b)
print "Sum of two numberes is", c

def func2 (a, b):
	# Floor division
	c = b // a	
	return c
c = func2(a,b) 	
print "Floor division of %d i %d is %d" % (b,a,c)

### __END__ Example3