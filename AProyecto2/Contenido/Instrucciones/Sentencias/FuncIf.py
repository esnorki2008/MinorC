from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos


class FuncIf(Instruccion):
    param = None
    cuerpo_si = None
    cuerpo_no = None

    def __init__(self, param, cuerpo_si, cuerpo_no, tupla):
        self.cuerpo_si = cuerpo_si
        self.cuerpo_no = cuerpo_no
        self.param = param
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "IF"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.param.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.param)) + "\n"
        concatenar += self.cuerpo_si.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.cuerpo_si)) + "\n"
        if self.cuerpo_no is not None:
            concatenar += self.cuerpo_no.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(self.cuerpo_no)) + "\n"
        return concatenar

    def ejecutar_3D(self, Tabla):
        novo = TablaDeSimbolos(Tabla)
        valor_exec = self.param.mi_tempo
        if valor_exec is None:
            valor_exec = self.param.ejecutar_3D(novo)
        if valor_exec.tipo != 0:
            novo.nuevo_error("Error De Tipo", "solo se aceptan tipos enteros en la condicional del IF", 0, self.tupla)

        if self.cuerpo_no is None:
            self.cuerpo_si.paso_continue = self.paso_continue
            self.cuerpo_si.paso_break = self.paso_break
        else:
            self.cuerpo_si.paso_continue = self.paso_continue
            self.cuerpo_si.paso_break = self.paso_break
            self.cuerpo_no.paso_continue = self.paso_continue
            self.cuerpo_no.paso_break = self.paso_break

        if self.nombre_padre is None:
            nombre_if = "label" + str(id(self))

            if self.cuerpo_no is None:
                condicional = "if (!" + valor_exec.temp_str() + ") goto out" + nombre_if + " ;"
                Tabla.nuevo_codigo_3d(condicional)
                novo = TablaDeSimbolos(Tabla)
                self.cuerpo_si.ejecutar_3D(novo)
                condicional = "out" + nombre_if + ": "
                Tabla.nuevo_codigo_3d(condicional)
            else:
                condicional = "if (!" + valor_exec.temp_str() + ") goto out" + str(id(self.cuerpo_no)) + " ;"
                Tabla.nuevo_codigo_3d(condicional)
                novo = TablaDeSimbolos(Tabla)
                self.cuerpo_si.ejecutar_3D(novo)
                condicional = "goto out" + nombre_if + "; "
                Tabla.nuevo_codigo_3d(condicional)
                condicional = "out" + str(id(self.cuerpo_no)) + ": "
                Tabla.nuevo_codigo_3d(condicional)
                novo = TablaDeSimbolos(Tabla)
                self.cuerpo_no.nombre_padre = nombre_if
                self.cuerpo_no.ejecutar_3D(novo)
                condicional = "out" + nombre_if + ": "
                Tabla.nuevo_codigo_3d(condicional)
        else:
            nombre_if = "label" + str(id(self))
            if self.cuerpo_no is None:
                condicional = "if (!" + valor_exec.temp_str() + ") goto out" + self.nombre_padre + " ;"
                Tabla.nuevo_codigo_3d(condicional)
                novo = TablaDeSimbolos(Tabla)
                self.cuerpo_si.ejecutar_3D(novo)
            else:
                condicional = "if (!" + valor_exec.temp_str() + ") goto out" + str(id(self.cuerpo_no)) + " ;"
                Tabla.nuevo_codigo_3d(condicional)
                novo = TablaDeSimbolos(Tabla)
                self.cuerpo_si.ejecutar_3D(novo)
                condicional = "goto out" + self.nombre_padre + "; "
                Tabla.nuevo_codigo_3d(condicional)
                condicional = "out" + str(id(self.cuerpo_no)) + ": "
                Tabla.nuevo_codigo_3d(condicional)
                novo = TablaDeSimbolos(Tabla)
                self.cuerpo_no.nombre_padre = self.nombre_padre
                self.cuerpo_no.ejecutar_3D(novo)

                # condicional = "out" + nombre_if + ": "
                # Tabla.nuevo_codigo_3d(condicional)
