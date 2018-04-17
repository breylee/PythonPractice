# reads in the text file whosename is specified on command line
# and reports the number of lines and words

import sys

def checkline():
	global _l
	global _wordcount # has value None during declaration
	w = _l.split()
	_wordcount += len(w)

def myfunc(x):
	if x:
		print("True")
		return
	print("False")

#-----------------main function starts here-------------------
print("Get File Word Line Count")
myfunc(False)
print("len(sys.argv): ",len(sys.argv))
if len(sys.argv) < 2:
	print("Missing Filename")
	exit()
_wordcount = 0
print("argv[0]: ",sys.argv[0])
print("argv[1]: ",sys.argv[1])
f = open(sys.argv[1])
flines = f.readlines()
linecount = len(flines)
for _l in flines:
	checkline()
print("linecount:",linecount,"wordcount",_wordcount)
print("\n")