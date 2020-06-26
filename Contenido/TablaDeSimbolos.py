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
    dic_struct = {}
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
        self.dic_struct = {}
        if tabla_padre is None:
            self.correlativo = 0
        else:
            self.correlativo = self.tabla_padre.correlativo + 1

    def nuevo_struct(self,llave,struct):
        self.dic_struct[llave] = struct

    def declarar_struct_busqueda(self,nombre,tempo_var,tupla):
        temp = self
        while temp.tabla_padre is not None:
            temp = temp.tabla_padre

        for cada in temp.dic_struct.items():
            if cada[0]==nombre:
                cada[1].colocar_inicializacion(temp,tempo_var)
                return

        self.nuevo_error("struct '"+nombre+ "' no definido", "se intento usar un struct no definido", 0, tupla)

    def struct_busqueda_atributo(self,nombre,tempo_var,tupla):
        temp = self
        while temp.tabla_padre is not None:
            temp = temp.tabla_padre


        for cada in temp.dic_struct.items():
            if cada[0]==nombre:
                verdad=cada[1].struct_busqueda_atributo(temp,tempo_var)
                if verdad == True:
                    return True
                else:
                    descrip ="el struct '" + nombre + "' no tiene el atributo: " + tempo_var
                    self.nuevo_error("struct '" + nombre + "' no tiene atributo",descrip, 0, tupla)

        self.nuevo_error("struct '" + nombre + "' no definido", "se intento usar un struct no definido", 0, tupla)
        return False

    def struct_busqueda_atributo_tipo(self, nombre, tempo_var, tupla):
            temp = self
            while temp.tabla_padre is not None:
                temp = temp.tabla_padre

            for cada in temp.dic_struct.items():
                if cada[0] == nombre:
                    verdad = cada[1].struct_busqueda_atributo_tipo(temp, tempo_var)
                    if verdad is not None:
                        return verdad
                    else:
                        descrip = "el struct '" + nombre + "' no tiene el atributo: " + tempo_var
                        self.nuevo_error("struct '" + nombre + "' no tiene atributo", descrip, 0, tupla)

            self.nuevo_error("struct '" + nombre + "' no definido", "se intento usar un struct no definido", 0, tupla)
            return None

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

    def caso_continue(self):
        tmp = self
        while tmp.tabla_padre is not None:
            tmp = tmp.tabla_padre
        return tmp.codigo_3d.pop(-1)

    def reemplazar_ultimo_codigo_3d(self,ultimo,correcto):
        #return None

        tmp = self
        while tmp.tabla_padre is not None:
            tmp = tmp.tabla_padre

        if len(tmp.codigo_3d) == 0 :
            print("ERROR REEMPLAZANDO")
            return None
        cd_3d:str = tmp.codigo_3d[-1]
        spl = cd_3d.split("=")
        if spl[0]==ultimo:
            import re
            es_sub=spl[0].find(ultimo)
            es_llamado = spl[1].find(ultimo)
            if es_sub!=-1 and es_llamado == -1:
                last = correcto+"="+spl[1]

                #print(spl[1]+'   '+ultimo+'   '+correcto+'    '+spl[0])
                tmp.codigo_3d[-1]=last
                return True
        return None

    def terminar_codigo_3d(self):
        self.mi_tabla_de_retornos()

    def imprimir_codigo_3d(self,lista_3d):
        for cada in lista_3d:
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