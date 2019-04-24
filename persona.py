#lo que estaba en persona.py crear una Clase persona con 
# atributo nombre
# despues instanciar un objeto de tipo persona
class Persona:
    nombre = None
    edad = None

    def __init__(self, un_nombre, una_edad):
        self.nombre = un_nombre
        self.edad = una_edad
        print("Hola soy", self.nombre, "y tengo ", self.edad, "anhos")
    def get_edad(self):
        return self.edad
    def cumple_anhos(self):
        self.edad = self.edad + 1
        return self.edad


persona1 = Persona("Lucas", 20)
print(persona1.cumple_anhos())
persona1.get_edad()


#modificar la clase de persona agregarle 
#un atributo de edad y un metodo cumple_anhos y un metodo get_edad
#inicializar un objeto de tipo persona 
#y hacerle cumplir anhos

