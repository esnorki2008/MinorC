from Contenido.Instrucciones.InstruccionAbstracta import Instruccion

class Hoja(Instruccion):
    contenido=None

    def __init__(self, contenido,tupla):
        self.contenido = contenido
        self.tipo=contenido.tipo
        self.tupla=tupla

    def ejecutar_3D(self,Tabla):
        return self.contenido

    def str_arbol(self):
        pass
