from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal


class ValorVariable(Instruccion):
    nombre = None
    corche = []

    def __init__(self, nombre,tupla,corche = []):
        self.nombre = nombre
        self.tupla=tupla
        self.corche=corche

    def str_arbol(self):
        concatenar = ""
        expand = "Valor Variable " +  str(self.nombre)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += "c"+str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + "[]" + "\"]\n"
        concatenar += str(id(self)) + " -> " + "c"+str(id(self))  + "\n"
        for cada in self.corche:
            concatenar += cada.str_arbol()
            concatenar += "c"+str(id(self))  + " -> " + str(id(cada)) + "\n"
        return concatenar

    def ejecutar_arreglo(self,Tabla):


        concat = ""
        for cor in self.corche:
            tem=cor.ejecutar_3D(Tabla);
            if tem.tipo != 0:
                desc = "Los indices de los arreglos solo pueden ser enteros"
                Tabla.nuevo_error("Eror De Tipos", desc, 0, self.tupla)
                return Temporal(0, 0)

            concat =concat +"["+str(tem.contenido)+"]"


        vari = Tabla.buscar_temporal(self.nombre, self.tupla, None)
        if vari is None:
            self.tipo = 0
            return Temporal(0, 0)
        else:
            self.tipo = vari.tipo
            varre= Temporal(0,0)

            if vari.tipo == 3 or vari.tipo == 4 or vari.tipo == 5:
                varre.tipo = vari.tipo - 3
            else:
                varre.tipo = vari.tipo
            varre.contenido =vari.contenido+concat
            return varre


    def ejecutar_3D(self, Tabla):
        if len(self.corche) != 0:
            return  self.ejecutar_arreglo(Tabla)

        vari = Tabla.buscar_temporal(self.nombre,self.tupla,None)
        if vari is None:
            self.tipo=0
            return Temporal(0,0)
        else :
            self.tipo = vari.tipo
            return  vari


