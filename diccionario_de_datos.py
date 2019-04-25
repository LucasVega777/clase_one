import os
os.system("clear")
"""
#Diccionario de datos
diccionario = { }

nombre_de_diccionario = {"Nombre_clave":"valor"}

#Ejemplo lista
persona = ["Marce", 32 , "Programador"]

#Ejemplo Diccionario
dic_persona = {"nombre":"Marce", "edad": 32}
print(dic_persona)

dic_persona["edad"] = "ggggg"
print(dic_persona["edad"])

dic_persona["profesion"] = "Programador"
print(dic_persona)

print(dic_persona["profesion"])

if dic_persona.get("estatura") != None:
    print("Si existe estarura")
else:
    print("No existe la clave estatura")

dic_persona2 = {
                    "nombre":"Lucas",
                    "edad": 20,
                    "peinado":"algo"
                }
print(dic_persona2)

CREAR UN DICCIONARIO PERSONA CON CLAVES NOMBRE
EDAD ESTATURA E IMPRIMIR CADA UNO DE LOS VALORES DE LAS CLAVES EN UN PRINT DIFERENTE
Luego cambiar la edad en otro valor  e imprimir denuevo luego agregar un par clave/error
"""

dic_persona = {
                "nombre": "Lucas",
                "edad": 20,
                "estatura": 1.75
                }

print(dic_persona["nombre"])
print(dic_persona["edad"])
print(dic_persona["estatura"])

dic_persona["edad"] = input("Ingresa una nueva edad: ")

print(dic_persona["nombre"])
print(dic_persona["edad"])
print(dic_persona["estatura"])


if dic_persona.get("peso"):
    print("Existe la clave Peso")
else:
    print("No existe la clave Peso") 

if dic_persona.get("profesion"):
    print("Existe la clave Profesion")
else:
    print("No existe la clave Profesion")

if dic_persona.get("color_ojos"):
    print("Existe la clave color ojos")
else:
    print("No existe la clave color ojos") 

dic_persona["Hobbies"] = ["Jugar","Programar","Dibjuar"]

print(dic_persona)
""" 
lista_claves = ["nombre", "edad", "estatura"]
for clave in lista_claves:
    print(dic_persona[clave])

dic_profe = {
                    "Cant_Alumnos": 25
}

dic_prueba = {
                "Alumno": dic_persona,
                "Profesor": dic_profe
            }
        
print(dic_prueba["Alumno"]["estatura"])"""