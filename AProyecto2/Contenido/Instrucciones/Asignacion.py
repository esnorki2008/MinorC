from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class Asignacion(Instruccion):
    valor = None
    nombre = None
    tipo_asignacion = None
    corche = []

    def __init__(self, nombre, valor, tipo_asignacion, tupla, corche=[]):
        self.valor = valor
        self.nombre = nombre
        self.tupla = tupla
        self.tipo_asignacion = tipo_asignacion
        self.corche = corche

    def str_arbol(self):
        concatenar = ""
        expand = "ASIGNAR " + str(self.nombre) + str(self.tipo_asignacion)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.valor.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.valor)) + "\n"
        concatenar += "c"+str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "[]" + "\"]\n"
        concatenar += str(id(self)) + " -> " + "c"+str(id(self))  + "\n"
        for cada in self.corche:
            concatenar += cada.str_arbol()
            concatenar += "c"+str(id(self))  + " -> " + str(id(cada)) + "\n"
        return concatenar

    def ejecutar_3D(self, Tabla):

        valor_exec = self.valor.mi_tempo
        if valor_exec is None:
            valor_exec = self.valor.ejecutar_3D(Tabla)

        for cada in self.nombre:
            vari = Tabla.buscar_temporal(cada, self.tupla, None)
            if vari is not None:
                k_tipo = vari.tipo
                if k_tipo == 3 or k_tipo == 4 or k_tipo == 5:
                    k_tipo = k_tipo - 3;

                if k_tipo != valor_exec.tipo:
                    desc = "Asignacion a una variable de tipo: " + self.tipo_a_str(
                        vari.tipo) + " un valor de tipo: " + self.tipo_a_str(valor_exec.tipo)
                    Tabla.nuevo_error("Eror De Tipos", desc, 0, self.tupla)

                aux = vari.contenido

                # concat=""
                # for cada_cosa in self.corche:
                #    val=cada_cosa.ejecutar_3D(Tabla)
                #    concat = "["+str(val.contenido)+"]"

                concat = ""
                for cor in self.corche:
                    tem = cor.ejecutar_3D(Tabla);
                    if tem.tipo != 0:
                        desc = "Los indices de los arreglos solo pueden ser enteros"
                        Tabla.nuevo_error("Eror De Tipos", desc, 0, self.tupla)
                        return Temporal(0, 0)
                    concat = concat + "[" + str(tem.contenido) + "]"

                vari.contenido = vari.contenido + concat
                # temp = vari
                # mi_expresion = temp.temp_str() + "=" + valor_exec.temp_str() + ";"
                if self.tipo_asignacion == "+=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " + " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "-=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " - " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "*=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " * " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "/=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " / " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "%=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " % " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "<<=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " << " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == ">>=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " >> " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "&=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " & " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "^=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " ^ " + str(valor_exec.contenido) + ";")
                elif self.tipo_asignacion == "|=":
                    Tabla.nuevo_codigo_3d(
                        vari.contenido + " = " + vari.contenido + " | " + str(valor_exec.contenido) + ";")
                else:
                    rst = None
                    rst = Tabla.reemplazar_ultimo_codigo_3d(valor_exec.temp_str(), vari.temp_str())
                    if rst is None:
                        mi_expresion = vari.contenido + " = " + valor_exec.temp_str() + ";"
                        Tabla.nuevo_codigo_3d(mi_expresion)

                vari.contenido = aux

        # return self.contenido
