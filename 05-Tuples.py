x = (1,2,"abc")
print(x)
print(x[1])
y = [4,5,6]

zipobject = zip([1,2],[3,4])

#tuples are iterators. to access them, create a list object
listobject = list(zipobject)
print(listobject)
