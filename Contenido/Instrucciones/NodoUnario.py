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
        ver_tipo=self.mi_tipo_ope(exec_op,self.operando)
        temp = Temporal(None,ver_tipo,correlativo=Tabla.nuevo_correlativo())
        mi_expresion=temp.temp_str()+"="+self.operando+exec_op.temp_str()+";"
        Tabla.nuevo_codigo_3d(mi_expresion)
        self.mi_tempo=temp
        return temp

    def mi_tipo_ope(self,op,operando):
        #print(izquierda.tipo)
        return 0

    def str_arbol(self):
        pass
