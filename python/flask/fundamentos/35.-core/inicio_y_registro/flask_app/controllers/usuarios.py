from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    if "id_usuario" in session:
        return redirect("/dashboard")
    return render_template("login.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    datos = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip().lower(),
        "password": request.form["password"],
        "confirm_password": request.form.get("confirm_password", "")
    }

    if not Usuario.validar_usuario(datos):
        return redirect("/")

    if Usuario.existe_email({"email": datos["email"]}):
        flash("El email ya está registrado.", "email")
        return redirect("/")

    password_hash = bcrypt.generate_password_hash(datos["password"]).decode("utf-8")
    datos["password"] = password_hash

    usuario_id = Usuario.guardar(datos)

    if not usuario_id:
        flash("No fue posible registrar el usuario.", "general")
        return redirect("/")

    session["id_usuario"] = usuario_id
    return redirect("/dashboard")

@app.route("/login", methods=["POST"])
def login():
    datos = {
        "email": request.form["email"].strip().lower(),
        "password": request.form["password"]
    }

    usuario = Usuario.buscar_por_email({"email": datos["email"]})

    if not usuario or not bcrypt.check_password_hash(usuario.password, datos["password"]):
        flash("Email o contraseña incorrectos.", "login")
        return redirect("/")

    session["id_usuario"] = usuario.id_usuario
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    if "id_usuario" not in session:
        return redirect("/")

    usuario = Usuario.buscar_por_id({"id_usuario": session["id_usuario"]})

    if not usuario:
        return redirect("/")

    return render_template("dashboard.html", usuario=usuario)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")