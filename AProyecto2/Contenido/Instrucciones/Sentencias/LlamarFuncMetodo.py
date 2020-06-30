from AProyecto2.Contenido.Instrucciones.InstruccionAbstracta import Instruccion, Temporal
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos


class LlamarFuncMetodo(Instruccion):
    lst_param: [] = None
    nombre_func: str = None

    def __init__(self, nombre_func, lista_parametros, tupla):
        self.lst_param = lista_parametros
        self.tupla = tupla
        self.nombre_func = nombre_func

    def str_arbol(self):
        concatenar = ""
        expand = "LLAMADO DE FUNCION :  "+self.nombre_func
        concatenar += str(id(self)) + "[shape=rect,sides=4,skew=.4,label=\"" + expand + "\"]\n"
        for cada in self.lst_param:
            concatenar += cada.str_arbol()
            concatenar += str(id(self)) + " -> " + str(id(cada)) + "\n"
        return concatenar

    def ejecutar_3D(self, Tabla):
        novo = TablaDeSimbolos(Tabla)
        lista_temp = []
        for each in self.lst_param:
            tempo: Temporal = each.ejecutar_3D(novo)

            each.pop_retorno(Tabla, tempo.contenido)

            param = Temporal(None, tempo.tipo, novo.nuevo_parametro())
            inst = param.param_str() + " = " + tempo.temp_str() + ";";
            lista_temp.append(inst)
            lista_temp.append("$sp = $sp + 1;")
            lista_temp.append("$s0[$sp] = " + param.param_str() + ";")
            # novo.nuevo_codigo_3d(inst)
            # novo.nuevo_codigo_3d("$sp = $sp + 1;")
            # novo.nuevo_codigo_3d("$s0[$sp] = "+param.param_str()+";")

        # for cada in Tabla.dic_temporales.items():
        # novo.nuevo_codigo_3d("$sp = $sp + 1;")
        # novo.nuevo_codigo_3d("$s0[$sp] = " + str(cada[1].contenido) + ";#push param")
        # novo.nuevo_codigo_3d("$s0[$sp] = $t2;#push param")
        novo.push_mi_alcance()

        for cada in lista_temp:
            novo.nuevo_codigo_3d(cada)

        novo.nuevo_codigo_3d("$ra = $ra + 1;")
        ra = novo.aumentar_retorno()
        novo.nuevo_codigo_3d("$s1[$ra] = " + str(ra) + " ;")

        novo.nuevo_codigo_3d("goto " + self.nombre_func + ";")
        novo.nuevo_codigo_3d("ra" + str(ra) + ":")
        novo.nuevo_codigo_3d("$ra = $ra - 1;")

        # for cada in Tabla.dic_temporales.items():
        # novo.nuevo_codigo_3d(str(cada[1].contenido) +" = $s0[$sp];#pop param")
        # novo.nuevo_codigo_3d("$t2 = $s0[$sp];#pop param")
        # novo.nuevo_codigo_3d("$sp = $sp - 1;")
        novo.pop_mi_alcance()

        corre = Tabla.nuevo_parametro()

        print("Implementar Tipo Del Retorno")

        Te = Temporal(None, 0, "v" + str(corre + 2))
        # Tabla.nuevo_temporal("$v"+str(corre+2),Te)
        return Te

    def pop_retorno(self, Tabla, reto):
        Tabla.nuevo_codigo_3d(reto + " = $s2[$v1000];#Valor En Pila Retorno")
        Tabla.nuevo_codigo_3d("unset($s2[$v1000]);")
        Tabla.nuevo_codigo_3d("$v1000 = $v1000 - 1;")
