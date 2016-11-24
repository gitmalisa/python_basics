# Example2: if statements and dictionaries

x=5
if x==2:   print "x=2"
elif x==3: print "x=3"
else:      print "x!=2 and x!=3"


dict1={'1': 1, '2': 2, '3': 3}

if (3 is dict1['1']):
	pass

dict2={'Name': 'Pera', 'Surname': 'Petrovic', 'Age': 29}

print "dictionary", dict2	 

print "The first element in dictionary dict2 is", dict2['Name']

print "%s is the second element of the dictionary dict2" % dict2['Surname']

sn = dict2['Surname']
print sn[0:2]
	
	
### __END__ Example2