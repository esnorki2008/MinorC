from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal


class Variaciones(Instruccion):
    operando = None
    nombre = None

    def __init__(self, nombre, operando, tupla):
        self.operando = operando
        self.nombre = nombre
        self.tupla = tupla

    def str_arbol(self):
        concatenar = ""
        expand = "VARIAR "+self.nombre+" "+self.operando
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        return concatenar

    def ejecutar_3D(self, Tabla):
        vari = Tabla.buscar_temporal(self.nombre,self.tupla,None)
        if vari is not None:
            if self.operando == "++":
                Tabla.nuevo_codigo_3d(vari.contenido+" = "+vari.contenido + " + 1;")
            else:
                Tabla.nuevo_codigo_3d(vari.contenido + " = " + vari.contenido + " - 1;")
        else:
            titu="Variable: '"+self.nombre+" Encontrada "
            desc="no se puede incrementar o decrementar si no esta definida la variable"
            Tabla.nuevo_error(titu,desc,0,self.tupla)
            vari= Temporal(0,0)


        return vari
        # return self.contenido


