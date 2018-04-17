#type conversion
print("type demo")
a = "100"
print("a = \"100\" type: " + str(type(a)))
a = 1
print("a = 1 type: " + str(type(a)))
a = 0.059
print("a = 0.059 type: " + str(type(a)))
a = "0.123456"
print("float(\"0.123456\") type: " + str(type(float(a))))
a = "1256"
print("int(\"1256\") type: " + str(type(int(a))))
print("\n")

#convert string <-> float/int
print("type demo")
print( "eval(\"0xF\") + eval(\"0.123\") :", eval("0xF") + eval("0.123"))
print("\n")

