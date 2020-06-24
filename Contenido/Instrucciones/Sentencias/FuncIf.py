from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncIf(Instruccion):
    param = None
    cuerpo_si = None
    cuerpo_no = None

    def __init__(self, param, cuerpo_si,cuerpo_no,tupla):
        self.cuerpo_si = cuerpo_si
        self.cuerpo_no = cuerpo_no
        self.param = param
        self.tupla = tupla

    def ejecutar_3D(self, Tabla):


        novo = TablaDeSimbolos(Tabla)

        nombre_if = "label" + str(id(self))
        nombre_salida =nombre_if
        if self.nombre_padre is not None:
            nombre_salida = self.nombre_padre


        #novo.nuevo_codigo_3d(nombre_if+":")
        valor_exec = self.param.mi_tempo
        if valor_exec is None:
            valor_exec = self.param.ejecutar_3D(novo)

        if valor_exec.tipo != 0:
            novo.nuevo_error("Error De Tipo","solo se aceptan tipos enteros en la condicional del IF",0,self.tupla)

        condicional="if (!"+valor_exec.temp_str()+") goto out"+nombre_if+" ;"
        if self.cuerpo_no is None:
            condicional = "if (!" + valor_exec.temp_str() + ") goto outs" + nombre_salida + " ;"

        novo.nuevo_codigo_3d(condicional)
        #self.cuerpo_si.nombre_padre = nombre_if
        self.cuerpo_si.ejecutar_3D(novo)
        if(self.cuerpo_no is not None):
            novo.nuevo_codigo_3d("goto outs" + nombre_salida + ";")

        if self.cuerpo_no is not None:
            self.cuerpo_no.nombre_padre = nombre_if
            novo.nuevo_codigo_3d("out" + nombre_if + ":")
            self.cuerpo_no.ejecutar_3D(novo)

        if nombre_salida == nombre_if:
            novo.nuevo_codigo_3d("outs" + nombre_salida + ":")


        # return self.contenido

    def str_arbol(self):
        pass
