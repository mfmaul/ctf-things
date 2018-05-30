#!/usr/bin/python

cipher = 'TbioooIlpdpnFohee}Ece_rSkroaT__ft{cm_i'
block_size = 7
len_cipher = len(cipher)
remainder = len_cipher % block_size
horizontal_block = (len_cipher+(block_size-remainder)) / block_size

cipher_split_horizontal = []
count = 0
for x in range(block_size):
	if x < remainder:
		cipher_split_horizontal.append(cipher[count:count+horizontal_block])
		count += horizontal_block
		continue
	cipher_split_horizontal.append(cipher[count:count+horizontal_block-1])
	count += horizontal_block-1

plain = ''
for x in range(block_size):
	try:
		for block_horizontal in cipher_split_horizontal:
			plain += block_horizontal[x]
	except:
		pass

print plain
