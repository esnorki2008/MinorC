from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal


class NodoBinario(Instruccion):
    operador_izquierdo:Instruccion = None
    operador_derecho:Instruccion = None
    operando: str = ""

    def __init__(self, operador_izquierdo,operando,operador_derecho,tupla):
        self.operador_izquierdo = operador_izquierdo
        self.operador_derecho = operador_derecho
        self.operando = operando
        self.tupla=tupla

    def str_arbol(self):
        concatenar = ""
        expand =  str(self.operando)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.operador_izquierdo.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.operador_izquierdo)) + "\n"
        concatenar += self.operador_derecho.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.operador_derecho)) + "\n"
        return concatenar

    def ejecutar_3D(self,Tabla):
        exec_iz = self.operador_izquierdo.ejecutar_3D(Tabla)
        exec_de = self.operador_derecho.ejecutar_3D(Tabla)
        self.operador_izquierdo.pop_retorno(Tabla,exec_iz.temp_str())
        self.operador_derecho.pop_retorno(Tabla, exec_de.temp_str())
        ver_tipo=self.mi_tipo_ope(exec_iz,self.operando,exec_de,Tabla)
        temp = Temporal(None,ver_tipo,correlativo=Tabla.nuevo_correlativo())
        mi_expresion=temp.temp_str()+"="+exec_iz.temp_str()+self.operando+exec_de.temp_str()+";"
        Tabla.nuevo_codigo_3d(mi_expresion)
        self.mi_tempo=temp
        return temp





    def mi_tipo_ope(self,izquierda,operando,derecha,tabla):
        if operando == "+" :
            return self.tipo_mas(izquierda,derecha,operando,tabla)
        elif operando == "-" or operando == "*" or operando == "/" or operando == "%" :
            return self.tipo_menos_por_div_mod(izquierda,derecha,operando,tabla)
        elif operando == "<<" or operando == ">>":
            return self.tipo_nivel_binario(izquierda,derecha,operando,tabla)
        elif operando == "<" or operando == "<=" or operando == ">" or operando == ">=":
            return 0
        elif operando == "==" or operando == "!=":
            return 0
        elif operando == "&&" or operando == "||":
            return 0
        elif operando == "^" or operando == "&" or operando == "|":
            return self.tipo_nivel_binario(izquierda,derecha,operando,tabla)
        else:
            print("Tipo Desconocido :" + str(operando))
        return 0


    def tipo_nivel_binario(self,izquierda,derecha,op,tabla):
        if izquierda.tipo == 0:
            if derecha.tipo == 0:
                return 0
            else:
                desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo)+" "+ self.tipo_a_str(derecha.tipo)
                tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
                return 0
        else:
            desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo) + " " + self.tipo_a_str(
                derecha.tipo)
            tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
            return 0

    def tipo_menos_por_div_mod(self,izquierda,derecha,op,tabla):
        if izquierda.tipo == 0:
            if derecha.tipo == 0:
                return 0
            elif derecha.tipo == 1:
                return 1
            else:
                desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo)+" "+ self.tipo_a_str(derecha.tipo)
                tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
                return 0
        elif izquierda.tipo == 1:
            if derecha.tipo == 0:
                return 1
            elif derecha.tipo == 1:
                return 1
            else:
                desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo)+" "+ self.tipo_a_str(derecha.tipo)
                tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
                return 0
        else:

            desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo) + " " + self.tipo_a_str(derecha.tipo)
            tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
            return 0




    def tipo_mas(self,izquierda,derecha,op,tabla):
        if izquierda.tipo == 0:
            if derecha.tipo == 0:
                return 0
            elif derecha.tipo == 1:
                return 1
            else:
                desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo)+" "+ self.tipo_a_str(derecha.tipo)
                tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
                return 0
        elif izquierda.tipo == 1:
            if derecha.tipo == 0:
                return 1
            elif derecha.tipo == 1:
                return 1
            else:
                desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo)+" "+ self.tipo_a_str(derecha.tipo)
                tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
                return 0
        elif izquierda.tipo == 2:
            if derecha.tipo == 2:
                return 2
            else:
                desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo)+" "+ self.tipo_a_str(derecha.tipo)
                tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
                return 2
        else:
            desc = "No se Puede '" + op + "' con tipos: " + self.tipo_a_str(izquierda.tipo) + " " + self.tipo_a_str(
                derecha.tipo)
            tabla.nuevo_error("Error De Tipos", desc, 0, self.tupla)
            return 0