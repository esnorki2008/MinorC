class Error:
    titulo = None
    descripcion = None
    tipo = None
    tupla = (0, 0)

    def __init__(self, titulo, descripcion, tipo, tupla):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo
        self.tupla = tupla

        print(titulo+"  "+descripcion)


class TablaDeSimbolos:
    correlativo: int = 0
    codigo_3d = []
    tabla_padre = None
    lst_errores = None

    dic_temporales = {}

    def __init__(self, tabla_padre):
        self.codigo_3d=[]
        self.lst_errores = []
        self.dic_temporales = {}
        self.tabla_padre = tabla_padre
        if tabla_padre is None:
            self.correlativo = 0
        else:
            self.correlativo = self.tabla_padre.correlativo + 1

    def nuevo_correlativo(self):
        self.correlativo = self.correlativo + 1
        return self.correlativo

    def nuevo_codigo_3d(self, nuevo):
        tmp = self
        while tmp.tabla_padre is not None:
            tmp = tmp.tabla_padre
        tmp.codigo_3d.append(nuevo)

    def reemplazar_ultimo_codigo_3d(self,ultimo,correcto):
        tmp = self
        while tmp.tabla_padre is not None:
            tmp = tmp.tabla_padre

        if len(tmp.codigo_3d) == 0 :
            print("ERROR REEMPLAZANDO")
            return

        text:str=tmp.codigo_3d[-1]
        text=text.replace(ultimo,correcto)
        tmp.codigo_3d[-1]=text

    def imprimir_codigo_3d(self):
        for cada in self.codigo_3d:
            print(cada)

    def nuevo_temporal(self, llave, valor):
        self.dic_temporales[llave] = valor


    def imprimir_temporales(self):
        for cada in self.dic_temporales.items():
            print(str(cada[0]) + "      " + str(cada[1].contenido))

    def nuevo_error(self, titulo, descripcion, tipo, tupla):
        tmp = self
        while tmp.tabla_padre is not None:
            tmp = tmp.tabla_padre

        tmp.lst_errores.append(Error(titulo, descripcion, tipo, tupla))

    def buscar_temporal(self, nombre, tupla, default):
        bus = self.dic_temporales.get(nombre, None)
        if bus is None:
            tmp = self
            while tmp is not None:
                bus = tmp.dic_temporales.get(nombre, None)
                tmp = tmp.tabla_padre
                if bus is not None:
                    return bus
            desc = "La Variable " + str(nombre) + " no fue definida en este ambito"
            self.nuevo_error("Variable No Definida", desc, 0, tupla)
            return default

        else:
            return bus