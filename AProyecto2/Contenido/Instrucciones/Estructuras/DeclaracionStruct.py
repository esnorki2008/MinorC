from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class DeclaracionStruct(Instruccion):
    tipo = None
    nombre = None
    corche = []
    def __init__(self,tipo,nombre,tp,corche = []):
        self.nombre = nombre
        self.tipo = tipo
        self.tupla=tp
        self.corche = corche

    def str_arbol(self):
        concatenar = ""
        expand = "Declarar " + str(self.tipo) + " : " + str(self.nombre)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += str(id(self)) + "c[shape=rect,sides=4,skew=.4,label=\"" + "[]" + "\"]\n"
        concatenar += str(id(self)) + " -> " + str(id(self)) + "c" + "\n"
        for cada in self.corche:
            concatenar += cada.str_arbol()
            concatenar += str(id(self)) + "c" + " -> " + str(id(cada)) + "\n"
        return concatenar

    def ejecutar_3D(self, Tabla):
        temp = Temporal(None,self.tipo, correlativo=Tabla.nuevo_correlativo())
        lista_val = []
        for cor in self.corche:
            tem = cor.ejecutar_3D(Tabla);
            if tem.tipo != 0:
                desc = "Los indices de los arreglos solo pueden ser enteros"
                Tabla.nuevo_error("Eror De Tipos", desc, 0, self.tupla)
                return
            lista_val.append(tem)
        temp.lista_corchetes = lista_val


        mi_expresion = temp.temp_str() + " = " + "array();"
        Tabla.nuevo_codigo_3d(mi_expresion)
        Tabla.declarar_struct_busqueda(self.tipo,temp.temp_str(),self.tupla)
        Tabla.nuevo_temporal(self.nombre, temp,self.tupla)

        # return self.contenido


