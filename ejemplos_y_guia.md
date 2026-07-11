# Miniguía: ¿Cómo usar las funciones de tu CRUD?

En este laboratorio tenemos dos archivos trabajando en equipo. Piensa que tu app.py es el Mesero (habla con el cliente) y tu operaciones.py es el Cocinero (habla con la base de datos).

Para que el mesero le pase órdenes al cocinero, usamos el comando import operaciones. Aquí tienes 3 ejemplos de cómo usarlo para que no te pierdas al programar tu menú:

# Pista 1: Enviar datos a la base de datos (INSERT)

Cuando quieres guardar algo, primero le pides los datos al usuario con input(). Recuerda: Si la base de datos espera números, debes convertir el texto usando int() o float().

Ejemplo (Sistema de Empleados):

# 1. Pedimos datos
nombre_emp = input("Nombre del empleado: ")
edad_emp = int(input("Edad: ")) # Convertimos a entero

# 2. Llamamos a la función y le pasamos las variables en los paréntesis
operaciones.agregar_empleado(nombre_emp, edad_emp)


# Pista 2: Recibir datos y mostrarlos (SELECT)

Cuando la base de datos te devuelve información (como al ver un inventario), te devuelve una Lista. No puedes imprimirla directamente, tienes que usar un ciclo for para recorrerla y mostrarla bonito.

Ejemplo (Sistema de Empleados):

# 1. Llamamos a la función y GUARDAMOS su respuesta en una variable
lista_de_empleados = operaciones.obtener_todos_los_empleados()

# 2. Usamos un 'for' para imprimir uno por uno
for empleado in lista_de_empleados:
    # empleado[0] es el ID, empleado[1] es el nombre, etc.
    print(f"ID: {empleado[0]} | Nombre: {empleado[1]}")


(Usa esta pista para resolver la Opción 2 del menú)

# Pista 3: Borrar usando un ID (DELETE)

Para borrar algo, la base de datos solo necesita saber el id (el número único). Solo pide ese número y pásaselo a la función.

Ejemplo (Sistema de Empleados):

# 1. Pedimos el ID y lo convertimos a entero
id_despedir = int(input("Ingresa el ID del empleado a borrar: "))

# 2. Le pasamos el número al cocinero (CRUD)
operaciones.eliminar_empleado(id_despedir)


(Usa esta pista para resolver la Opción 3 del menú)