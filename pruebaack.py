#import sys
#sys.setrecursionlimit(10**6)

from AProyecto2.Main import Proyecto2

pro = Proyecto2()
cadenita = '''
    
    int main(){
        int a=5;
    }
'''
pro.analizar_minor_c_optimizar_3D(cadenita);
print(pro.reporte_errores())