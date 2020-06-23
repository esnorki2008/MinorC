from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class Declaracion(Instruccion):
    valor = None
    nombre = None

    def __init__(self, nombre, valor, tipo, tupla):
        self.valor = valor
        self.nombre = nombre
        self.tipo = tipo
        self.tupla = tupla

    def ejecutar_3D(self, Tabla):
        valor_exec = None
        if self.valor is None:
            valor_exec = Temporal(0,0)
        else:
            valor_exec = self.valor.mi_tempo
            if valor_exec is None:
                valor_exec = self.valor.ejecutar_3D(Tabla)

            self.valor.pop_retorno(Tabla,valor_exec.contenido)

        ver_tipo = valor_exec.tipo
        for cada in self.nombre:
            temp = Temporal(None, ver_tipo, correlativo=Tabla.nuevo_correlativo())
            mi_expresion = temp.temp_str() + "= 0;"
            if self.nombre[-1] == cada:
                    mi_expresion = temp.temp_str() + "=" + valor_exec.temp_str() + ";"

            rst = Tabla.reemplazar_ultimo_codigo_3d(valor_exec.temp_str(), temp.temp_str())
            if rst is None:
                Tabla.nuevo_codigo_3d(mi_expresion)
            #Tabla.nuevo_codigo_3d(mi_expresion)
            Tabla.nuevo_temporal(cada, temp)

        # return self.contenido

    def str_arbol(self):
        pass
