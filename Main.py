from Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from Contenido.TablaDeSimbolos import TablaDeSimbolos

#cadena="int x=0; int a=0; do { a=a+x; x=x+1;  } while(x<4)"









cadena1 = '''
        int main(){

            int m=factorial(5);
            printf(m);
        }

        int factorial(int n) {
            if (n>=1)
        return n*factorial(n-1);
            else
        return 1;


}

'''







cadena3='''int main() {
    int x = Ackerman(3,4);
    printf( x );
    return 0;
}

int Ackerman(int m, int n)
{
    if(m==0)
      return n+1;
    
        if(n==0)
           return Ackerman(m-1, 1);
        
           return Ackerman(m-1, Ackerman(m, n-1));
    
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

cadena4='''
int main()
{
    int num=2;
     switch(num+9)
     {
         case 1+10:
           printf(11);
         case 2:
           printf(2);
         case 3:
           printf(3);
         default:
           printf(num+2);
    }
   
   return 0;
}
'''
cadena5='''
int main()
{
    int f=1;
    f+=2+8+8;
    printf(f);
   
}
'''
rst=analizar_ascendente(cadena5)
tab = TablaDeSimbolos(None)
if rst is None :
    print("Error")
else:
    pass
    rst.ejecutar_3D(tab)
    tab.imprimir_codigo_3d()
    #print(tab.codigo_3d)
    #tab.imprimir_temporales()


