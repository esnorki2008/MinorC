from Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from Contenido.TablaDeSimbolos import TablaDeSimbolos

class FuncMetodo(Instruccion):
    param = None
    cuerpo = None
    nombre = None
    def __init__(self,nombre, param, cuerpo,tupla):
        self.cuerpo = cuerpo
        self.param = param
        self.nombre=nombre
        self.tupla = tupla

    def ejecutar_3D(self, Tabla):


        novo = TablaDeSimbolos(Tabla)
        nombre_metodo = str(self.nombre)
        novo.nuevo_codigo_3d(nombre_metodo + ":")
        if self.nombre == "main" :
            init="$s0=array();#pila"
            Tabla.nuevo_codigo_3d(init)
            init = "$s1=array();#retorno"
            Tabla.nuevo_codigo_3d(init)
            init="$sp=-1;#null ptr"
            Tabla.nuevo_codigo_3d(init)
            init="$ra=-1;#null ptr"
            Tabla.nuevo_codigo_3d(init)
            init = "$v=0;"
            Tabla.nuevo_codigo_3d(init)
        if len(self.param) > 0:
            self.simular_pop(novo)

        self.cuerpo.ejecutar_3D(novo);
        Tabla.nuevo_codigo_3d("goto retornos;")

    def str_arbol(self):
        pass

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
        return ""