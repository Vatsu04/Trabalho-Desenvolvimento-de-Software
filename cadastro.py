import mysql.connector 
import bcrypt as crypt
import getpass

def connect():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="financeiro")
    if connection.is_connected():
        print("Connected successfully")
        return connection
    else:
        print("Failed to connect")
        return None

class Usuario:
    def __init__(self, nome="", email="", senha=""):
        self.nome = nome
        self.email = email
        self.senha = senha

def verificar_senha(senha):
    return len(senha) >= 8

def verificar_email(email):
    return "@" in email and "." in email

def cadastrar_usuario(connection, usuario):
    cursor = connection.cursor()
    sql = "INSERT INTO usuarios (Nome, Email, Senha) VALUES (%s, %s, %s)"
    cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha))
    connection.commit()
    cursor.close()
    print("Usuário cadastrado com sucesso!")
    return True




