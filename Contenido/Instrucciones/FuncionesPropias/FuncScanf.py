from Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncScanF(Instruccion):



    def __init__(self, tupla):
        self.tupla = tupla


    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        novo_tempo=Temporal(None,0,Tabla.nuevo_correlativo())
        Tabla.nuevo_codigo_3d(novo_tempo.contenido+" = read();")
        return novo_tempo

    def str_arbol(self):
        pass
