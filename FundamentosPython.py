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

	nuevoTema("Flotantes")

	x = 1297.5
	print(x, type(x))
	y = 0.052829
	print(y, type (y))

	nuevoTema("Numeros complejos")
	x = -46j
	y = 12 + 45j
	z = 2j
	print(x, type(x))
	print (y, type(y))
	print(z, type(z))

	nuevoTema("Listas")

	a = [10, 30.5, "Python List"]
	print (a)
	a = ["Lista2", 45, 16.3j]
	print(a)
	print(a[2])
	a[1] = 34.6
	print(a)

	nuevoTema("Tuplas")
	t = (25,'tuple', 1+10j)
	print("t[1] =", t[1])
	print(("t^[0:3] = ", t[0:3]))
	print(t) 

	nuevoTema("Conjuntos")
	c = {50, 20, 10, 4, 8 ,50 } #en un conjunto no repite datos
	print(c)

	nuevoTema("Diccionarios")
	d = {1:'val1', "2":45}
	print(d,type(d))
	print(d["2"])
	print(d[1])

	nuevoTema("Cadenas")
	s = "Esta es una linea simple"
	print(s)
	
	c2 = 'Cadena entre comillas sencillas'
	print(c2)
	c3 = ''' 
	Cadena
		de varias 
	Lines'''
	print(c3)