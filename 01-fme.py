def printEndl():
	print("\n")


#for loop
print("for loop demo") 
for i in range(10):
	x = 0.1 * i
	print(x)
	print(x/1-x*x)
printEndl()

print("array [2,3,6] demo")
for i in [2,3,6]:
	print(i)
printEndl()
	
#while loop
print("while loop")
i = 0
while i<10:
	if i%2 == 0:
		i+=1
		continue	
	print(i)
	i+=1
printEndl()
	
#multiline statement
print("this is a multi\
line statement \
demo")
printEndl()

#boolean
print("boolean demo")
a = True
b = False
c = False
print(a)
print(a and b and c)
print(a or b or c) # a short circuits b and c
printEndl()

#hex
print("hex demo")
a = 16
print("hex(16) is: " + hex(a))
printEndl()

#ascii
print("hex demo")
print("ord(a) is: " + str(ord('a')))
printEndl()


#import demo
import math
print("math.sqrt(64) is: " + str(math.sqrt(64)))