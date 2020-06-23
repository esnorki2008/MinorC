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

        print(titulo+"  "+descripcion+" "+str(tupla))


class TablaDeSimbolos:
    correlativo: int = 0
    codigo_3d = []
    tabla_padre = None
    lst_errores = None
    parametros = 0
    dic_temporales = {}
    return_address = 0
    contador_retornos=0

    def __init__(self, tabla_padre):
        self.contador_retornos = 0
        self.parametros = 0
        self.codigo_3d=[]
        self.lst_errores = []
        self.dic_temporales = {}
        self.tabla_padre = tabla_padre
        self.return_address=0
        if tabla_padre is None:
            self.correlativo = 0
        else:
            self.correlativo = self.tabla_padre.correlativo + 1

    def nuevo_retorno(self):
        self.contador_retornos = self.contador_retornos +1 ;
        return  self.contador_retornos

    def push_mi_alcance(self):
        tmp = self
        while tmp is not None:
            for cada in tmp.dic_temporales.items():
                self.nuevo_codigo_3d("$sp1 = $sp1 + 1;")
                self.nuevo_codigo_3d("$s3[$sp1] = "+cada[1].contenido+";#push alcance")
            tmp = tmp.tabla_padre

    def pop_mi_alcance(self):
        tmp = self
        volcado = []
        while tmp is not None:
            for cada in  tmp.dic_temporales.items():
                vol_item=("$sp1 = $sp1 - 1;",cada[1].contenido+" = $s3[$sp1]"+";#pop alcance")
                volcado.append(vol_item)

            tmp = tmp.tabla_padre

        for cada in reversed(volcado):

            self.nuevo_codigo_3d(cada[1])
            self.nuevo_codigo_3d("unset($s3[$sp1]);")
            self.nuevo_codigo_3d(cada[0])


    def aumentar_retorno(self):
        tmp = self
        while tmp.tabla_padre is not None:
            tmp = tmp.tabla_padre
        tmp.return_address= tmp.return_address+1
        return  tmp.return_address

    def mi_tabla_de_retornos(self):
        self.nuevo_codigo_3d("retornos:")
        self.nuevo_codigo_3d("if ($sp1 > 1000) goto stacko;")
        self.nuevo_codigo_3d("if ($sp  > 1000) goto stacko;")
        self.nuevo_codigo_3d("if ($ra  < 0) exit;")
        for i in range(1,self.return_address+1):
            self.nuevo_codigo_3d("if ($s1[$ra] == "+str(i)+ ") goto ra"+str(i)+" ;")
        self.nuevo_codigo_3d("stacko:")
        self.nuevo_codigo_3d("print(\"Desbordamiento de pila\");")
        self.nuevo_codigo_3d("exit;")

    def nuevo_correlativo(self):
        self.correlativo = self.correlativo + 1
        return self.correlativo

    def nuevo_parametro(self):
        self.parametros = self.parametros + 1
        return self.parametros

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
        self.mi_tabla_de_retornos()
        for cada in self.codigo_3d:
            print(cada)

    def ultimo_redundante(self,nuevo):
        if self.codigo_3d[-1] != nuevo :
            self.nuevo_codigo_3d(nuevo)

    def nuevo_temporal(self, llave, valor):
        self.dic_temporales[llave] = valor


    def imprimir_temporales(self):
        for cada in self.dic_temporales.items():
            print(str(cada[0]) + "      " + str(cada[1].contenido))

    def nuevo_error(self, titulo, descripcion, tipo, tupla):
        tmp = self
        while tmp.tabla_padre is not None:
            tmp = tmp.tabla_padre
        print(titulo)
        print(descripcion)
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