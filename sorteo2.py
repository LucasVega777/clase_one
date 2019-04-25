from random import  randint 
import os
os.system("clear")
#hacer un sorteo para 5 personas y hay tres premios
#una persona no puede ganar dos veces
cant_personas = 5

parti = ["Pepito", "Nemo", "Rodi", "Dino", "GRshits" ]
cant_premios = 3
for k in range(cant_premios):
    indice_ganador = randint(0 , cant_personas - 1)
    print("Ganador N°", k+1,":", parti[indice_ganador])
    parti.pop(indice_ganador)
    cant_personas -= 1
