import mysql.connector 
import bcrypt
import getpass

def connect():
    connection = mysql.connector.connect(host="localhost", user="root", password="", database="financeiro")
    if connection.is_connected():
        print("Connected successfully")
        return connection
    else:
        print("Failed to connect")
        return None

def login(username, password):
    try:
        connection = connect()
        if connection is None:
            return False, "Failed to connect to the database"
        
        cursor = connection.cursor()

        query = "SELECT Id_Usuario, Nome, Email, Senha FROM usuarios WHERE Email = %s"
        cursor.execute(query, (username,))
        user_record = cursor.fetchone()
        
        if user_record is None:
            return False, "Username not found"
        
        user_id, db_name, db_email, db_password = user_record

        if bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
            return True, user_id
        else:
            return False, "Incorrect password"
    
    except Exception as e:
        return False, str(e)
    
    finally:
        cursor.close()
        connection.close()

def log_in():
    email = input("Digite seu email de usuário: ")
    password = getpass.getpass("Digite sua senha: ")
    login_successful, result = login(email, password)
    if login_successful:
        print(f"Login bem-sucedido! ID do usuário: {result}")
        return True
    else:
        print(f"Falha no login: {result}")
        return False
