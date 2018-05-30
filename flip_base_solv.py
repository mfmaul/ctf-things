from pwn import *
import base64

r = remote('ctf.komatik.wg.ugm.ac.id', 21300)
n = 10
inc = 0

def tryin(getit):
	l, rht = 0, 8
	tmp = ''
	for y in range(len(getit)/8):
		tmp += chr(int(getit[l:rht], 2))
		l, rht = l+8, rht+8
		print l, rht
	return tmp

"""
    for y in range(len(getit)/8):
		tmp += chr(int(getit[l:rht], 2))
		l, rht = l+8, rht+8
"""

for x in range(n):
	r.recvuntil('(*) Ai pass a salt\n    ')
	salt = r.recvline().strip()
	r.recvuntil('(*) Char got\n    ')
	get_char = r.recvline().strip()
	r.recvuntil('(*) Answer\n    ')
	map_char = []
	for y in range(len(get_char)):
		if get_char[y] != '=':
			map_char.append(get_char[y])
			continue
	ex = []
	print 'map char : ', map_char
	for y in range(len(map_char)):
		ex.append("{0:b}".format(salt.find(map_char[y])))
	for y in range(len(ex)):
		if len(ex[y])%6 != 0:
			ex[y] = '0'*(6-len(ex[y])) + ex[y]
	getit = ''.join(ex)
	print len(getit)
	getit = getit[:-(len(getit)%8)]
	tmp = ''
	while len(tmp)==0:
		tmp = tryin(getit)
	print len(tmp)
	print '-----', tmp
	r.sendline(tmp)
	r.recvuntil('Anda')
	print r.recvline()
r.recvuntil('Flag')
print r.recvline()
