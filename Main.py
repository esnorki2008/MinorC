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


cadena2='''

int fibo(int n)
{
    if(n == 0)
       return n;
    if ( n == 1 )
        return n;
    else
       return fibo(n - 2) + fibo(n - 1);
}

int main() {
    int a=(fibo(7));
    printf(a);
    return 0;
}
'''

cadena3='''


struct punto {
    int x,h;
    int y;
}
int main()
{
    
    int arre[11];
    arre[0]=1;
    arre[1]=5;
    arre[2]=6;
    arre[3]=7;
    arre[4]=14;
    arre[5]=64;
    arre[6]=34;
    arre[7]=22;
    arre[8]=21;
    arre[9]=20;
    
    for (int j=0;j<10;j++){
        for (int i=0;i<9;i++){
            if(arre[i]>arre[i+1]){
                int tempo = arre[i+1];
                arre[i+1] = arre[i];
                arre[i] = tempo;
            }
        }
    }
    
    for (int i=0;i<10;i++){
            printf(arre[i]);
            printf("\n");
    }
}
'''

cadena4 = '''

int main()
{
    int a=0;
    int b=0;
    b = -b;
    a=b;
    b=a;
    b=0+b;
    b=b+0;
    b=0-b;
    b=b-0;
    b=1*b;
    b=b*1;
    b=1/b;
    b=b/1;
    b=a+0;
    b=0+a;
    b=a-0;
    b=0-a;
    b=a*1;
    b=1*a;
    b=a/1;
    b=1/a;
    b=a*2;
    b=2*a;
    b=a*0;
    b=0*a;
    b=0/a;
    
    
    
}
'''
rst=analizar_ascendente(cadena4)
tab = TablaDeSimbolos(None)
if rst is None :
    print("Error")
else:
    #print(rst.str_arbol());
    rst.ejecutar_3D(tab)
    tab.terminar_codigo_3d()
    from Contenido.Optimo import Optimo
    Optm:Optimo = Optimo(tab.codigo_3d)
    lst_sal = Optm.codigo_optimizado()
    tab.imprimir_codigo_3d(lst_sal)


    #print(tab.codigo_3d)
    #tab.imprimir_temporales()


