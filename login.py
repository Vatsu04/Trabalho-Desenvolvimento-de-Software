import connect as con
import bcrypt

def login(username, password):
    try:
        connection = con.connect()
        cursor = connection.cursor()

        query = "SELECT Id_Usuario, username, password FROM Usuarios WHERE username = %s"
        cursor.execute(query, (username,))
        user_record = cursor.fetchone()
        
        if user_record is None:
            return False, "Username not found"
        
        user_id, db_username, db_password = user_record

        if bcrypt.checkpw(password.encode('utf-8'), db_password.encode('utf-8')):
            return True, user_id
        else:
            return False, "Incorrect password"
    
    except Exception as e:
        return False, str(e)
    
    finally:
        cursor.close()
        connection.close()
username = input("Enter your username: ")
password = input("Enter your password: ")
login_successful, result = login(username, password)
if login_successful:
    print(f"Login successful! User ID: {result}")
else:
    print(f"Login failed: {result}")
