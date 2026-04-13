import os 
os.system("cls")
respuesta = 0
try:
    pregunta = int(input("cual de los siguientes animales vive en el agua?, opcion a) Perro, b) Cocodrilo, c) Conejo, D) Tiburon, escriba por orden el numero correspondiente, ej: perro = 1"))
    if pregunta == 2:
        respuesta =+ 0.5
    elif pregunta == 4:
        respuesta =+ 1.0
    else:
        respuesta == 0
    puntaje = print(f"el putnaje obtenido es {respuesta}")
except:
    print("datos invalidos")    