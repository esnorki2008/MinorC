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

    @abstractmethod
    def ejecutar_3D(self,Tabla):
        pass


