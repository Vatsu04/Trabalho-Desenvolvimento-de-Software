import tkinter as tk
from tkinter import messagebox
import mysql.connector
import bcrypt
import getpass
import cadastro
import login
import funcoes

# Função para conectar ao banco de dados
def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="financeiro"
        )
        print("Connected successfully")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Função para verificar o login
def verificar_login():
    email = email_login_entry.get()
    senha = senha_login_entry.get()
    login_successful, result = login.login(email, senha)
    if login_successful:
        id_user = funcoes.get_user_id(email)
        messagebox.showinfo("Login", f"Login bem-sucedido! ID do usuário: {id_user}")
    else:
        messagebox.showerror("Login", f"Falha no login: {result}")

# Função para registrar um novo usuário
def registrar_usuario():
    nome = nome_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()
    
    connection = connect()
    if not connection:
        return
    
    if not cadastro.verificar_email(email):
        messagebox.showerror("Cadastro", "Email inválido.")
        return
    
    if not cadastro.verificar_senha(senha):
        messagebox.showerror("Cadastro", "Senha inválida. Deve ter pelo menos 8 caracteres.")
        return
    
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    novo_usuario = cadastro.Usuario(nome, email, hashed_senha)
    cadastro.cadastrar_usuario(connection, novo_usuario)
    connection.close()
    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

# Interface gráfica com tkinter
root = tk.Tk()
root.title("Matemática financeira")

# Frames
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

cadastro_frame = tk.Frame(root)
cadastro_frame.pack(pady=20)

# Labels
tk.Label(login_frame, text="Email: ").grid(row=0, column=0, padx=10, pady=10)
tk.Label(login_frame, text="Senha: ").grid(row=1, column=0, padx=10, pady=10)

tk.Label(cadastro_frame, text="Nome: ").grid(row=0, column=0, padx=10, pady=10)
tk.Label(cadastro_frame, text="Email: ").grid(row=1, column=0, padx=10, pady=10)
tk.Label(cadastro_frame, text="Senha: ").grid(row=2, column=0, padx=10, pady=10)

# Entries
email_login_entry = tk.Entry(login_frame, width=30)
email_login_entry.grid(row=0, column=1, padx=10, pady=10)
senha_login_entry = tk.Entry(login_frame, width=30, show="*")
senha_login_entry.grid(row=1, column=1, padx=10, pady=10)

nome_entry = tk.Entry(cadastro_frame, width=30)
nome_entry.grid(row=0, column=1, padx=10, pady=10)
email_entry = tk.Entry(cadastro_frame, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=10)
senha_entry = tk.Entry(cadastro_frame, width=30, show="*")
senha_entry.grid(row=2, column=1, padx=10, pady=10)

# Botões
login_button = tk.Button(login_frame, text="Login", command=verificar_login)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

cadastro_button = tk.Button(cadastro_frame, text="Cadastrar", command=registrar_usuario)
cadastro_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()