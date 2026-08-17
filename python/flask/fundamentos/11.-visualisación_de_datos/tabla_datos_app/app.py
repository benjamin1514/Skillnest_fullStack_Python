from flask import Flask, render_template, request

app = Flask(__name__)

datos = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]

@app.route('/')
def index():
    pais = request.args.get('pais', 'Todos')
    orden = request.args.get('orden', 'nombre')
    direccion = request.args.get('direccion', 'asc')

    # Filtrar
    resultado = datos if pais == 'Todos' else [d for d in datos if d['pais'] == pais]

    # Ordenar
    reverse = (direccion == 'desc')
    resultado = sorted(resultado, key=lambda x: x.get(orden, ''), reverse=reverse)

    return render_template('tabla.html', plataformas=resultado, pais_sel=pais, orden_sel=orden, dir_sel=direccion)

if __name__ == '__main__':
    app.run(debug=True)