from Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from Contenido.TablaDeSimbolos import TablaDeSimbolos

#cadena="int x=0; int a=0; do { a=a+x; x=x+1;  } while(x<4)"

rst=analizar_ascendente(cadena4)
tab = TablaDeSimbolos(None)
if rst is None :
    print("Error")
    #print(rst.str_arbol());
    rst.ejecutar_3D(tab)
    tab.terminar_codigo_3d()
    from Contenido.Optimo import Optimo
    Optm:Optimo = Optimo(tab.codigo_3d)
    lst_sal = Optm.codigo_optimizado()
    tab.imprimir_codigo_3d(lst_sal)


    #print(tab.codigo_3d)
    #tab.imprimir_temporales()


