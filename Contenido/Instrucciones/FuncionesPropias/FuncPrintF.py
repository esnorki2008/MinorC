from Contenido.Instrucciones.InstruccionAbstracta import Instruccion
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncPrintF(Instruccion):

    lst_param: [] = None

    def __init__(self, lista_parametros, tupla):
        self.lst_param = lista_parametros
        self.tupla = tupla

    def agregar(self, item):
        self.contenido.append(item)

    def ejecutar_3D(self, Tabla):
        novo = TablaDeSimbolos(Tabla)
        for each in self.lst_param:
            eti_temp=each.ejecutar_3D(novo).temp_str()
            inst="print( "+eti_temp+" );"
            novo.nuevo_codigo_3d(inst)

    def str_arbol(self):
        pass
