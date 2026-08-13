from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template(
        "index.html",
        nombre="Benjamin",
        apellido="Delgado",
        curso="Desarrollo Web con Flask",
        institucion="Vate Vicente Huidobro",
        anio=2026,
        es_docente=False,
        tecnologias=[ 
            "Python", 
            "Flask", 
            "HTML", 
            "CSS", 
            "JavaScript"
        ]
    )
    
if __name__ == "__main__":
    app.run(debug=True)