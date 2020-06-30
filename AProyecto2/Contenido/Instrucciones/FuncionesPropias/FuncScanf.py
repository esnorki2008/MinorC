from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncScanF(Instruccion):



    def __init__(self, tupla):
        self.tupla = tupla


    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        novo_tempo=Temporal(None,0,Tabla.nuevo_correlativo())
        Tabla.nuevo_codigo_3d(novo_tempo.contenido+" = read();")
        return novo_tempo

    def str_arbol(self):
        concatenar = ""
        expand = "SCANF"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar
