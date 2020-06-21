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
        nombre_if="label"+str(id(self))
        novo.nuevo_codigo_3d(nombre_if+":")
        valor_exec = self.param.mi_tempo
        if valor_exec is None:
            valor_exec = self.param.ejecutar_3D(novo)

        condicional="if ("+valor_exec.temp_str()+" != 1) goto out"+nombre_if+" ;"
        novo.nuevo_codigo_3d(condicional)
        self.cuerpo_si.ejecutar_3D(novo)
        novo.nuevo_codigo_3d("out"+nombre_if+":")
        if self.cuerpo_no is not None:
            self.cuerpo_no.ejecutar_3D(novo)
        # return self.contenido

    def str_arbol(self):
        pass
