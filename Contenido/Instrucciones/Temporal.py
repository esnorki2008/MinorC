class Temporal:
    contenido=None
    tipo=None
    correlativo = -1
    def __init__(self,contenido,tipo,correlativo=-1):
        self.contenido=contenido
        self.tipo=tipo
        self.correlativo=correlativo

    def temp_str(self):
        if self.correlativo != -1 :
            return "$t"+str(self.correlativo)
        else:
            return str(self.contenido)