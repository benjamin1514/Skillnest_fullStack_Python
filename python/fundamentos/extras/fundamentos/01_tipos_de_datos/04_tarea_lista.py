'''
Actividad : gestor de inventario 
'''
'''
1.- Creación: Crear una lista llamada inventario que contenga los siguientes 
articulos: "laptop", "raton", "monitor", "cable hdmi" 
'''
'''
2.- Expansión: utiliza el metodo correspondiente para agregar "impresora" y "teclado" al final de la lista
'''
'''
3.- Conteo: utiliza la funcion integrada para mostrar cuantos elementos totales hay en una lista
'''
'''
4.- Acceso y modificación: modifica "teclado" por "teclado mecanico"
'''
'''
5.- Slicing: crea una nueva lista llamada promocion, debe contener solo 3 primeros elementos de la lista 
"inventario" 
'''
'''
6.- Mostrar la lista inventario ordenados alfabeticamente
'''
'''
7.- Elimina el ultimo elemento de la lista inventario mostrando el elemento eliminado y la lista final
'''

inventario = ["laptop", "raton", "monitor", "cable hdmi"] 
inventario.append("impresora")
inventario.append("teclado")
inventario[5] = "teclado mecanico"
mostrarUltimo = inventario.pop()
print(f"Elemento eliminado: {mostrarUltimo}")
print(len(inventario))
print(inventario)

promocion = inventario[0:3]
print(promocion)
inventario.sort()
print(inventario)


