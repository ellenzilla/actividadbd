import mysql.connector

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="AQUI_IP_DEL_SERVIDOR",
            user="AQUI_TU_USUARIO",
            password="AQUI_TU_PASSWORD",
            database="AQUI_NOMBRE_BD"
        )
        return conexion
    except Exception as e:
        print("Error de conexión:", e)
        return None