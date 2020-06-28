from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncContinue(Instruccion):



    def __init__(self, tupla):
        self.tupla = tupla


    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        if self.paso_continue is None:
            Tabla.nuevo_error("Error Continue", "Continue Solo puede usarse en ciclos", 0, self.tupla)
            return

        Tabla.nuevo_codigo_3d("goto " + self.paso_continue + ";")

        return "stopc"

    def str_arbol(self):
        concatenar = ""
        expand = "CONTINUE"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar
