from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncLabel(Instruccion):

    nombre = None

    def __init__(self, nombre, tupla):
        self.nombre = nombre
        self.tupla = tupla


    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        if Tabla.nueva_etiqueta(self.nombre,self.tupla) is  None:
            Tabla.nuevo_codigo_3d("ETI"+str(self.nombre)+":")

    def str_arbol(self):
        concatenar = ""
        expand = "LABEL: "+self.nombre
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar