from Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from Contenido.TablaDeSimbolos import TablaDeSimbolos

cadena="int x=0; int a=0; while(x<4) { a=a+x; x=x+1;  } while(x<4) { a=a+x; x=x+1;  }"
#cadena = "int x=0; x=x+5+(x+x);"
#"8/2*(2%2)/5+8"
rst=analizar_ascendente(cadena)
tab = TablaDeSimbolos(None)
if rst is None :
    print("Error")
else:
    rst.ejecutar_3D(tab)
    tab.imprimir_codigo_3d()
    #print(tab.codigo_3d)
    #tab.imprimir_temporales()
