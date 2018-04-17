# reads in the text file whosename is specified on command line
# and reports the number of lines and words

import sys

def checkline():
	global _l
	global _wordcount
	w = _l.split()
	_wordcount += len(w)
	
_wordcount = 0
f = open(sys.argv[1])
flines = f.readlines()
linecount = len(flines)
for _l in flines:
	checkline()
print(linecount,_wordcount)

