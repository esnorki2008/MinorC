from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class Goto(Instruccion):

    nombre = None

    def __init__(self, nombre, tupla):
        self.nombre = nombre
        self.tupla = tupla


    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        if Tabla.buscar_etiqueta(self.nombre,self.tupla) is not  None:
            Tabla.nuevo_codigo_3d("goto ETI"+str(self.nombre)+";")

    def str_arbol(self):
        concatenar = ""
        expand = "GOTO: "+self.nombre
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar