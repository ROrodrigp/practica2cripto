#!/bin/sh
import fileinput
#import codecs 




#hex = codecs.encode(key, "hex")

def KSA(key):
	S = list(range(0,256))
	keylength=len(key)
	j = 0 

	for i in range(256):
		j = (j+S[i]+key[i%keylength])%256
		S[i],S[j]= S[j],S[i]

	return S


def PRGA(S,mensaje):

	KS = []
	i = j = k = 0 

	while (k < len(mensaje)):
		i = (i+1)%256
		j = (j+S[i])%256
		S[i],S[j]= S[j],S[i]
		t = (S[i]+S[j])%256
		KS.append(S[t])
		k+=1
	return KS

	#print(KS)
def cifrado(key, mensaje):
	S = KSA(key)
	KS = PRGA(S, mensaje)
	#print('S:',S)
	#print('KS:',KS)
	cifrado = []
	for i in range(len(mensaje)):
		C = KS[i] ^ mensaje[i]
		cifrado.append(C)
	
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

key= b"Wiki"
mensaje = b"pedia"
cifrado(key,mensaje)














