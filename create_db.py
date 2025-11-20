import sqlite3

# Conectarse a la base de datos (se creará el archivo si no existe)
conn = sqlite3.connect('zapatenis.db')

# Crear un "cursor" para ejecutar comandos
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL 
);
""")

# Confirmamos los cambios
conn.commit()

# Cerramos la conexión
conn.close()

print("¡Base de datos y tabla 'personas' creadas exitosamente!")