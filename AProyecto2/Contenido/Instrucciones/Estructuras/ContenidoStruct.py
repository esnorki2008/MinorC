from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class ContenidoStruct(Instruccion):
    tipo = None
    lst_nombres = None

    def __init__(self, tipo, lst_nombres,tupla):
        self.tipo= tipo
        self.lst_nombres = lst_nombres
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "Declaraciones Struct"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        for cada in self.lst_nombres:
            concatenar += str(id(cada)) + "[shape=rect,sides=4,skew=.4,label=\"" + cada + "\"]\n"
            concatenar += str(id(self))  + " -> " + str(id(cada)) + "\n"
        return concatenar

    def colocar_inicializacion(self,tabla,temporal):
        for cada in self.lst_nombres:
            inst = temporal + "[\"" + cada + "\"]" + " = " + self.val_defecto(self.tipo) + ";"
            tabla.nuevo_codigo_3d(inst)

    def struct_busqueda_atributo(self,tabla,atributo):
        for cada in self.lst_nombres:
            if cada == atributo:
                return True

    def struct_busqueda_atributo_tipo(self,tabla,atributo):
        for cada in self.lst_nombres:
            if cada == atributo:
                return self.tipo

    def ejecutar_3D(self, Tabla):
        pass

    def val_defecto(self,tipo):
        if tipo == 0: return "0"
        elif tipo == 1: return "0.0"
        elif tipo == 2:return " "


