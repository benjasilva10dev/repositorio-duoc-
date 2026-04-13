import os 
os.system("cls")
try:
    nota1 = float(input("escriba su primera nota, como decimal"))
    nota2 = float(input("escriba su segunda nota, como decimal"))
    nota3 = float(input("escriba su tercera nota, como decimal"))
    promedio = (nota1 + nota2 + nota3) % 3
    print(f"su promedio es : {promedio}")
except:
    print("formato de notas invalido")
    
