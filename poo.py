#clases
#parece que el codidgo no compila
class humano:
    pass
class mamifero:
    pass
class hola:
    pass

class Persona:
    def __init__(self,nombre,edad,pais):
        self.nombre=nombre
        self.edad=edad
        self.pais=pais
    def hablar(self):
        return "estoy hablando bla bla..."
class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad
    def hablar(self):
        return f"mi habilidad es {self.habilidad}"
        
class Empleado(Persona,Artista):
    def __init__(self,nombre,edad,pais,habilidad,salario):
        Persona.__init__(self,nombre,edad,pais)
        Artista.__init__(self,habilidad)
        self.salario=salario
    def hablar(self):
        return f"pido un salario de {self.salario}"
    
    def guion(self):
        return f"hola yo pido {self.hablar()} y {super().hablar()} ademas mi {Artista.hablar(self)}"
entrevistado=Empleado("juan",25,"chile","cantar",500)
print(entrevistado.guion())
