from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class Declaracion(Instruccion):
    valor = None
    nombre = None
    corche = None
    arr_val = []
    def __init__(self, nombre, valor, tipo, tupla,corche = [],arr_val = []):
        self.valor = valor
        self.nombre = nombre
        self.tipo = tipo
        self.tupla = tupla
        self.corche = corche
        self.arr_val = arr_val

    def str_arbol(self):
        concatenar = ""
        expand = "DECLARACION " + str(self.nombre)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        if self.valor is not None:
            concatenar += self.valor.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(self.valor)) + "\n"
        concatenar += "c"+str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "[]" + "\"]\n"
        concatenar += str(id(self)) + " -> " + "c"+str(id(self))  + "\n"
        for cada in self.corche:
            concatenar += cada.str_arbol()
            concatenar += "c"+str(id(self))   + " -> " + str(id(cada)) + "\n"
        return concatenar

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
        Tabla.nuevo_temporal(self.nombre[0], temp,self.tupla)
        self.ejecutar_arreglo_con_valor(Tabla,temp)

    def ejecutar_arreglo_con_valor(self,Tabla,tempo):
        if self.arr_val is None:
            return
        conta=0;
        for cor in self.arr_val:
            if type(cor) != list:
                tem_exec=cor.ejecutar_3D(Tabla);
                expresion=tempo.contenido+"["+str(conta)+"] = "+str(tem_exec.contenido)+";"
                Tabla.nuevo_codigo_3d(expresion)
                
            else:
                conta_sub=0;
                for sub_item in cor:
                    tem_exec=sub_item.ejecutar_3D(Tabla);
                    expresion=tempo.contenido+"["+str(conta)+"]"+"["+str(conta_sub)+"]"+" = "+str(tem_exec.contenido)+";"
                    Tabla.nuevo_codigo_3d(expresion)
                    conta_sub=conta_sub+1

            conta=conta+1

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

        if self.tipo != valor_exec.tipo and (self.union(self.tipo,valor_exec.tipo)==False):
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
            Tabla.nuevo_temporal(cada, temp , self.tupla)

        # return self.contenido


    def union(self,tipo1,tipo2):
        if tipo1 == 0:
            if tipo2==0:
                return True
            elif tipo2==1:
                return True
            else:
                return False
        elif tipo1==1:
            if tipo2==0:
                return True
            elif tipo2==1:
                return True
            else:
                return False
        return False

