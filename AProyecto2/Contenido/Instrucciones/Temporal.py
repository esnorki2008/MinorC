class Temporal:
    contenido = None
    tipo = None
    correlativo = -1
    ref = False
    es_parametro=False
    lista_corchetes = []
    def __init__(self, contenido, tipo, correlativo=-1,es_parametro = False):
        self.ref = True
        self.tipo = tipo
        self.correlativo = correlativo
        self.es_parametro = es_parametro
        self.lista_corchetes = []

        if contenido is None:
            if es_parametro:
                self.contenido=self.param_str()
            else:
                self.contenido=self.temp_str()
        else:
            self.contenido=contenido

    def temp_str(self):
        if self.contenido is not None:
            return str(self.contenido)

        if self.es_parametro :
            return  self.param_str()

        if self.correlativo != -1:
            if str(self.correlativo)[0] == "v":
                return "$"+self.correlativo
            return "$t" + str(self.correlativo)
        else:
            return str(self.contenido)

    def param_str(self):
        if self.correlativo != -1:
            if str(self.correlativo)[0] == "v":
                return "$"+self.correlativo
            return "$a" + str(self.correlativo)
        else:
            return str(self.contenido)