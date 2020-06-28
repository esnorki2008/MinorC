from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncSwitch(Instruccion):
    param = None
    cuerpo_switch = None

    def str_arbol(self):
        concatenar = ""
        expand = "SWITCH"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.param.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.param)) + "\n"
        for cada in self.cuerpo_switch:
            concatenar += cada.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(cada)) + "\n"
        return concatenar

    def __init__(self, param, cuerpo_switch,tupla):
        self.cuerpo_switch = cuerpo_switch
        self.param = param
        self.tupla = tupla

    def ejecutar_3D(self, Tabla):
        temp = self.param.ejecutar_3D(Tabla);
        mi_eti = "out"+str(id(self))
        defa = None



        for cada in self.cuerpo_switch:
            cada.paso_continue = self.paso_continue
            cada.paso_break = mi_eti
            if cada.param is not None:
                novo = TablaDeSimbolos(Tabla)
                cada.ejecutar_3D(novo,temp,mi_eti)

            else:
                defa = cada

        novo = TablaDeSimbolos(Tabla)
        if defa is not None:
            defa.ejecutar_3D(novo, temp,mi_eti)
        Tabla.nuevo_codigo_3d(mi_eti+":")


