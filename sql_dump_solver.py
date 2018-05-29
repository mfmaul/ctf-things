f = open('query_flag_decoded.txt', 'rb').read().split('\n')
char_flag_raw = []
index_flag_raw = []
for x in range(len(f)-3, -1, -1):
	getidx = f[x].find('>')
	index_flag = f[x][getidx-9:getidx]
	if index_flag not in index_flag_raw:
		if 'ag' in index_flag:
			continue
		index_flag_raw.append(index_flag)
		char_flag_raw.append(f[x][getidx+1:getidx+4])
index_flag = []
for x in range(len(index_flag_raw)):
	getidx = index_flag_raw[x].find(',')
	if getidx == 0:
		getidx = index_flag_raw[x][1:len(index_flag_raw[x])].find(',')
		index_flag.append(int(index_flag_raw[x][getidx+2:getidx+3]))
		continue
	index_flag.append(int(index_flag_raw[x][getidx+1:getidx+3]))
char_flag = []
for x in range(len(char_flag_raw)):
	charcon = char_flag_raw[x].replace(' ', '')
	if x==0:
		charcon = charcon[:1]
	char_flag.append(chr(int(charcon)))
flag = ''
for x in range(1, len(char_flag)+1):
	flag += char_flag[index_flag.index(x)]

print flag
