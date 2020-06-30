from abc import ABC, abstractmethod
from AProyecto2.Contenido.Instrucciones.Temporal import Temporal

class Instruccion(ABC):
    tupla: () = (0, 0)
    mi_tempo= None
    tipo = None
    nombre_padre = None
    paso_break = None
    paso_continue = None
    def n_t(self, tupla: ()):
        self.tupla = tupla

    def __init__(self, *args):
        self.mi_tempo=None
        self.tipo=None
        self.nombre_padre = None
        self.paso_break = None
        self.paso_continue = None

    @abstractmethod
    def str_arbol(self):
        pass

    def pop_retorno(self, Tabla,et):
        pass

    def guardar_struct(self, Tabla):
        pass

    @abstractmethod
    def ejecutar_3D(self,Tabla):
        pass

    def tipo_a_str(self,tipo):
        if tipo == 0:
            return  "entero"
        elif tipo == 1:
            return  "decimal"
        elif tipo == 2:
            return  "cadena"
        elif tipo == 3:
            return  "arreglo entero"
        elif tipo == 4:
            return  "arreglo decimal"
        elif tipo == 5:
            return  "arreglo cadena"
        else:
            return tipo
