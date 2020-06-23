from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class ValorStruct(Instruccion):
    contenido = None
    nombre = None
    def __init__(self,nombre,contenido,tp):
        self.nombre = nombre
        self.contenido = contenido
        self.tupla=tp

    def ejecutar_3D(self, Tabla):
        vari = Tabla.buscar_temporal(self.nombre, self.tupla, None)
        if vari is not None:
            tipa=Tabla.struct_busqueda_atributo_tipo(vari.tipo, self.contenido, self.tupla)
            if  tipa is None:
                tipa=0
        reto= Temporal(None,0,0)
        reto.tipo=tipa
        reto.contenido=vari.contenido+"[\""+self.contenido+"\"]"
        return reto


    def str_arbol(self):
        pass
