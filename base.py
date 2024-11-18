import mysql.connector

class CConexion:
    @staticmethod
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(
                user="root",
                password="santi2005@",
                host="localhost",
                database="tiendita",
                port=3306
            )
            print("Conexión Correcta")
            return conexion
        except mysql.connector.Error as error:
            print(f"Error al conectarse a la base de datos: {error}")
            return None

# Función para insertar datos en la tabla `categorias`
def insertar_categoria(cod_categoria, categoria):
    try:
        conexion = CConexion.ConexionBaseDeDatos()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO categorias (cod_categoria, categoria) VALUES (%s, %s);"
            valores = (cod_categoria, categoria)
            cursor.execute(query, valores)
            conexion.commit()
            print("Categoría insertada correctamente.")
            cursor.close()
            conexion.close()
    except mysql.connector.Error as error:
        print(f"Error al insertar categoría: {error}")

# Función para insertar datos en la tabla `productos`
def insertar_producto(cod_producto, producto, cod_categoria):
    try:
        conexion = CConexion.ConexionBaseDeDatos()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO productos (cod_producto, producto, cod_categoria) VALUES (%s, %s, %s);"
            valores = (cod_producto, producto, cod_categoria)
            cursor.execute(query, valores)
            conexion.commit()
            print("Producto insertado correctamente.")
            cursor.close()
            conexion.close()
    except mysql.connector.Error as error:
        print(f"Error al insertar producto: {error}")

# Función para mostrar todas las categorías
def mostrar_categorias():
    try:
        conexion = CConexion.ConexionBaseDeDatos()
        if conexion:
            cursor = conexion.cursor()
            query = "SELECT * FROM categorias;"
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Categorías:")
            for fila in resultados:
                print(f"ID: {fila[0]}, Categoría: {fila[1]}")
            cursor.close()
            conexion.close()
    except mysql.connector.Error as error:
        print(f"Error al mostrar categorías: {error}")

# Función para mostrar todos los productos
def mostrar_productos():
    try:
        conexion = CConexion.ConexionBaseDeDatos()
        if conexion:
            cursor = conexion.cursor()
            query = """
                SELECT p.cod_producto, p.producto, c.categoria 
                FROM productos p 
                JOIN categorias c ON p.cod_categoria = c.cod_categoria;
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            print("Productos:")
            for fila in resultados:
                print(f"Producto ID: {fila[0]}, Producto: {fila[1]}, Categoría: {fila[2]}")
            cursor.close()
            conexion.close()
    except mysql.connector.Error as error:
        print(f"Error al mostrar productos: {error}")

# Insertar categorías
insertar_categoria(1, "Frutas")
insertar_categoria(2, "Verduras")
insertar_categoria(4, "Tuberculos")

# Insertar productos
insertar_producto(101, "Manzana", 1)
insertar_producto(102, "Lechuga", 2)
insertar_producto(108, "papa", 4)

# Mostrar datos
mostrar_categorias()
mostrar_productos()

    