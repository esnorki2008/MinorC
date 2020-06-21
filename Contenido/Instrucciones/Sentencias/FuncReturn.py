from Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncReturn(Instruccion):

    expresion = None
    def __init__(self,expresion, tupla):
        self.tupla = tupla
        self.expresion=expresion

    def ejecutar_3D(self, Tabla):
        #print(self.expresion)
        tempo=self.expresion.ejecutar_3D(Tabla)
        inst = "$v = " + tempo.temp_str() + ";#Dando Retorno";
        Tabla.nuevo_codigo_3d(inst)
        Tabla.nuevo_codigo_3d("goto retornos;")

    def str_arbol(self):
        pass
