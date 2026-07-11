from conexion import obtener_conexion

def agregar_producto(nombre, cantidad, precio):
    """Inserta un nuevo producto en la base de datos"""
    bd = obtener_conexion()
    if bd != None:
        cursor = bd.cursor()
        
        # TODO: Completa la consulta SQL
        sql = "___ INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
        valores = (nombre, cantidad, precio)
        
        cursor.execute(sql, valores)
        # TODO: Guarda los cambios
        bd.___()
        print(f"Éxito: {nombre} guardado en la base de datos.")
        bd.close()

def obtener_inventario():
    """Lee y devuelve todos los productos"""
    bd = obtener_conexion()
    if bd != None:
        cursor = bd.cursor()
        
        # TODO: Completa la consulta SQL para leer todo
        sql = "___ * FROM ___"
        cursor.execute(sql)
        
        resultados = cursor.fetchall()
        bd.close()
        
        return resultados

def eliminar_producto(id_producto):
    """Elimina un producto basándose en su ID"""
    bd = obtener_conexion()
    if bd != None:
        cursor = bd.cursor()
        
        # TODO: Completa la consulta SQL para borrar usando el id
        sql = "___ FROM productos WHERE ___ = %s"
        
        cursor.execute(sql, (id_producto,))
        bd.commit()
        print(f"Éxito: Producto {id_producto} eliminado.")
        bd.close()