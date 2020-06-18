from Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal


class NodoBinario(Instruccion):
    operador_izquierdo:Instruccion = None
    operador_derecho:Instruccion = None
    operando: str = ""

    def __init__(self, operador_izquierdo,operando,operador_derecho):
        self.operador_izquierdo = operador_izquierdo
        self.operador_derecho = operador_derecho
        self.operando = operando

    def ejecutar_3D(self,Tabla):
        exec_iz = self.operador_izquierdo.ejecutar_3D(Tabla)
        exec_de = self.operador_derecho.ejecutar_3D(Tabla)
        ver_tipo=self.mi_tipo_ope(exec_iz,exec_de)
        temp = Temporal(None,ver_tipo,correlativo=Tabla.nuevo_correlativo())
        mi_expresion=temp.temp_str()+"="+exec_iz.temp_str()+self.operando+exec_de.temp_str()+";"
        print(mi_expresion)

        return temp

    def mi_tipo_ope(self,izquierda,derecha):
        return 0

    def str_arbol(self):
        pass
