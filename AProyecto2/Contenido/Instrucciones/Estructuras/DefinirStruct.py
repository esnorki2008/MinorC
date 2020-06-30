from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class DefinirStruct(Instruccion):
    nombre = None
    lst_contenido = None

    def __init__(self, nombre, lst_contenido, tupla):
        self.nombre = nombre
        self.lst_contenido = lst_contenido
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "Struct " + str(self.nombre)
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        for cada in self.lst_contenido:
            concatenar += cada.str_arbol()
            concatenar += str(id(self))  + " -> " + str(id(cada)) + "\n"
        return concatenar

    def guardar_struct(self, Tabla):
        Tabla.nuevo_struct(self.nombre,self)

    def colocar_inicializacion(self,tabla,temporal):
        for cada in self.lst_contenido:
            cada.colocar_inicializacion(tabla,temporal)

    def struct_busqueda_atributo(self,tabla,atributo):
        for cada in self.lst_contenido:
            verdad=cada.struct_busqueda_atributo(tabla, atributo)
            if verdad:
                return True
        else:
            return False

    def struct_busqueda_atributo_tipo(self,tabla,atributo):
        for cada in self.lst_contenido:
            verdad=cada.struct_busqueda_atributo_tipo(tabla, atributo)
            if verdad is not None:
                return verdad


        return None

    def ejecutar_3D(self, Tabla):
        pass

