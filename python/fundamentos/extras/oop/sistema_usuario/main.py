from usuario import Usuario
continuar = True

while continuar:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Inicio de sesión")
    print("2. Salir")
    opcion = input("Elige una opción (1 o 2): ")
    
    if opcion == "1":
        print("\n===== Inicie sesión =====")
        username = input("Username: ")
        password = input("Contraseña: ")
        
        # 1. Guardamos el resultado (puede ser un String de error o el Objeto Usuario)
        resultado_login = Usuario.validarLogin(username, password)
        
        # 2. FILTROS DE ERROR: Evaluamos si es un String de error
        if resultado_login == "USUARIO_INCORRECTO":
            print("❌ El nombre de usuario ingresado no existe.")
            
        elif resultado_login == "PASSWORD_INCORRECTO":
            print("❌ Contraseña incorrecta. Intente de nuevo.")
            
        elif resultado_login is None:
            print("❌ Error: El sistema devolvió un valor vacío.")
            
        else:
            # 3. ÉXITO: Si no es ninguno de los anteriores, garantizamos que es el Objeto Usuario
            user_sesion = resultado_login
            rol = user_sesion.tipo_usuario.lower() # <-- Aquí ya NUNCA fallará
            
            # ---------------------------------------------
            # SUB-MENÚS (ADMINISTRADOR o USUARIO)
            # ---------------------------------------------
            if rol == "administrador":
                while True:
                    print(f"\nBienvenido Administrador: {user_sesion.username}")
                    print("1. Registrar usuario  | 2. Listar usuarios")
                    print("3. Buscar usuario     | 4. Modificar usuario")
                    print("5. Eliminar usuario   | 6. Cerrar sesión")
                    opcion_admin = input("Seleccione (1-6): ")
                    
                    if opcion_admin == "1":
                        nom = input("Nuevo username: ")
                        contra = input("Nueva contraseña: ")
                        tipo = int(input("Rol (1: Admin, 2: User): "))
                        nuevo = Usuario(username=nom, password=contra, tipo_usuario=tipo)
                        nuevo.regristrar()
                        print("¡Usuario registrado!")
                        
                    elif opcion_admin == "2":
                        print("\nID\tUsuario\t\tTipo")
                        print("-----------------------------------")
                        for u in Usuario.obtener_todos():
                            print(f"{u.usuario_id}\t{u.username}\t\t{u.tipo_usuario}")
                            
                    elif opcion_admin == "3":
                        print("\n--- [3] Buscar Usuario por ID ---")
                        id_buscado = int(input("Ingrese el ID del usuario: "))
                        
                        # Llamamos al método de la clase
                        u_encontrado = Usuario.buscar_por_id(id_buscado)
                        
                        if u_encontrado is not None:
                            print("\n===============================")
                            print(f"ID:       {u_encontrado.usuario_id}")
                            print(f"Usuario:  {u_encontrado.username}")
                            print(f"Rol/Tipo: {u_encontrado.tipo_usuario}")
                            print("===============================")
                        else:
                            print(f"❌ No se encontró ningún usuario activo con el ID {id_buscado}.")
                    elif opcion_admin == "4":
                        id_mod = int(input("ID a modificar: "))
                        nom = input("Nuevo username: ")
                        contra = input("Nueva contraseña: ")
                        editado = Usuario(usuario_id=id_mod, username=nom, password=contra)
                        editado.modificar()
                        print("¡Usuario actualizado!")
                        
                    elif opcion_admin == "5":
                        print("\n--- [5] Eliminar Usuario ---")
                        id_eliminar = int(input("Ingrese el ID del usuario a eliminar: "))
                        
                        # Desafío Extra: Solicitar confirmación previa
                        confirmacion = input(f"¿Está seguro de que desea eliminar al ID {id_eliminar}? (S/N): ")
                        
                        if confirmacion.upper() == "S":
                            exito = Usuario.eliminar(id_eliminar)
                            if exito:
                                print(f"✅ El usuario con ID {id_eliminar} ha sido eliminado exitosamente.")
                            else:
                                print("❌ No se pudo eliminar. El ID no existe o ya estaba eliminado.")
                        else:
                            print("❌ Operación de eliminación cancelada.")
                        
                    elif opcion_admin == "6":
                        print("Cerrando sesión de administrador...")
                        break
            
            elif rol == "usuario":
                while True:
                    print(f"\nBienvenido {user_sesion.username}\nTipo de usuario: USER")
                    print("1. Cerrar sesión")
                    opcion_user = input("Seleccione: ")
                    
                    if opcion_user == "1":
                        print("Cerrando sesión...")
                        break
    elif opcion == "2":
        print("Saliendo...")
        continuar = False
    
    else:
        print("Opción incorrecta...")