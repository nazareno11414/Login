import sqlite3 as bd

con=bd.connect('Usuarios.db')
cur=con.cursor()
cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            nombre TEXT NOT NULL,
            telefono NUMBER,
            email TEXT NOT NULL,
            contraseña TEXT NOT NULL
        )
        ''')
"""cur.execute('DROP TABLE usuarios')
con.commit()"""
cur.close()



def buscar_usuario(email,contraseña):
    con=bd.connect('Usuarios.db')
    cur=con.cursor()
    
    user=cur.execute(
        "SELECT email,contraseña FROM usuarios WHERE email=? AND contraseña=?",(email,contraseña)
    )
    usuarios=user.fetchall()
    cur.close()
    if usuarios and usuarios[0][0]==email and usuarios[0][1]==contraseña:
        return True
    else:
        return False
    
def registrar(nombre, telefono, email, contraseña):
    con = bd.connect('Usuarios.db')
    cur = con.cursor()
    
    try:
        cur.execute("SELECT email FROM usuarios WHERE email=?", (email,))
        user = cur.fetchall()
        
        if user:
            return False
        
        cur.execute(
            "INSERT INTO usuarios (nombre, telefono, email, contraseña) VALUES (?, ?, ?, ?)",
            (nombre, telefono, email, contraseña)
        )
        con.commit()
    except Exception as e:
        return False
    finally:
        cur.close()
        con.close()
    
    return True