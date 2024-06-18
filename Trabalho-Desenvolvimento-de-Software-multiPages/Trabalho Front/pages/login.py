import tkinter as tk
from tkinter import ttk
import mysql.connector
import bcrypt
from cadastro import cadastrar_usuario, verificar_email, verificar_senha, Usuario
from login import login
from funcoes import get_user_id

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
def verificar_login(email_login_entry, senha_login_entry, mostrar_pagina, message_label):
    email = email_login_entry.get()
    senha = senha_login_entry.get()
    login_successful, result = login(email, senha)
    
    if login_successful:
        id_user = get_user_id(email)
        message_label.config(text=f"Login bem-sucedido! ID do usuário: {id_user}", foreground="green")
        
        email_login_entry.delete(0, "end")
        senha_login_entry.delete(0, "end")
        mostrar_pagina('ROI')
        
    else:
        message_label.config(text=f"Falha no login: {result}", foreground="red")
        return 0

# Função para registrar um novo usuário
def registrar_usuario(nome_entry, email_entry, senha_entry, mostrar_pagina, message_label):
    nome = nome_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()
    
    connection = connect()
    
    if not connection:
        message_label.config(text="Erro ao conectar ao banco de dados.", foreground="red")
        return
    
    if not verificar_email(email):
        message_label.config(text="Email inválido.", foreground="red")
        return
    
    if not verificar_senha(senha):
        message_label.config(text="Senha inválida. Deve ter pelo menos 8 caracteres.", foreground="red")
        return
    
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
    novo_usuario = Usuario(nome, email, hashed_senha)
    cadastrar_usuario(connection, novo_usuario)
    
    connection.close()
    
    message_label.config(text="Usuário cadastrado com sucesso!", foreground="green")
    
    nome_entry.delete(0, "end")
    email_entry.delete(0, "end")
    senha_entry.delete(0, "end")
    mostrar_pagina('ROI')

def login_page(container, mostrar_pagina):

    # Frames
    main_frame = ttk.Frame(container)
    
    login_frame = ttk.Frame(main_frame)
    login_frame.pack(pady=20)

    cadastro_frame = ttk.Frame(main_frame)
    cadastro_frame.pack(pady=20)
    
    # Labels
    ttk.Label(login_frame, text="Email: ").grid(row=0, column=0, padx=10, pady=10)
    ttk.Label(login_frame, text="Senha: ").grid(row=1, column=0, padx=10, pady=10)

    ttk.Label(cadastro_frame, text="Nome: ").grid(row=0, column=0, padx=10, pady=10)
    ttk.Label(cadastro_frame, text="Email: ").grid(row=1, column=0, padx=10, pady=10)
    ttk.Label(cadastro_frame, text="Senha: ").grid(row=2, column=0, padx=10, pady=10)

    # Entries
    email_login_entry = ttk.Entry(login_frame, width=30)
    email_login_entry.grid(row=0, column=1, padx=10, pady=10)
    senha_login_entry = ttk.Entry(login_frame, width=30, show="*")
    senha_login_entry.grid(row=1, column=1, padx=10, pady=10)

    nome_entry = ttk.Entry(cadastro_frame, width=30)
    nome_entry.grid(row=0, column=1, padx=10, pady=10)
    email_entry = ttk.Entry(cadastro_frame, width=30)
    email_entry.grid(row=1, column=1, padx=10, pady=10)
    senha_entry = ttk.Entry(cadastro_frame, width=30, show="*")
    senha_entry.grid(row=2, column=1, padx=10, pady=10)

    # Mensagem
    message_label = ttk.Label(main_frame, text="", foreground="red")
    message_label.pack(pady=10)
    
    # Botões
    login_button = ttk.Button(login_frame, text="Login", command=lambda:verificar_login(email_login_entry, senha_login_entry, mostrar_pagina, message_label))
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    cadastro_button = ttk.Button(cadastro_frame, text="Cadastrar", command=lambda:registrar_usuario(nome_entry, email_entry, senha_entry, mostrar_pagina, message_label))
    cadastro_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    return main_frame
