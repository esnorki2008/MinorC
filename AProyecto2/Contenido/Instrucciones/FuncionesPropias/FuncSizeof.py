from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncSizeof(Instruccion):

    expre = None
    tipo_fijo = None
    def __init__(self,expre, tupla,tipo_fijo=None):
        self.tupla = tupla
        self.expre = expre
        self.tipo_fijo=tipo_fijo

    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        novo_tempo=Temporal(None,0,Tabla.nuevo_correlativo())
        tama = 20
        
        mid = self.tipo_fijo
        if self.tipo_fijo is None:
            execu = self.expre.ejecutar_3D(Tabla)
            mid = execu.tipo

        
        if mid == 1:
                tama =8
        elif mid ==2:
                tama = 1
        elif mid ==0:
                tama = 4
        else:
                tama =20      

        Tabla.nuevo_codigo_3d(novo_tempo.contenido+" = "+str(tama)+";")
        return novo_tempo

    def str_arbol(self):
        concatenar = ""
        expand = "SIZEOF"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar
