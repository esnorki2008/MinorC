from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos


class FuncFor(Instruccion):
    inst_inicio = None
    comprobador = None
    inst_cada = None
    cuerpo = None

    def __init__(self, inst_inicio, comprobador, inst_cada, cuerpo, tupla):
        self.inst_inicio = inst_inicio
        self.comprobador = comprobador
        self.inst_cada = inst_cada
        self.cuerpo = cuerpo
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "FOR"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.inst_inicio.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.inst_inicio)) + "\n"
        concatenar += self.comprobador.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.comprobador)) + "\n"
        concatenar += self.cuerpo.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.cuerpo)) + "\n"
        if self.inst_cada is not None:
            concatenar += self.inst_cada.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(self.inst_cada)) + "\n"
        return concatenar

    def ejecutar_3D(self, Tabla):
        novo = TablaDeSimbolos(Tabla)
        self.inst_inicio.ejecutar_3D(novo)
        nombre_ciclo = "label" + str(id(self))
        novo.nuevo_codigo_3d(nombre_ciclo + ":")
        valor_exec = self.comprobador.ejecutar_3D(novo)
        if valor_exec.tipo != 0:
            novo.nuevo_error("Error De Tipo", "solo se aceptan tipos enteros en la condicional del FOR", 0, self.tupla)

        condicional = "if (" + valor_exec.temp_str() + " != 1) goto out" + nombre_ciclo + " ;"
        novo.nuevo_codigo_3d(condicional)

        self.cuerpo.paso_continue = nombre_ciclo
        self.cuerpo.paso_break = "out" + nombre_ciclo

        sal=self.cuerpo.ejecutar_3D(novo)
        if self.inst_cada is not None:
            if sal =="stopc":
                rest=novo.caso_continue()
                self.inst_cada.ejecutar_3D(novo)
                novo.nuevo_codigo_3d(rest)
            else:
                self.inst_cada.ejecutar_3D(novo)
                novo.nuevo_codigo_3d("goto " + nombre_ciclo + ";")


        novo.nuevo_codigo_3d("out" + nombre_ciclo + ":")
        # return self.contenido
