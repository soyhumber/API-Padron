#!/usr/bin/python

# -*- coding: utf-8 -*-

import requests
import json
import os
import response


""" mostrar_provincia = requests.get('http://127.0.0.1:5000/provincias').json()
mostrar_cantones = requests.get('http://127.0.0.1:5000/cantones').json()
mostrar_distritos = requests.get('http://127.0.0.1:5000/distritos').json()
mostrar = requests.get('http://127.0.0.1:5000/cantones/canton-provincia/1').json()
mostrar = requests.get('http://127.0.0.1:5000/cantones/canton-provincia/1').json()
mostrar = requests.get('http://127.0.0.1:5000/cantones/canton-provincia/1').json()
mostrar = requests.get('http://127.0.0.1:5000/cantones/canton-provincia/1').json()
mostrar = requests.get('http://127.0.0.1:5000/cantones/canton-provincia/1').json() """

response_provincia = requests.get('http://127.0.0.1:5000/provincias')
response_cantones = requests.get('http://127.0.0.1:5000/cantones')
response_distritos = requests.get('http://127.0.0.1:5000/distritos')
provincia = response_provincia.content
cantones = response_cantones.content
distritos = response_cantones.content


def menu():

	"""

	Función que limpia la pantalla y muestra nuevamente el menu

	"""

	os.system('clear') # NOTA para windows tienes que cambiar clear por cls

	print ("Selecciona una opción")

	print ("\t1 - Consulta de Provincias")

	print ("\t2 - Consulta de Cantones")

	print ("\t3 - Consulta de Distritos")


	print ("\t9 - salir")

 

 

while True:

	# Mostramos el menu

	menu()

 

	# solicituamos una opción al usuario

	opcionMenu = input("inserta un numero valor >> ")

 

	if opcionMenu=="1":
        
		print (provincia)

		input("Has pulsado la opción 1...\npulsa una tecla para continuar")


	elif opcionMenu=="2":

		print (cantones)

		input("Has pulsado la opción 2...\npulsa una tecla para continuar")


	elif opcionMenu=="3":
        
		print (distritos)

		input("Has pulsado la opción 3...\npulsa una tecla para continuar")


	elif opcionMenu=="9":

		break

	else:

		print ("")

		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")