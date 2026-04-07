# Bucles While

'''
La sentencia while es otra manera en la que podemos crear un bucle; esta va a ser repetida mientras
(while en inglés) se cumpla con la condicional dada.


'''
# La sintaxis en Python es:

#while condicion:
#    pass#Código que se ejecuta mientras la condición se cumpla

# Veamos el siguiente ejemplo: 

num = 0

while num < 4:
    print("bucle while -", num)
    num += 1
#Imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3

# while con Else 

num = 0
while num < 4:
    print("bucle while -", num)
    num += 1
else:
    print("Acabamos de salir del bucle")
    

# Break

'''
La sentencia break termina de forma definitiva el bucle y 
continúa con la primera sentencia después del bucle. 
El break se puede utilizar tanto para bucles for como para while.
'''

'''
El break suele utilizarse cuando sucede 
alguna condición externa que demanda salir del bucle de manera inmediata.
'''
