from Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from Contenido.TablaDeSimbolos import TablaDeSimbolos

#cadena="int x=0; int a=0; do { a=a+x; x=x+1;  } while(x<4)"









cadena1 = '''
        int main(){

            int m=factorial(factorial(3));
            printf(m);
        }

        int factorial(int n) {
            if (n>=1)
        return n*factorial(n-1);
            else
        return 1;


}

'''


cadena2='''int main() {
    int a=(fibo(7));
    printf(a);
    return 0;
}

int fibo(int n)
{
    if(n == 0)
       return n;
    if ( n == 1 )
        return n;
    else
       return fibo(n - 2) + fibo(n - 1);
}
'''

cadena3='''


struct punto {
    int x,h;
    int y;
}
int main()
{
    struct punto mivar;
    mivar.x+=1;
    mivar.x*=9;
    int g=mivar.x+8*8;
    g +=5+scanf();
    printf(g);    
}
'''

rst=analizar_ascendente(cadena3)
tab = TablaDeSimbolos(None)
if rst is None :
    print("Error")
else:
    pass
    rst.ejecutar_3D(tab)
    tab.imprimir_codigo_3d()
    #print(tab.codigo_3d)
    #tab.imprimir_temporales()


