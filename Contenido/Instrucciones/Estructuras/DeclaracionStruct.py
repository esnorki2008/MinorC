from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class DeclaracionStruct(Instruccion):
    tipo = None
    nombre = None

    def __init__(self,tipo,nombre,tp):
        self.nombre = nombre
        self.tipo = tipo
        self.tupla=tp

    def ejecutar_3D(self, Tabla):
        temp = Temporal(None,self.tipo, correlativo=Tabla.nuevo_correlativo())
        mi_expresion = temp.temp_str() + " = " + "array();"
        Tabla.nuevo_codigo_3d(mi_expresion)
        Tabla.declarar_struct_busqueda(self.tipo,temp.temp_str(),self.tupla)
        Tabla.nuevo_temporal(self.nombre, temp)

        # return self.contenido

    def str_arbol(self):
        pass
