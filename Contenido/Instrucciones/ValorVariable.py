from Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal


class ValorVariable(Instruccion):
    nombre = None


    def __init__(self, nombre,tupla):
        self.nombre = nombre
        self.tupla=tupla

    def ejecutar_3D(self, Tabla):
        vari = Tabla.buscar_temporal(self.nombre,self.tupla,None)
        if vari is None:
            return Temporal(0,0)
        else :
            return  vari

    def str_arbol(self):
        pass
