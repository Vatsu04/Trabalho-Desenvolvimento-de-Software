import mysql.connector 

connection = mysql.connector.connect(host="localhost", user="root", password="", database="financeiro")

if connection.is_connected():
    print("Connected Succesfully")
else:
    print("Failed to connect")


#Perform db operations

#connection.close()