#!/bin/sh
import fileinput

def KSA(key):
	#Llenamos el vector S con valores de 0 a 256
	S = list(range(0,256))
	keylength=len(key)
	j = 0 
	#Aqui se iran cambiando los valores de S segun el valor de la operacion en J 
	for i in range(256):
		j = (j+S[i]+key[i%keylength])%256
		S[i],S[j]= S[j],S[i]

	return S


def PRGA(S,mensaje):

	KS = []
	i = j = k = 0 
	#Llenamos el vector KS en este ciclo 
	while (k < len(mensaje)):
		i = (i+1)%256
		j = (j+S[i])%256
		S[i],S[j]= S[j],S[i]
		t = (S[i]+S[j])%256
		KS.append(S[t])
		k+=1
	return KS

def cifrado(key, mensaje):
	#Aqui se llama a KSA y a PRGA 
	S = KSA(key)
	KS = PRGA(S, mensaje)
	cifrado = []
	cifradohexa= ''
	#En este ciclo se hace XOR de KS con el mensaje 
	for i in range(len(mensaje)):
		C = KS[i] ^ mensaje[i]
		cifrado.append(C)
	#Estan en decimal y se les da formato de hexadecimal
	for i in cifrado: 
		z = format(i,'02X')
		cifradohexa+=z
	print(cifradohexa)

archivo = fileinput.input()
leerlinea = archivo.readline()
seleccion= leerlinea.rstrip('\n')
key = bytes(seleccion,'utf-8')
leerlinea = archivo.readline()
seleccion= leerlinea.rstrip('\n')
mensaje = bytes(seleccion,'utf-8')
cifrado(key,mensaje)














