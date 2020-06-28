from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class Cast(Instruccion):

    nombre = None
    expre = None

    def __init__(self,nombre,expre, tupla):
        self.tupla = tupla
        self.nombre=nombre
        self.expre=expre

    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        novo_tempo = Temporal(None, 0, Tabla.nuevo_correlativo())
        dot_exe = self.expre.ejecutar_3D(Tabla)
        sub_str:str=self.nombre
        if sub_str.find("double")!=-1:
            sub_str="(float)"
            novo_tempo.tipo=1
        elif sub_str.find("float")!=-1:
            novo_tempo.tipo=1
        elif sub_str.find("int")!=-1:
            novo_tempo.tipo=0
        elif sub_str.find("char")!=-1:
            novo_tempo.tipo=2
        Tabla.nuevo_codigo_3d(novo_tempo.contenido + "=" +sub_str+str(dot_exe.contenido)+";")
        return novo_tempo

    def str_arbol(self):
        concatenar = ""
        expand = self.nombre
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += str(id(self)) +" -> "+str(id(self.expre))+"\n"
        concatenar += self.expre.str_arbol()+"\n"
        return concatenar
