from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion


class ListaInstruccion(Instruccion):
    contenido: [] = None
    nombre = ""
    def __init__(self, contenido: []):
        self.contenido = contenido

    def str_arbol(self):
        concatenar = ""
        expand = "Lista Instrucciones"
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        for cada in self.contenido:
            concatenar += cada.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(cada)) + "\n"
        return concatenar

    def agregar(self, item):
        self.contenido.append(item)

    def ejecutar_3D(self, Tabla):
        for each in self.contenido:
            each.paso_continue = self.paso_continue
            each.paso_break = self.paso_break
            detener =each.ejecutar_3D(Tabla)
            if detener =="stopu" or detener =="stopc":
                return  detener

        # return self.contenido

    def homogenizar_tipos(self, tipo_dado):
        for each in self.contenido:
            each.tipo = tipo_dado
