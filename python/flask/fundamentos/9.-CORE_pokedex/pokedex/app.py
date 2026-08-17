from flask import Flask, render_template

app = Flask(__name__)

pokedex = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]

@app.errorhandler(404)
def pokemon_no_encontrado(e):
    # Captura el mensaje si se llama manualmente o usa un mensaje por defecto para URLs inválidas
    mensaje = e if isinstance(e, str) else "El recurso o Pokémon solicitado no existe."
    return render_template("404.html", mensaje=mensaje), 404
    if not pokemon:
        return pokemon_no_encontrado(f'No pudimos encontrar el Pokémon con ID #{id}.')

@app.route("/")
@app.route("/pokemon")
def mostrar_todos_pokemon():
    return render_template("pokemon.html", pokedex=pokedex)

# La ruta numérica debe ir ANTES de la ruta por texto para evitar conflictos de evaluación
@app.route("/pokemon/<int:id>")
def mostrar_pokemon_por_id(id: int):        
    pokemon = next((p for p in pokedex if p["id"] == id), None)
    if pokemon:
        return render_template("pokemon.html", pokedex=[pokemon])
    return pokemon_no_encontrado(f'No pudimos encontrar información sobre el Pokémon #{id} en nuestra Pokédex.')

@app.route("/pokemon/<string:nombre>")
def mostrar_pokemon_por_nombre(nombre: str):
    pokemon = next((p for p in pokedex if p["nombre"].lower() == nombre.lower()), None)
    if pokemon:
        return render_template("pokemon.html", pokedex=[pokemon])
    return pokemon_no_encontrado(f'No pudimos encontrar información sobre "{nombre}" en nuestra Pokédex.')

@app.route("/pokemon/cantidad/<int:cantidad>")
def mostrar_cantidad_pokemon(cantidad: int):
    if cantidad <= 0:
        return pokemon_no_encontrado("La cantidad solicitada debe ser mayor que cero.")
    elif cantidad > len(pokedex):
        return pokemon_no_encontrado(f"No hay suficientes Pokémon. Solo hay {len(pokedex)} registrados.")
    return render_template("pokemon.html", pokedex=pokedex[:cantidad])

if __name__ == "__main__":
    app.run(debug=True)