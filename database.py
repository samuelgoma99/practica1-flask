import sqlite3
DB_NAME = "grup.db"
def get_connection():
	return sqlite3.connect(DB_NAME)
# Inicializamos la base de datos
def init_db():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("""CREATE TABLE IF NOT EXISTS grup (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL)""")
	conn.commit()
	conn.close()
# Funcion que guarda los nombres que introducimos
def guardar_grup(noms):
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("DELETE FROM grup")
	for nom in noms:
		cursor.execute("INSERT INTO grup (nom) VALUES (?)", (nom,))
	conn.commit()
	conn.close()
# Funcion opara mostrar los nombres introducidos
def carregar_grup():
	conn = get_connection()
	cursor = conn.cursor()
	cursor.execute("SELECT nom FROM grup")
	resultats = cursor.fetchall()
	conn.close()
	return [fila[0] for fila in resultats]
