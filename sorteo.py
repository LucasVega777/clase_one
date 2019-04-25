from random import  randint 
import os
os.system("clear")

#hacer un sorteo para 5 personas y hay tres premios
#una persona no puede ganar dos veces
cant_personas = 3

parti = ["Pepito", "Nemo", "Rodi", "Dino", "GRshits" ]
lista_ganadores = []
cant_premios = 3
while cant_premios !=0:
    indice_ganador = randint(0 , cant_personas - 1)
    if not parti [indice_ganador] in lista_ganadores:
        lista_ganadores.append( parti [indice_ganador] )
        cant_premios -= 1
c = 0
for winners in lista_ganadores:
    c +=1
    print("Ganador N°", c,":", winners) 


