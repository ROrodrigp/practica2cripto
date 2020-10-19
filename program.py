#!/bin/sh
import fileinput
#import codecs 
S = list(range(0,256))

key= b"Wiki"
M = b"pedia"
keylength=len(key)
#hex = codecs.encode(key, "hex")
print(key[0])

j = 0 
for i in range(256):
	#print('i: ',i)
	#print('j:',j)
	#print('\n',S)
	j = (j+S[i]+key[i%keylength])%256
	S[i],S[j]= S[j],S[i]

KS = []

i = j = k = 0 
while (k < len(M)):
	i = (i+1)%256
	j = (j+S[i])%256
	S[i],S[j]= S[j],S[i]
	t = (S[i]+S[j])%256
	KS.append(S[t])
	k+=1
print(KS)

cifrado = []
for i in range(len(M)):
	C = KS[i] ^ M[i]
	cifrado.append(C)

print(cifrado)
d=[]
e = 0 
y= ''
for i in cifrado:
	#Estan en decimal 
	d.append(i)
	z = format(d[e],'02X')
	y=y+z
	e+=1


print(y)





x = str(d[0])
x = x.strip("0x")
print(x)









