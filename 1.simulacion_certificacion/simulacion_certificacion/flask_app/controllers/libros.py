from datetime import datetime
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


@app.route('/libros/<int:id_libro>')
def ver_libro(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  libro = Libro.get_by_id({'id_libro': id_libro})
  if not libro:
    return redirect('/dashboard')

  return render_template('detalle_libro.html', libro=libro)


@app.route('/libros/<int:id>/editar')
def editar_libro(id):
    if 'id_usuario' not in session:
        return redirect('/')

    libro = Libro.obtener_por_id({'id': id})

    # Verificar que el libro pertenezca al usuario en sesión
    if not libro or libro['id_usuario'] != session['id_usuario']:
        return redirect('/libros')

    # Convertir fecha a string YYYY-MM-DD si viene como objeto datetime/date
    if hasattr(libro['fecha_publicacion'], 'strftime'):
        libro['fecha_publicacion'] = libro['fecha_publicacion'].strftime('%Y-%m-%d')

    return render_template('editar_libro.html', libro=libro)


@app.route('/libros/<int:id_libro>/actualizar', methods=['POST'])
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


@app.route('/libros/<int:id_libro>/agregar_mi_lista')
def agregar_a_mi_lista(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  data = {'id_usuario': session['id_usuario'], 'id_libro': id_libro}
  Libro.add_to_my_list(data)
  return redirect('/dashboard')


@app.route('/libros/<int:id_libro>/quitar_mi_lista')
def quitar_de_mi_lista(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  data = {'id_usuario': session['id_usuario'], 'id_libro': id_libro}
  Libro.remove_from_my_list(data)
  return redirect('/dashboard')


@app.route('/libros/<int:id_libro>/eliminar')
def eliminar_libro(id_libro):
  if 'id_usuario' not in session:
    return redirect('/')

  data = {'id_libro': id_libro, 'id_usuario': session['id_usuario']}

  Libro.delete(data)
  return redirect('/dashboard')


@staticmethod
def validar_libro(data):
    es_valido = True

    if data.get('fecha_publicacion'):
        fecha_ingresada = datetime.strptime(data['fecha_publicacion'], '%Y-%m-%d').date()
        fecha_actual = datetime.now().date()
        if fecha_ingresada > fecha_actual:
            flash("La fecha de publicación no puede ser futura.", "libro")
            es_valido = False

    return es_valido