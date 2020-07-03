from AProyecto2.Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from AProyecto2.Contenido.TablaDeSimbolos import TablaDeSimbolos

#cadena="int x=0; int a=0; do { a=a+x; x=x+1;  } while(x<4)"









cadena1 = '''
        

       

'''


cadena2='''

'''

cadena3='''



'''

cadena4 = '''
struct punto {
    int x,h;
    int y;
}
int main()
{   
    struct punto hola;
    hola.x=50;
}
'''

class Proyecto2:
    lst_repo_grama = []
    lst_errores = []
    lst_historial_variables = []
    raiz_arbol = None
    lst_reglas_usadas = []
    lst_metodos_declarados = []
    def __init__(self):
        self.lst_repo_grama = []
        self.reporte_gramatical_contenido=""
        self.lst_errores=[]
        self.taba = None
        self.lst_historial_variables = []
        self.lst_reglas_usadas = []
        self.lst_metodos_declarados = []

    def reporte_metodos_declarados(self):
        from AProyecto2.Contenido.TablaDeSimbolos import Error
        concaten="<table border='1' cellborder='1' color='blacks' cellspacing='0'>"
        concaten += "<tr> \n <td>Nombre Metodo</td> \n <td>Columna</td> \n"
        concaten +=" <td>Fila</td></tr>"
        conta = 1
        for cada in self.lst_metodos_declarados:
            erri:Error = cada
        
           
            concaten +="<tr>\n"
            concaten +="<td>"+str(cada[0])+"</td>\n"
            concaten +="<td>"+str(cada[1])+"</td>\n"
            concaten +="<td>"+str(cada[2])+"</td>\n"
            concaten +="</tr>\n"

            conta = conta +1
        concaten+="</table> "#\n >]; \n}"
        self.lst_metodos_declarados = []
        return concaten

    def reporte_reglas_utilizadas(self):
        from AProyecto2.Contenido.TablaDeSimbolos import Error
        concaten="<table border='1' cellborder='1' color='blacks' cellspacing='0'>"
        concaten += "<tr> \n <td>Numero De Regla</td> \n <td>Linea</td> \n"
        concaten +=" <td>Contenido Linea</td></tr>"
        conta = 1
        for cada in self.lst_reglas_usadas:
            erri:Error = cada
        
           
            concaten +="<tr>\n"
            concaten +="<td>"+str(cada[0])+"</td>\n"
            concaten +="<td>"+str(cada[1])+"</td>\n"
            concaten +="<td>"+str(cada[2])+"</td>\n"
            concaten +="</tr>\n"

            conta = conta +1
        concaten+="</table> "#\n >]; \n}"
        self.lst_reglas_usadas = []
        return concaten
    
    def reporte_tabla_variables(self):
        from AProyecto2.Contenido.TablaDeSimbolos import Error
        concaten="<table border='1' cellborder='1' color='blacks' cellspacing='0'>"
        concaten += "<tr> \n <td>Identificador</td> \n <td>Tipo</td> \n"
        concaten +=" <td>Valor</td>  \n <td>Columna</td>\n <td>Linea</td> \n</tr>"
        conta = 1
        for cada in self.lst_historial_variables:
            erri:Error = cada
            tis = "entero"
            if cada[1] == 0:tis="entero"
            elif cada[1] == 1:tis="decimal"
            elif cada[1] == 2:tis="cadena"
            elif cada[1] == 3:tis="arreglo entero"
            elif cada[1] == 4:tis="arreglo decimal"
            elif cada[1] == 5:tis="arreglo char"
            else:tis=str(cada[1])
            concaten +="<tr>\n"
            concaten +="<td>"+str(cada[0])+"</td>\n"
            concaten +="<td>"+str(tis)+"</td>\n"
            concaten +="<td>"+str(cada[2])+"</td>\n"
            concaten +="<td>"+str(cada[3])+"</td>\n"
            concaten +="<td>"+str(cada[4])+"</td>\n"
            
            concaten +="</tr>\n"
            conta = conta +1
        concaten+="</table> "#\n >]; \n}"
        self.lst_historial_variables = []
        return concaten

    def reporte_errores(self):
        from AProyecto2.Contenido.TablaDeSimbolos import Error
        concaten="<table border='1' cellborder='1' color='blacks' cellspacing='0'>"
        concaten += "<tr> \n <td>Indice</td> \n <td>Titulo</td> \n"
        concaten +=" <td>Descripcion</td> \n <td>Tipo</td> \n <td>Columna</td>\n <td>Linea</td> \n</tr>"
        conta = 1
        for cada in self.lst_errores:
            erri:Error = cada
            concaten +="<tr>\n"
            concaten +="<td>"+str(conta)+"</td>\n"
            concaten +="<td>"+str(erri.titulo)+"</td>\n"
            concaten +="<td>"+str(erri.descripcion)+"</td>\n"
            tis = "semantico"
            if erri.tipo == 1:tis="sintactico"
            elif erri.tipo == 2:tis="lexico"
            concaten +="<td>"+str(tis)+"</td>\n"
            concaten +="<td>"+str(erri.tupla[0])+"</td>\n"
            concaten +="<td>"+str(erri.tupla[1])+"</td>\n"
            concaten +="</tr>\n"
            conta = conta +1
        concaten+="</table> "#\n >]; \n}"
        return concaten

    def reporte_gramatical(self):
        #print(len(self.lst_repo_grama))
        self.reporte_gramatical_contenido=""
        for cada in self.lst_repo_grama:
            self.rp_nuevo_nodo(cada[0],cada[1])

        #print(self.reporte_gramatical_contenido)
        
        return self.rp_cabecera()
    
    def rp_nuevo_nodo(self, produ,regla):
        novo_nodo="<tr>\n <td>" +produ+"</td> \n"
        novo_nodo+="<td>"+regla+"</td> \n </tr>\n"
        self.reporte_gramatical_contenido = novo_nodo + self.reporte_gramatical_contenido

    def rp_cabecera(self):
        cabe =""
        #cabe +="digraph { \n tbl [ \n shape=plaintext \n label=<"
        cabe +="<table border='1' cellborder='1' color='blacks' cellspacing='0'>"
        cabe += "<tr> \n <td>Producción</td> \n <td>Regla Semantica</td> \n </tr>"
        cabe+=self.reporte_gramatical_contenido
        cabe+="</table> "#\n >]; \n}"
        return cabe
    
    def graphviz_arbol(self):
        if self.raiz_arbol is None:
            return "digraph { }"

        return self.raiz_arbol.str_arbol()

    def analizar_minor_c_optimizar_3D(self,cadena_entrada):     
        tab = TablaDeSimbolos(None)
        
        self.lst_repo_grama = []
        self.raiz_arbol = None
        self.lst_historial_variables = []
        rst=analizar_ascendente(cadena_entrada,self.lst_repo_grama,tab)
        if rst is None :
            self.lst_errores = tab.lst_errores
            print("Error")
        else:
            
            self.raiz_arbol = rst
            from AProyecto2.Contenido.Instrucciones.Listas.ListaMetodos import ListaMetodos
            self.lst_metodos_declarados = []
            if isinstance(rst,ListaMetodos):
                rst.reporte_metodos(self.lst_metodos_declarados)
            #print(rst.str_arbol());
            rst.ejecutar_3D(tab)
            self.lst_historial_variables = tab.lst_historial_variables
            tab.lst_historial_variables = []
            tab.terminar_codigo_3d()
            self.lst_errores = tab.lst_errores
            from AProyecto2.Contenido.Optimo import Optimo
            Optm:Optimo = Optimo(tab.codigo_3d,self.lst_reglas_usadas)
            lst_sal = Optm.codigo_optimizado()

            #print("NORMAL")
            #tab.imprimir_temporales()
            return tab.string_codigo_3d(lst_sal)

    def analizar_minor_c(self,cadena_entrada):
        tab = TablaDeSimbolos(None)
        self.lst_repo_grama = []
        self.raiz_arbol = None
        self.lst_historial_variables = []
        rst = analizar_ascendente(cadena_entrada,self.lst_repo_grama,tab)
        if rst is None :
            self.lst_errores = tab.lst_errores
            print("Error")
        else:
            
            self.raiz_arbol = rst
            from AProyecto2.Contenido.Instrucciones.Listas.ListaMetodos import ListaMetodos
            self.lst_metodos_declarados = []
            if isinstance(rst,ListaMetodos):
                rst.reporte_metodos(self.lst_metodos_declarados)
            #print(rst.str_arbol());
            rst.ejecutar_3D(tab)
            self.lst_historial_variables = tab.lst_historial_variables
            tab.lst_historial_variables = []
            tab.terminar_codigo_3d()
            self.lst_errores = tab.lst_errores
            #from Contenido.Optimo import Optimo
            #Optm:Optimo = Optimo(tab.codigo_3d)
            #lst_sal = Optm.codigo_optimizado()
            return tab.string_codigo_3d(tab.codigo_3d)


        #print(tab.codigo_3d)
        #tab.imprimir_temporales()


