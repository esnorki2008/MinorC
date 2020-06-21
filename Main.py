from Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from Contenido.TablaDeSimbolos import TablaDeSimbolos

#cadena="int x=0; int a=0; do { a=a+x; x=x+1;  } while(x<4)"




cadena='''int main() {
    int x = Ackerman(3,4);
    printf( x );
    return 0;
}

int Ackerman(int m, int n)
{
    if(m==0)
      return n+1;
    else
    {
        if(n==0)
           return 1*Ackerman(m-1, 1);
        else
           return 1*Ackerman(m-1, Ackerman(m, n-1));
    }
}

'''


cadena='''int main() {
    printf(fibo(3));
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


cadena = '''
        int main(){

            int m=factorial(5,8);
            printf(m);
        }

        int factorial(int n,int k) {
            if (n>=1)
        return n*factorial(n-1,2);
            else
        return 1;


}

'''

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


