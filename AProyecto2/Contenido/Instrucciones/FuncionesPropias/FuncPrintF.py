from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncPrintF(Instruccion):

    lst_param: [] = None

    def __init__(self, lista_parametros, tupla):
        self.lst_param = lista_parametros
        self.tupla = tupla

    def agregar(self, item):
        self.contenido.append(item)

    def ejecutar_3D(self, Tabla):
        novo = TablaDeSimbolos(Tabla)
        lons = len(self.lst_param)
        conta =0
        for each in self.lst_param:
            if conta >0 or lons == 1:
                eti_temp=each.ejecutar_3D(novo).temp_str()
                inst="print( "+eti_temp+" );"
                novo.nuevo_codigo_3d(inst)
            conta = conta+1;

    def str_arbol(self):
        concatenar = ""
        expand = "PRINTF"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar