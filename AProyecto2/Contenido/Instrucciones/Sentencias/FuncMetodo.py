from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncMetodo(Instruccion):
    param = None
    cuerpo = None
    nombre = None
    def __init__(self,nombre, param, cuerpo,tupla):
        self.cuerpo = cuerpo
        self.param = param
        self.nombre=nombre
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "Declaracion Metodo-Funcion "+self.nombre
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += self.cuerpo.str_arbol()
        concatenar += str(id(self)) + " -> " + str(id(self.cuerpo)) + "\n"
        for cada in self.param:
            concatenar += str(id(cada)) + "[shape=rect,sides=4,skew=.4,label=\"" + str(cada[1]) + "\"]\n"
            concatenar += str(id(self)) + " -> " + str(id(cada)) + "\n"
        return concatenar

    def ejecutar_3D(self, Tabla):


        novo = TablaDeSimbolos(Tabla)
        nombre_metodo = str(self.nombre)
        if self.nombre != "main":
            novo.nuevo_codigo_3d(nombre_metodo + ":")


        if len(self.param) > 0:
            self.simular_pop(novo)

        self.cuerpo.ejecutar_3D(novo);
        Tabla.ultimo_redundante("goto retornos;")



    def simular_pop(self,novo):
        for cada in reversed(self.param):

           temp = Temporal(None,self.dar_tipo(cada[0]),novo.nuevo_correlativo())
           mi_expresion = temp.temp_str() + "= $s0[$sp];#pop "
           novo.nuevo_codigo_3d(mi_expresion)
           mi_expresion = "$sp= $sp-1;"
           novo.nuevo_codigo_3d(mi_expresion)
           novo.nuevo_temporal(cada[1], temp)

        #novo.nuevo_codigo_3d(nombre_metodo + ":")

    def dar_tipo(self,tipo_supuesto):
        return tipo_supuesto