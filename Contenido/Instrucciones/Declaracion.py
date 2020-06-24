from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class Declaracion(Instruccion):
    valor = None
    nombre = None
    corche = None
    def __init__(self, nombre, valor, tipo, tupla,corche = []):
        self.valor = valor
        self.nombre = nombre
        self.tipo = tipo
        self.tupla = tupla
        self.corche = corche

    def ejecutar_arreglo(self,Tabla):
        lista_val = []
        for cor in self.corche:
            tem=cor.ejecutar_3D(Tabla);
            if tem.tipo != 0:
                desc = "Los indices de los arreglos solo pueden ser enteros"
                Tabla.nuevo_error("Eror De Tipos", desc, 0, self.tupla)
                return
            lista_val.append(tem)

        temp = Temporal(None, self.tipo+3, correlativo=Tabla.nuevo_correlativo())
        temp.lista_corchetes=lista_val
        mi_expresion = temp.temp_str() + "=" +  " array();"
        Tabla.nuevo_codigo_3d(mi_expresion)
        Tabla.nuevo_temporal(self.nombre[0], temp)

    def ejecutar_3D(self, Tabla ):
        if len(self.corche) != 0:
            return  self.ejecutar_arreglo(Tabla)

        valor_exec = None
        if self.valor is None:
            valor_exec = Temporal(0,0)
        else:
            valor_exec = self.valor.mi_tempo
            if valor_exec is None:
                valor_exec = self.valor.ejecutar_3D(Tabla)

            self.valor.pop_retorno(Tabla,valor_exec.contenido)

        if self.tipo != valor_exec.tipo:
            desc="Asignacion a una variable de tipo: "+self.tipo_a_str(self.tipo)+" un valor de tipo: "+self.tipo_a_str(valor_exec.tipo)
            Tabla.nuevo_error("Eror De Tipos",desc,0,self.tupla)

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
