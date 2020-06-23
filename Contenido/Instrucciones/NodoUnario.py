from Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal


class NodoUnario(Instruccion):
    operacion_unica:Instruccion = None
    operando: str = ""

    def __init__(self,operando, operacion_unica,tupla):
        self.operacion_unica = operacion_unica
        self.operando = operando
        self.tupla=tupla

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
            print("Tipo Desconocido :"+str(op))

        #print(izquierda.tipo)
        return 0

    def str_arbol(self):
        pass
