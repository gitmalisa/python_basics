# Example1: Lists and tuples, for and while loops.

a, b, c = "Pera", "Zika", "Laza"
list1 = [a, b, c]
list1.append("Milica")
print list1 + ["Ana"]   # you can only add list on list

x, y, z = 1, 2, 3
tuple1 = (x, y, z)

for exp in tuple1:
	cn = 0
	while (cn<5):
		res = cn**exp
		print res 
		cn+=1
	
### __END__ Example1