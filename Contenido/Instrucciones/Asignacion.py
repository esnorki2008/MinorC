from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class Asignacion(Instruccion):
    valor = None
    nombre = None

    def __init__(self, nombre, valor, tupla):
        self.valor = valor
        self.nombre = nombre
        self.tupla = tupla

    def ejecutar_3D(self, Tabla):
        valor_exec = self.valor.mi_tempo
        if valor_exec is None:
            valor_exec = self.valor.ejecutar_3D(Tabla)

        for cada in self.nombre:
            vari = Tabla.buscar_temporal(cada,self.tupla,None)
            if vari is not None:
                #temp = vari
                #mi_expresion = temp.temp_str() + "=" + valor_exec.temp_str() + ";"
                Tabla.reemplazar_ultimo_codigo_3d(valor_exec.temp_str(),vari.temp_str())
                #Tabla.nuevo_codigo_3d(mi_expresion)
                #print()




        # return self.contenido

    def str_arbol(self):
        pass
