from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncBreak(Instruccion):



    def __init__(self, tupla):
        self.tupla = tupla


    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        if self.paso_break is None:
            Tabla.nuevo_error("Error Break","Solo puede usarse en ciclos y switch",0,self.tupla)
            return

        Tabla.nuevo_codigo_3d("goto "+self.paso_break+";")

        return "stopu"

    def str_arbol(self):
        concatenar = ""
        expand = "Break"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar
