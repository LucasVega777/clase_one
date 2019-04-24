#PARADIGMAS DE LA PROGRAMACION ORIENTADA A OBJETOS

class Dino:
    patas = 4
    nombre = None

    def __init__(self, canti_patas, un_nombre):
        self.patas = canti_patas
        self.nombre = un_nombre
        print("Hola soy un dinosaurio y tengo ", self.patas, "patas, y me llamo", self.nombre)   
    def get_patas(self, cantidad):
        self.patas = cantidad
    def set_patas(self, cantidad):
        self.patas = cantidad
    def cortar_patas(self):
        self.patas = self.patas -1
     
pepito = Dino(4,"Pepito")

