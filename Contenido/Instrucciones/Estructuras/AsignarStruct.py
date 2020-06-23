from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class AsignarStruct(Instruccion):
    valor = None
    contenido = None
    nombre = None
    tipo_asignacion = None
    def __init__(self,nombre,contenido,valor,asig,tp):
        self.nombre = nombre
        self.contenido = contenido
        self.valor = valor
        self.tupla=tp
        self.tipo_asignacion = asig

    def ejecutar_3D(self, Tabla):

        valor_exec = self.valor.mi_tempo
        if valor_exec is None:
            valor_exec = self.valor.ejecutar_3D(Tabla)


        vari = Tabla.buscar_temporal(self.nombre, self.tupla, None)
        if vari is not None:
                if not Tabla.struct_busqueda_atributo(vari.tipo, self.contenido, self.tupla):
                    return

                resg = vari.contenido
                vari.contenido=vari.contenido+"[\""+self.contenido+"\"]"
                # temp = vari
                # mi_expresion = temp.temp_str() + "=" + valor_exec.temp_str() + ";"
                if self.tipo_asignacion == "+=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " + " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "-=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " - " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "*=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " * " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "/=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " / " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "%=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " % " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "<<=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " << " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == ">>=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " >> " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "&=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " & " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "^=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " ^ " + str(valor_exec.contenido)+";")
                elif self.tipo_asignacion == "|=":
                    Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " | " + str(valor_exec.contenido)+";")
                else:
                    vari.contenido =resg
                    rst = Tabla.reemplazar_ultimo_codigo_3d(valor_exec.temp_str(), vari.temp_str()+ "[\""+self.contenido+"\"]")
                    if rst is None:
                        mi_expresion = vari.contenido + "[\""+self.contenido+"\"] = " + valor_exec.temp_str() + ";"
                        Tabla.nuevo_codigo_3d(mi_expresion)

                vari.contenido=resg
                # Tabla.nuevo_codigo_3d(mi_expresion)
                #print("MATAR")

    def str_arbol(self):
        pass
