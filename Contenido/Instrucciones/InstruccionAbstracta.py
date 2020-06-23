from abc import ABC, abstractmethod
from Contenido.Instrucciones.Temporal import Temporal

class Instruccion(ABC):
    tupla: () = (0, 0)
    mi_tempo= None
    tipo = None
    def n_t(self, tupla: ()):
        self.tupla = tupla

    def __init__(self, *args):
        self.mi_tempo=None
        self.tipo=None

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
        else:
            return tipo
