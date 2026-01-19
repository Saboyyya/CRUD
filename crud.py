from database import entrar

def criar_usuario():
    con = entrar()
    cursor = con.cursor()

    cursor.execute("INSERT INTO USUARIOS (nome,email) VALUES (?,?)")
    
    con.commit()
    con.close()

def listar_usuario():
    con = entrar()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM USUARIOS")
    usuarios = cursor.fetchall()
    con.close()
    return usuarios 
def atualizar_usuario(nome,email):
    con = entrar()
    cursor = con.cursor()

    cursor.execute("UPDATE usuarios SET nome = ?, email = ?, WHERE id = ?",(nome,email,id))

def deletar_usuario():
    con = entrar()
    cursor = con.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?")
    
    con.commit()
    con.close()
