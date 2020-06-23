from Contenido.Instrucciones.InstruccionAbstracta import Instruccion

class ListaInstruccion(Instruccion):
    contenido : [] = None

    def __init__(self, contenido : []):
        self.contenido = contenido

    def agregar(self,item):
        self.contenido.append(item)

    def ejecutar_3D(self,Tabla):
        for each in self.contenido:
            each.ejecutar_3D(Tabla)

        #return self.contenido

    def homogenizar_tipos(self,tipo_dado):
        for each in self.contenido:
            each.tipo=tipo_dado

    def str_arbol(self):
        pass
