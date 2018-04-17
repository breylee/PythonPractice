#sequences
#lists
print("list demo")
x = [5,12,13,200]
print(x)
x.append(-2) 	#[5,12,13,200,-2]
print(x)
del x[2]		#[5,12,200,-2]
print(x)
z = x[1:3]		#[12,200]
print(z)		
yy = [3,4,5,12,13]
print(yy[3:])	#[12,13]
print(yy[:3])	#[3,4,5]
print(yy[-1])	#[13]
x.insert(2,28)  #[5,12,28,200,-2]
print(x)
print(28 in x)	#True
print(13 in x)	#False
print(x.index(28)) #2
x.remove(200)
print(x)      	#[5,12,28,-2] #removes first only
w = x + [1,"ghi"] #[5,12,28,-2,1,'ghi']
print(w)
qz = 3*[1,2,3]	#[1,2,3,1,2,3,1,2,3]
print(qz)
x=[1,2,3]		#[1,2,3]
print(x)
x.extend([4,5])	#[1,2,3,4,5]
print(x)
g = [1,2,3]
g.append([4,5]) #[1,2,3,[4,5]]
print(g)
y = x.pop(0)		#1
print(y)
print(x)		#[2,3,4,5]
t = [5,12,13]
t.reverse()		#[13,12,5]
print(t)

#append vs extend
#append [ 1 , 2 , 3 , 8 , 88 , [ 8 , 8 8] ]
#extend [ 1 , 2 , 3 , 8 , 88]

#swapping
x = 5
y = 10
z = 15
print(x,y,z)
[x,y,z] = [y,z,x]
print(x,y,z)