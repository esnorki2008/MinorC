from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncWhile(Instruccion):
    param = None
    cuerpo = None

    def __init__(self, param, cuerpo,tupla):
        self.cuerpo = cuerpo
        self.param = param
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "WHILE"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.param.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.param)) + "\n"
        concatenar += self.cuerpo.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.cuerpo)) + "\n"

        return concatenar

    def ejecutar_3D(self, Tabla):
        novo = TablaDeSimbolos(Tabla)
        nombre_ciclo="label"+str(id(self))
        novo.nuevo_codigo_3d(nombre_ciclo+":")
        valor_exec = self.param.mi_tempo
        if valor_exec is None:
            valor_exec = self.param.ejecutar_3D(novo)

        if valor_exec.tipo != 0:
            novo.nuevo_error("Error De Tipo", "solo se aceptan tipos enteros en la condicional del WHILE", 0, self.tupla)

        condicional="if ("+valor_exec.temp_str()+" != 1) goto out"+nombre_ciclo+" ;"
        novo.nuevo_codigo_3d(condicional)

        self.cuerpo.paso_continue = nombre_ciclo
        self.cuerpo.paso_break = "out" + nombre_ciclo

        self.cuerpo.ejecutar_3D(novo)
        novo.nuevo_codigo_3d("goto " +nombre_ciclo +";")
        novo.nuevo_codigo_3d("out"+nombre_ciclo+":")
        # return self.contenido


