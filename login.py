import connect as con
import bcrypt

def login(username, password):
    try:
        connection = con.connect()
        cursor = connection.cursor()

        query = "SELECT Id_Usuario, Nome, Email FROM usuarios WHERE username = %s"
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
