from Contenido.Instrucciones.InstruccionAbstracta import Instruccion

class ListaMetodos(Instruccion):
    contenido : [] = None

    def __init__(self, contenido : []):
        self.contenido = contenido

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

    def str_arbol(self):
        pass
