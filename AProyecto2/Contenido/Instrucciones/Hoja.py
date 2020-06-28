from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion

class Hoja(Instruccion):
    contenido=None

    def __init__(self, contenido,tupla):
        self.contenido = contenido
        self.tipo=contenido.tipo
        self.tupla=tupla

    def ejecutar_3D(self,Tabla):
        return self.contenido

    def str_arbol(self):
        concatenar = ""
        expand = "HOJA   "+str(self.contenido.contenido)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar
