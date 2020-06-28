from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal


class NodoUnario(Instruccion):
    operacion_unica:Instruccion = None
    operando: str = ""

    def __init__(self,operando, operacion_unica,tupla):
        self.operacion_unica = operacion_unica
        self.operando = operando
        self.tupla=tupla

    def str_arbol(self):
        concatenar = ""
        expand =  str(self.operando)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.operacion_unica.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.operacion_unica)) + "\n"
        return concatenar

    def ejecutar_3D(self,Tabla):

        exec_op = self.operacion_unica.ejecutar_3D(Tabla)
        ver_tipo=self.mi_tipo_ope(self.operando,exec_op,Tabla)
        temp = Temporal(None,ver_tipo,correlativo=Tabla.nuevo_correlativo())
        self.operacion_unica.pop_retorno(Tabla, exec_op.temp_str())
        tmp_op = ""
        if self.operando != "+":
            tmp_op = self.operando

        mi_expresion=temp.temp_str()+"="+tmp_op+exec_op.temp_str()+";"
        Tabla.nuevo_codigo_3d(mi_expresion)
        if self.operando == "&":
            temp.ref=True
        self.mi_tempo=temp

        return temp

    def mi_tipo_ope(self,op,operando,Tabla):
        if op == "~" or op == "+" or op == "-" or op == "&" or op == "!":
            if operando.tipo == 0 or operando.tipo == 1 :
                return operando.tipo
            else:
                desc="No se Puede "+op+" con tipo: "+self.tipo_a_str(operando.tipo)
                Tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
                return 0;
        else:
            return str(op)
            #print("Tipo Desconocido :"+str(op))

        #print(izquierda.tipo)
        return 0


