from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncWhile(Instruccion):
    param = None
    cuerpo = None

    def __init__(self, param, cuerpo,tupla):
        self.cuerpo = cuerpo
        self.param = param
        self.tupla = tupla

    def ejecutar_3D(self, Tabla):
        novo = TablaDeSimbolos(Tabla)
        nombre_ciclo="label"+str(id(self))
        novo.nuevo_codigo_3d(nombre_ciclo+":")
        valor_exec = self.param.mi_tempo
        if valor_exec is None:
            valor_exec = self.param.ejecutar_3D(novo)

        condicional="if ("+valor_exec.temp_str()+" != 1) goto out"+nombre_ciclo+" ;"
        novo.nuevo_codigo_3d(condicional)
        self.cuerpo.ejecutar_3D(novo)
        novo.nuevo_codigo_3d("goto " +nombre_ciclo +";")
        novo.nuevo_codigo_3d("out"+nombre_ciclo+":")
        # return self.contenido

    def str_arbol(self):
        pass
