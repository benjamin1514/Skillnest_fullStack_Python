# Ranking de puntajes de un torneo de eSports
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
'''
En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda).
Resultado esperado
puntajes = [[1000, 1500, 2000], [600, 700, 1400]]
'''

puntajes[1][0] = 600

print(puntajes)


# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]

# En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.

streamers[0]["nombre"] = "ElitegamerX"
print(streamers[0])


# Eventos en distintas ciudades del mundo
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}

#En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.
eventos["Estados Unidos"][2] = "San Francisco"

print(eventos["Estados Unidos"])

# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]

'''
En ubicacion, cambia el valo de ”latitud” a 40.712776 
(cambiando la sede del torneo a Nueva York).
'''

ubicacion[0]["latitud"] = 40.712776

print(ubicacion[0]["latitud"])

'''
Crea la función iterar_diccionario(lista) que reciba una lista de diccionarios 
(como streamers) y recorra cada uno, 
imprimiendo sus claves y valores.
'''

'''
Formatea la salida para que cada diccionario se 
imprima en una sola línea, con el formato.
nombre - EliteGamerX, seguidores - 250000
'''
ListaItems = {
    "nombre": ["EliteGamerX", "PixelWarrior"], "seguidores": [250000, 180000]
}
def iterar_diccionario(lista,diccionario):
    valor = diccionario.get(lista, [])
    for valores in valor:
        print(valores)
    
iterar_diccionario("nombre", ListaItems)
iterar_diccionario("seguidores", ListaItems)
    
        
    
categorias = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}

def mostrar_informacion(categorias):
    pass







