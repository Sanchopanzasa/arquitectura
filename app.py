import sqlite3
from flask import Flask, request, render_template

# -----------------------------------------------------------------
# 🚨 IMPORTANTE: Necesitarás instalar Flask primero 🚨
# En tu terminal, ejecuta: pip install Flask
# -----------------------------------------------------------------


app = Flask(__name__)

# Ruta 1: Muestra el formulario HTML
@app.route('/')
def index():
    # Busca 'tu_pagina.html' dentro de la carpeta 'templates'
    return render_template('index.html')

# Ruta 2: Recibe los datos del formulario (la ruta del 'action' del form)
@app.route('/create-user', methods=['POST'])
def guardar_datos():
    if request.method == 'POST':
        # Obtener los datos del formulario por su 'name'
        nombre_form = request.form['name']
        email_form = request.form['email']
        password_form = request.form['password']
        # Conectar a la BD SQLite y guardar
        try:
            conn = sqlite3.connect('zapatenis.db')
            cursor = conn.cursor()
            # Usamos '?' para evitar inyección SQL. Es más seguro.
            cursor.execute("INSERT INTO personas (nombre, email, password) VALUES (?, ?, ?)", (nombre_form, email_form, password_form))
            conn.commit()
            conn.close()
            # Puedes mostrar un mensaje de éxito
            return f"<h1>¡Datos guardados con éxito!</h1><p>Nombre: {nombre_form}, Email: {email_form}</p><a href='/'>Volver</a>"       
        except Exception as e:
            # Manejo de errores
            return f"<h1>Error al guardar en la base de datos</h1><p>{e}</p><a href='/'>Volver</a>"

# Esto es para que el servidor se ejecute
if __name__ == '__main__':
    app.run(debug=True) # debug=True te ayuda a ver errores mientras desarrollas