import os
os.system ("cls")
contrania1 = "1234"
contrasenia2 = "a4s1"
user1 = "pedro"
user2 = "angel"
try:
    user1 = str(input("escriba nombre de usuario"))
    user2 = str(input("escriba su nombre de usuario"))
    contrania1 = str(input("escriba su contraseña"))
    contrasenia2 = str(input("escriba su contraseña"))
    if user1 == user1 and contrania1 == contrania1:
        print("acceso correcto")
    elif user2 == user2 and contrasenia2 == contrasenia2:
        print("acceso correcto")
    else:
        print("acceso denegado")
except:
    print("datos incorrectos")