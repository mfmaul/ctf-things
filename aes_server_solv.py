import base64
flag = 'hmePAG+BdH0jx47Emdd9evRDtaKdxCBJAPloWNp9FUlbCcLA7Z0YmO0fiGmSSsQJDlCVShfw3THOpCCSoRZ84g=='
cipher = 'hmePAG+BdH0j4t/6gYZpRMBMsPCO1jUcD/xWbdMvK0sKBsCS/Igmyeohq2TDSM43DACEQ0Xjgy2lu1vENIh52g=='
plaintext = 'HackFest{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}'
flag_dec = base64.b64decode(flag)
cipher_dec = base64.b64decode(cipher)
key = ''
for x in range(len(plaintext)):
	key += chr(ord(plaintext[x])^ord(cipher_dec[x]))
flagnya = ''
for x in range(len(flag_dec)):
	flagnya += chr(ord(key[x%len(key)])^ord(flag_dec[x]))
print flagnya
