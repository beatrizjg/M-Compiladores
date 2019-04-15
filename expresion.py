
"""Laboratorio#2"""
""" El programa debe aceptar la siquiente expresion regular: (a|b)*abb"""
##########################Inicio del Automata############################
def estado0():
	pos = 0
	cadena = raw_input("Ingrese la primera letra:")
	for x in cadena:
		if x == 'a':
			print ("va al estado1 :")
			estado1(cadena, pos)
			break

		elif x == 'b':
			print ("Continue al estado4:")
			#funcion estado5
			estado4(cadena, pos)
			break
		else:
			print("Error, cadena no valida")
			break
		pos +=1

##########################Fin del estado0############################

def estado1(cadena, pos):
	inc = pos+1
	if inc < len(cadena):
		if cadena[inc] == 'a':
			print ("lee estado1:")
			estado1(cadena, inc)

		elif cadena[inc] == 'b':
		    print("va al estado 2")
		    estado2(cadena, inc)
		else:
			print("Error, cadena no valida")
	else:
		print("Error, La cadena no es valida")

##########################Fin del estado1############################

def estado2(cadena, pos):
	inc = pos+1
	if inc < len(cadena):
		if cadena[inc] == 'a':
			print ("retorna al estado1:")
			estado1(cadena, inc)

		elif cadena[inc] == 'b':
			print ("Va al estado3:")
	    		estado3(cadena,inc)
	    	else:
			print("Error, cadena no valida")
	else:
		print("Error, La cadena no es valida")

##########################Fin del estado2############################

def estado3(cadena, pos):
	inc = pos
	if cadena[inc] == 'b':
		print("Cadena valida.")


##########################Fin del estado3############################

def estado4(cadena, pos):
	#print ("prueba2:",pos)
	inc = pos+1
	if inc < len(cadena):
		if cadena[inc] == 'a':
			print ("pasa al estado1:")
			estado1(cadena, inc)

		elif cadena[inc] == 'b':
	    		print ("bucle en el estado4:")
	    		estado4(cadena, inc)	
	    	else:
			print("Error, cadena no valida")
	else:
		print("Error, La cadena no es valida")

estado0()
##########################Fin del estado4############################

