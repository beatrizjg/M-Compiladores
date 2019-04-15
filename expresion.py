
"""Laboratorio#2"""
""" El programa debe aceptar la siquiente expresion regular: (a|b)*abb"""

########################## Inicio del Automata ############################
def estado0():
	pos = 0
	cadena = raw_input("Ingrese la primera letra:")
	for x in cadena:
		if x == 'a':
			print ("Recorre del Estado0 al Estado1 :")
			estado1(cadena, pos)
			break

		elif x == 'b':
			print ("Recorre del Estado0 al Estado4 :")
			estado4(cadena, pos)
			break

		else:
			print("Error, cadena no es valida")
			break
		pos +=1

########################## Fin del Estado0 ############################

def estado1(cadena, pos):
	inc = pos+1
	if inc < len(cadena):
		if cadena[inc] == 'a':
			print ("Retorna del Estado1 al Estado1 :")
			estado1(cadena, inc)

		elif cadena[inc] == 'b':
		    print("Recorre del Estado1 al Estado2 :")
		    estado2(cadena, inc)
		else:
			print("Error, cadena no es valida")
	else:
		print("Error, La cadena no es valida")

########################## Fin del Estado1 ############################

def estado2(cadena, pos):
	inc = pos+1
	if inc < len(cadena):
		if cadena[inc] == 'a':
			print ("Recorre del Estado2 al Estado1 :")
			estado1(cadena, inc)

		elif cadena[inc] == 'b':
			print ("Recorre del Estado2 al Estado3 :")
	    		estado3(cadena,inc)
	    	else:
			print("Error, cadena no es valida")
	else:
		print("Error, La cadena no es valida")

########################## Fin del Estado2 ############################

def estado3(cadena, pos):
	inc = pos+ 1
	if inc < len(cadena):
		if cadena[inc] =='a' or cadena[inc] == 'b':
			print("Error, La cadena no es valida")
		
	elif cadena[pos] == 'b':
		print(" la Cadena es valida.")

########################## Fin del Estado3 ############################

def estado4(cadena, pos):
	inc = pos+1
	if inc < len(cadena):
		if cadena[inc] == 'a':
			print ("Recorre del Estado4 al Estado1 :")
			estado1(cadena, inc)

		elif cadena[inc] == 'b':
	    		print ("Retorna del Estado4 al Estado4 :")
	    		estado4(cadena, inc)	
	    	else:
			print("Error, cadena no valida")
	else:
		print("Error, La cadena no es valida")

estado0()

########################## Fin del Estado4 ############################


