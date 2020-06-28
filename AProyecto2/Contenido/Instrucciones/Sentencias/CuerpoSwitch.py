from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class CuerpoSwitch(Instruccion):
    param = None
    cuerpo_si = None

    def __init__(self, param, cuerpo_si,tupla):
        self.cuerpo_si = cuerpo_si
        self.param = param
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "CASE"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.param.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.param)) + "\n"
        concatenar += self.cuerpo_si.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.cuerpo_si)) + "\n"

        return concatenar

    def ejecutar_3D(self, Tabla, temp_padre ,eti_padre):
        if self.param is not None:
            temp = self.param.ejecutar_3D(Tabla);
            nombre_switch= "out"+str(id(self))
            condicional = "if (" + str(temp_padre.contenido) + " != "+ str(temp .contenido)+") goto " + nombre_switch + " ;"
            Tabla.nuevo_codigo_3d(condicional)
            self.cuerpo_si.paso_continue = self.paso_continue
            self.cuerpo_si.paso_break = self.paso_break
            self.cuerpo_si.ejecutar_3D(Tabla)
            condicional = "goto "+eti_padre+";"
            Tabla.nuevo_codigo_3d(condicional)
            condicional = nombre_switch+":"
            Tabla.nuevo_codigo_3d(condicional)
        else:
            self.cuerpo_si.paso_continue = self.paso_continue
            self.cuerpo_si.paso_break = self.paso_break
            self.cuerpo_si.ejecutar_3D(Tabla);


