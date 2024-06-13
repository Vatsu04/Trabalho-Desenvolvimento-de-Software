import bcrypt as crypt

var = "Oi, meu nome é Gustavo"


var_crypt = crypt.hashpw(var.encode('utf-8'), crypt.gensalt())

print(var_crypt)