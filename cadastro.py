import connect as con
import bcrypt as crypt


class Usuario:
    def __init__(self,nome="", email="", senha="", ):
        self.nome = nome
        self.email = email
        self.senha = senha
        

def verificar_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False

def verificar_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

def cadastrar_usuario(usuario):
    cursor = con.connection.cursor()
    sql = "INSERT INTO usuarios (Nome, Email, Senha) VALUES (%s, %s)"
    cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha))
    con.connection.commit()
    cursor.close()
    print("Usuário cadastrado com sucesso!")

def cadastro():
    con.connect()

    nome = input("Digite seu nome: ")


    email = input("Digite seu email: ")
    if not verificar_email(email):
        print("Email inválido.")
        return
    
    senha = input("Digite sua senha: ")
    if not verificar_senha(senha):
        print("Senha inválida. Deve ter pelo menos 8 caracteres.")
        return

    hashed_senha = crypt.hashpw(senha.encode('utf-8'), crypt.gensalt())

    novo_usuario = Usuario(nome, email, hashed_senha)
    cadastrar_usuario(novo_usuario)


