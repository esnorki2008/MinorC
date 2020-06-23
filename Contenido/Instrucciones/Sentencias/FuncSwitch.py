from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncSwitch(Instruccion):
    param = None
    cuerpo_switch = None

    def __init__(self, param, cuerpo_switch,tupla):
        self.cuerpo_switch = cuerpo_switch
        self.param = param
        self.tupla = tupla

    def ejecutar_3D(self, Tabla):
        temp = self.param.ejecutar_3D(Tabla);
        mi_eti = "out"+str(id(self))
        defa = None
        for cada in self.cuerpo_switch:
            if cada.param is not None:
                novo = TablaDeSimbolos(Tabla)
                cada.ejecutar_3D(novo,temp,mi_eti)
            else:
                defa = cada

        novo = TablaDeSimbolos(Tabla)
        defa.ejecutar_3D(novo, temp,mi_eti)
        Tabla.nuevo_codigo_3d(mi_eti+":")

    def str_arbol(self):
        pass
