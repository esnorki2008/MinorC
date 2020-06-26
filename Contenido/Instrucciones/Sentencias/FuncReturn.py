from Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncReturn(Instruccion):

    expresion = None
    def __init__(self,expresion, tupla):
        self.tupla = tupla
        self.expresion=expresion

    def str_arbol(self):
        concatenar = ""
        expand = "RETURN"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.expresion.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.expresion)) + "\n"

        return concatenar

    def ejecutar_3D(self, Tabla):
        #print(self.expresion)



        tempo=self.expresion.ejecutar_3D(Tabla)
        self.expresion.pop_retorno(Tabla, tempo.contenido)

        inst = "$v = $v + 1;";
        Tabla.nuevo_codigo_3d(inst)
        inst = " $s2[$v] = "+ tempo.temp_str() + ";#Dando Retorno";
        Tabla.nuevo_codigo_3d(inst)



        Tabla.nuevo_codigo_3d("goto retornos;")

        return "stopu"