class TablaDeSimbolos:
    correlativo: int = 0

    def __init__(self):
        self.correlativo = 0

    def nuevo_correlativo(self):
        self.correlativo = self.correlativo + 1
        return self.correlativo
