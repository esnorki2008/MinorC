from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion,Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

class Ternario(Instruccion):
    condicion = None
    val_true = None
    val_false = None

    def __init__(self,condicion,val_true,val_false, tupla):
        self.tupla = tupla
        self.condicion = condicion
        self.val_false = val_false
        self.val_true = val_true

    def ejecutar_3D(self, Tabla:TablaDeSimbolos):
        novo_tempo = Temporal(None, 0, Tabla.nuevo_correlativo())
        rst_condi = self.condicion.ejecutar_3D(Tabla)
        mi_nombre = "label"+str(id(self))
        condicion = "if(!"+str(rst_condi.contenido)+") goto "+mi_nombre+";"
        if rst_condi.tipo != 0:
            Tabla.nuevo_error("error de tipo","la condicion debe ser de tipo entero",0,self.tupla)
        Tabla.nuevo_codigo_3d(condicion)
        tempo_si = self.val_true.ejecutar_3D(Tabla)
        condicion = novo_tempo.contenido+"=" + str(tempo_si.contenido) + ";"
        Tabla.nuevo_codigo_3d(condicion)
        condicion = "goto out"+mi_nombre+";"
        Tabla.nuevo_codigo_3d(condicion)
        condicion = mi_nombre + ":"
        Tabla.nuevo_codigo_3d(condicion)
        tempo_no = self.val_false.ejecutar_3D(Tabla)
        condicion = novo_tempo.contenido + "=" + str(tempo_no.contenido) + ";"
        Tabla.nuevo_codigo_3d(condicion)
        condicion = "out"+mi_nombre + ":"
        Tabla.nuevo_codigo_3d(condicion)

        return novo_tempo

    def str_arbol(self):
        concatenar = ""
        expand = "Ternario"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        concatenar += str(id(self)) + " -> " + str(id(self.condicion))+"\n"
        concatenar += str(id(self)) + " -> " + str(id(self.val_true)) + "\n"
        concatenar += str(id(self)) + " -> " + str(id(self.val_false)) + "\n"
        concatenar += self.condicion.str_arbol() + "\n"
        concatenar += self.val_true.str_arbol() + "\n"
        concatenar += self.val_false.str_arbol() + "\n"
        return concatenar
