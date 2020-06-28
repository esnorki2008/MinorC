from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class ValorStruct(Instruccion):
    contenido = None
    nombre = None
    corche = None
    def __init__(self,nombre,contenido,tp,corche = []):
        self.nombre = nombre
        self.contenido = contenido
        self.tupla=tp
        self.corche = corche

    def str_arbol(self):
        concatenar = ""
        expand = "Valor Struct " + str(self.tipo) + " : " + str(self.nombre)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += str(id(self)) + "c[shape=rect,sides=4,skew=.4,label=\"" + "[]" + "\"]\n"
        concatenar += str(id(self)) + " -> " + str(id(self)) + "c" + "\n"
        concatenar += str(id(self)) + " -> " + str(id(self.contenido))  + "\n"
        concatenar += self.contenido.str_arbol()
        for cada in self.corche:
            concatenar += cada.str_arbol()
            concatenar += str(id(self)) + "c" + " -> " + str(id(cada)) + "\n"
        return concatenar

    def ejecutar_3D(self, Tabla):
        concat = ""
        for cor in self.corche:
            tem = cor.ejecutar_3D(Tabla);
            if tem.tipo != 0:
                desc = "Los indices de los arreglos solo pueden ser enteros"
                Tabla.nuevo_error("Eror De Tipos", desc, 0, self.tupla)
                return Temporal(0, 0)
            concat = concat + "[" + str(tem.contenido) + "]"



        vari = Tabla.buscar_temporal(self.nombre, self.tupla, None)
        reto = Temporal(0, 0)
        if vari is not None:
            tipa=Tabla.struct_busqueda_atributo_tipo(vari.tipo, self.contenido, self.tupla)
            reto.tipo=tipa
            reto.contenido=str(vari.contenido)+concat+"[\""+str(self.contenido)+"\"]"

        return reto



