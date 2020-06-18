from abc import ABC, abstractmethod
from Contenido.Instrucciones.Temporal import Temporal

class Instruccion(ABC):
    tupla: () = (0, 0)

    def n_t(self, tupla: ()):
        self.tupla = tupla

    def __init__(self, *args):
        pass

    @abstractmethod
    def str_arbol(self):
        pass

    @abstractmethod
    def ejecutar_3D(self,Tabla):
        pass


