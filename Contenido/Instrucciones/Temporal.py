class Temporal:
    contenido = None
    tipo = None
    correlativo = -1

    def __init__(self, contenido, tipo, correlativo=-1):
        self.tipo = tipo
        self.correlativo = correlativo

        if contenido is None:
            self.contenido=self.temp_str()
        else:
            self.contenido=contenido

    def temp_str(self):
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