from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
  if 'id_usuario' in session:
    return redirect('/dashboard')
  return render_template('index.html')


@app.route('/registro', methods=['POST'])
def registro():
  if not Usuario.validar_registro(request.form):
    return redirect('/')

  pw_hash = bcrypt.generate_password_hash(request.form['password']).decode(
      'utf-8'
  )

  data = {
      'nombre': request.form['nombre'],
      'apellido': request.form['apellido'],
      'email': request.form['email'],
      'password': pw_hash,
  }

  id_usuario = Usuario.save(data)
  session['id_usuario'] = id_usuario
  session['nombre'] = request.form['nombre']

  return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
  user = Usuario.get_by_email({'email': request.form['email']})

  if not user:
    flash('Correo o contraseña no válidos.', 'login')
    return redirect('/')

  if not bcrypt.check_password_hash(user.password, request.form['password']):
    flash('Correo o contraseña no válidos.', 'login')
    return redirect('/')

  session['id_usuario'] = user.id_usuario
  session['nombre'] = user.nombre

  return redirect('/dashboard')


@app.route('/perfil')
def perfil():
  if 'id_usuario' not in session:
    return redirect('/')

  usuario = Usuario.get_by_id({'id_usuario': session['id_usuario']})
  return render_template('perfil.html', usuario=usuario)


@app.route('/logout')
def logout():
  session.clear()
  return redirect('/')