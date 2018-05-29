from libnum import *

e = 1054942436795568843007638074101
N = 427369574724968124178587825259
c = 130283557086746678882229607299
p = 581413021388071 #didapat dari factordb.com
q = 735053325267229 #didapat dari factordb.com

phi = (p-1) * (q-1)
d = invmod(e, phi)
ascii = pow(c, d, N)
flag = str(ascii)

i = 0
current = []
while i < len(flag):
	if int(flag[i:i+2]) >= 20 and int(flag[i:i+2]) <= 127:
		current.append(chr(int(flag[i:i+2])))
		i = i + 2
	else :
		current.append(chr(int(flag[i:i+3])))
		i = i + 3
print "HackFest{"+''.join(current)+"}"
