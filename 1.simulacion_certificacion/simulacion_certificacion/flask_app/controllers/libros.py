from flask import flash, redirect, render_template, request, session
from flask_app import app
from flask_app.models.genero import Genero
from flask_app.models.libro import Libro


@app.route('/dashboard')
def dashboard():
  if 'id_usuario' not in session:
    return redirect('/')

  data = {'id_usuario': session['id_usuario']}
  mis_libros = Libro.get_all_by_user(data)
  libros_comunidad = Libro.get_all_community(data)

  return render_template(
      'dashboard.html',
      mis_libros=mis_libros,
      libros_comunidad=libros_comunidad,
  )


@app.route('/libros/nuevo')
def nuevo_libro():
  if 'id_usuario' not in session:
    return redirect('/')

  generos = Genero.get_all()
  return render_template('agregar_libro.html', generos=generos)


@app.route('/libros/crear', methods=['POST'])
def crear_libro():
  if 'id_usuario' not in session:
    return redirect('/')

  if not Libro.validar_libro(request.form):
    return redirect('/libros/nuevo')

  data = {
      'titulo': request.form['titulo'],
      'autor': request.form['autor'],
      'descripcion': request.form['descripcion'],
      'id_genero': request.form['id_genero'],
      'id_usuario': session['id_usuario'],
  }

  id_libro = Libro.save(data)

  # Al crear el libro, también se añade automáticamente a 'Mis Libros' del creador
  Libro.add_to_my_list({'id_usuario': session['id_usuario'], 'id_libro': id_libro})

  return redirect('/dashboard')


@app.route('/libros/')
def ver_libro(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  libro = Libro.get_by_id({'id_libro': id_libro})
  if not libro:
    return redirect('/dashboard')

  return render_template('detalle_libro.html', libro=libro)


@app.route('/libros//editar')
def editar_libro(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  libro = Libro.get_by_id({'id_libro': id_libro})

  # Seguridad: solo el creador puede editar el libro
  if not libro or libro.id_usuario != session['id_usuario']:
    return redirect('/dashboard')

  generos = Genero.get_all()
  return render_template('editar_libro.html', libro=libro, generos=generos)


@app.route('/libros//actualizar', methods=['POST'])
def actualizar_libro(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  if not Libro.validar_libro(request.form):
    return redirect(f'/libros/{id_libro}/editar')

  data = {
      'id_libro': id_libro,
      'titulo': request.form['titulo'],
      'autor': request.form['autor'],
      'descripcion': request.form['descripcion'],
      'id_genero': request.form['id_genero'],
      'id_usuario': session['id_usuario'],
  }

  Libro.update(data)
  return redirect('/dashboard')


@app.route('/libros//agregar_mi_lista')
def agregar_a_mi_lista(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  data = {'id_usuario': session['id_usuario'], 'id_libro': id_libro}
  Libro.add_to_my_list(data)
  return redirect('/dashboard')


@app.route('/libros//quitar_mi_lista')
def quitar_de_mi_lista(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  data = {'id_usuario': session['id_usuario'], 'id_libro': id_libro}
  Libro.remove_from_my_list(data)
  return redirect('/dashboard')


@app.route('/libros//eliminar')
def eliminar_libro(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  data = {'id_libro': id_libro, 'id_usuario': session['id_usuario']}

  Libro.delete(data)
  return redirect('/dashboard')