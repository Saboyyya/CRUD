import sqlite3 

DB_NAME = "database.db"
def entrar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    con = entrar()
    cursor = con.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL,email TEXT NOT NULL)""")

    con.commit()
    con.close()