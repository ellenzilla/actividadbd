import operaciones

def iniciar_sistema():
    print("Iniciando Sistema...")
    

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar un producto nuevo")
        print("2. Mostrar todo el inventario")
        print("3. Eliminar un producto")
        print("4. Apagar sistema")
        
        opcion = input("Elige una opción (1-4): ")
        
        # --- OPCIÓN 1: EJEMPLO RESUELTO ---
        if opcion == "1":
            print("\n--- NUEVO PRODUCTO ---")
            # 1. El mesero pide los datos al usuario
            nombre_nuevo = input("Escribe el nombre: ")
            cantidad_nueva = int(input("Escribe la cantidad: ")) # Convertimos a entero
            precio_nuevo = float(input("Escribe el precio: "))   # Convertimos a decimal
            
            # 2. Le pasamos los datos al "Cocinero" (nuestro CRUD)
            operaciones.agregar_producto(nombre_nuevo, cantidad_nueva, precio_nuevo)
            
        # --- OPCIÓN 2 ---
        elif opcion == "2":
            print("\n--- INVENTARIO ---")
            # TODO: Llama a la función operaciones.obtener_inventario() y guárdala en una variable
            
            # TODO: Crea un ciclo 'for' para recorrer esa variable e imprimir cada producto
            pass # (Borra este 'pass' cuando escribas tu código)
            
        # --- OPCIÓN 3 ---
        elif opcion == "3":
            print("\n--- BORRAR PRODUCTO ---")
            # TODO: Pide al usuario que escriba el ID del producto (recuerda convertirlo a int)
            
            # TODO: Llama a la función operaciones.eliminar_producto() pasándole ese ID
            pass # (Borra este 'pass' cuando escribas tu código)
            
        # --- OPCIÓN 4 ---
        elif opcion == "4":
            print("Apagando sistema... ¡Buen trabajo!")
            # TODO: Escribe el comando para romper el ciclo infinito y salir
            pass # (Borra este 'pass' cuando escribas tu código)
            
        else:
            print("Opción incorrecta. Intenta de nuevo.")

# Esta línea arranca todo el programa
iniciar_sistema()