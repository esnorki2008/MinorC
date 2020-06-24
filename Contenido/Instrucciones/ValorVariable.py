from Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal


class ValorVariable(Instruccion):
    nombre = None
    corche = []

    def __init__(self, nombre,tupla,corche = []):
        self.nombre = nombre
        self.tupla=tupla
        self.corche=corche

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

    def str_arbol(self):
        pass
