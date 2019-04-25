# sudo apt install python 3
# para instalar un instalador de paquetes de python
# pip3 install requests
# response => respuesta del servidor al usuario
# Codigo de Respuesta bien en el rango de 200
# Codigo de Respuesta mal por ejemplo 404 (rango de 400 aprox)

import requests
from pprint import pprint
"""
URL = "http://www.goole.com/"
respuesta = requests.get(URL)
texto = respuesta.text
print(texto)
a = "Tola mundo"
type(a)
#type retorn el tipo de dato de la variable que le pasas como parametro 


API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Fight Club"
busqueda = URL + API_KEY + "&t=" + titulo

print(busqueda)

respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
pprint(dic_peli)
print(dic_peli["Director"])"""

#Consultar el API de omdb y obtener el nombredel director de Figth Club
#Crear una funcion que reciba como argumento el titulo de una
#pelicula y retorne los actores de la peli

def hallar_actores(argumento_titulo):
    API_KEY = "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    titulo = argumento_titulo
    busqueda = URL + API_KEY + "&t=" + titulo
    respuesta = requests.get(busqueda)
    dic_peli = respuesta.json()
    return dic_peli["Actors"]

print("Los actores de The Matrix son:", hallar_actores("The Matrix"))
nombre_pelicula = input("Ingrese el nombre de una pelicula: ")
actores = hallar_actores(nombre_pelicula)
print(actores)