def nuevoTema(tema):
 	print ("=========",tema, "==========")

#Esto es un comentario
if __name__ == "__main__":
	nuevoTema("Operadores aritmeticos")
	print ("Operador de division entera (10//3) :", 10//3)
	print ("Operador de potencias (5**5):", 5**5) 
	print ("Operador de cambio de signo (-5) :", -5)

	print ("======Logicos======")
	print ("Operador and (True and true): ", True and True)
	print ("Operador and (True and False): ", True and False)
	print ("Operador and (False and False): ", False and False)
	print ("Operador not (not False): ", not False)
	print ("Operador not (not True): ", not True)
	print ("Operador or (True or True): ", True or True)
	print ("Operador or (True or False) ", True or False)
	print ("Operador or (False or True) ", False or True)
	print ("Operador or (False or False) ", False or True)
	

	print ("==== Operadores de comparacion =======")
	
	print ("== es igual", 5==5)
	print ("!= distinto a", 3!=4)

	nuevoTema("Enteros")
	w = 105
	y = 2074074834387878898
	x = -345
	z = 0b00110011 #es un numero binaro y lo traduce
	h = 0xffa #es un numero exadecimal

	print (w, type(w))
	print (x, type(x))
	print (y, type(x))
	print (z,type(z))
	print (h,type (h))

