# Example4:  Python classes and objects

class Student:
	'Common class for all registered students'
	studCount = 0
	def __init__(self, name, gpa):
		self.name   = name
		self.gpa = gpa
		Student.studCount +=1
	def printStudent(self):
	    print "Name: %s , Number: %d" % (self.name, self.gpa)
	def printCount(self):
		if Student.studCount==0:
		    print "There are currently no students registered" 
		elif Student.studCount==1:
			print "There is only one student registered"
		else:
		    print "There are total of %d students registered" % Student.studCount
			
# Creating object
stud = Student ("Peter", 3.9)
   
print "Student documentation string:", Student.__doc__
stud.printCount()
stud.printStudent()
 
### __END__ Example4