from Contenido.Instrucciones.InstruccionAbstracta import Instruccion

class ListaMetodos(Instruccion):
    contenido : [] = None

    def __init__(self, contenido : []):
        self.contenido = contenido

    def str_arbol(self):
        concatenar = "digraph G { \n"
        expand = "Listado General"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        for con in self.contenido:
            concatenar += str(id(self)) + " -> " + str(id(con))  + "\n"
            concatenar += con.str_arbol()
        concatenar += "\n }"
        return concatenar

    def agregar(self,item):
        self.contenido.append(item)

    def ejecutar_3D(self,Tabla):
        if len(self.contenido ) == 0:
            return

        for each in self.contenido:
            each.guardar_struct(Tabla)
        main = self.contenido[-1]
        if main.nombre != "main":
            tp=(0,0)
            Tabla.nuevo_error("Error con Main","El Main No Es La Ultima Declaracion",0,tp)
            for each in self.contenido:
                if each.nombre == "main":
                    main = each
                    break
        main.ejecutar_3D(Tabla)
        for each in self.contenido:
            if each.nombre != "main":
                each.ejecutar_3D(Tabla)

        #return self.contenido


