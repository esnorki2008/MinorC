from .MinorCLexico import *
import ply.lex as lex
import ply.yacc as yacc
from Contenido.Instrucciones.NodoBinario import NodoBinario
from Contenido.Instrucciones.Hoja import Hoja
from Contenido.Instrucciones.Temporal import Temporal
from Contenido.Instrucciones.Listas.ListaInstruccion import ListaInstruccion
from Contenido.Instrucciones.Listas.ListaMetodos import ListaMetodos
from Contenido.Instrucciones.Declaracion import Declaracion
from Contenido.Instrucciones.NodoUnario import NodoUnario
from Contenido.Instrucciones.ValorVariable import ValorVariable
from Contenido.Instrucciones.Asignacion import Asignacion

from Contenido.Instrucciones.Sentencias.FuncFor import FuncFor
from Contenido.Instrucciones.Sentencias.FuncWhile import FuncWhile
from Contenido.Instrucciones.Sentencias.FuncDoWhile import FuncDoWhile
from Contenido.Instrucciones.Sentencias.FuncIf import FuncIf
from Contenido.Instrucciones.Sentencias.FuncMetodo import FuncMetodo
from  Contenido.Instrucciones.Sentencias.LlamarFuncMetodo import LlamarFuncMetodo
from Contenido.Instrucciones.Sentencias.FuncReturn import FuncReturn
from Contenido.Instrucciones.Sentencias.CuerpoSwitch import CuerpoSwitch
from Contenido.Instrucciones.Sentencias.FuncSwitch import FuncSwitch
from Contenido.Instrucciones.Sentencias.Variaciones import Variaciones

from Contenido.Instrucciones.FuncionesPropias.FuncPrintF import FuncPrintF

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'ORB'),
    ('left', 'XORB'),
    ('left', 'ANDB'),
    ('left', 'IGUALDOBLE', 'DIFERENTE'),
    ('left', 'MAYOR', 'MAYORIGUAL', 'MENOR', 'MENORIGUAL'),
    ('left', 'SHIFTI', 'SHIFTD'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO', 'MOD'),
    ('right', 'UMENOS', 'UMAS', 'NOT', 'NOTB','UAND','MASDOBLE','MENOSDOBLE'),
)


def p_inicio(t):
    'inicio    : lista_metodos'
    t[0] = t[1]

def p_metodos_lista(t):
    'lista_metodos : lista_metodos metodos'
    t[0]=t[1]
    t[0].agregar(t[2])

def p_metodos_lista_solo(t):
    'lista_metodos :  metodos'
    t[0]=ListaMetodos([t[1]])

def p_metodos_declara(t):
    'metodos : tipo IDENTIFICADOR PARA parametros PARC instruccion'
    tp = find_column(entrada, t.slice[2])
    t[0]=FuncMetodo(t[2],t[4],t[6],tp)

def p_metodos_declara_parametros_muchos(t):
    'parametros : parametros COMA tipo IDENTIFICADOR'
    t[0]=t[1]
    tupla = (t[3], t[4])
    t[0].append(tupla)

def p_metodos_declara_parametros_solo(t):
    'parametros : tipo IDENTIFICADOR'
    t[0]=[]
    tupla = (t[1], t[2])
    t[0].append(tupla)

def p_metodos_declara_parametros_solo_va(t):
    'parametros : '
    t[0]=[]

def p_instruccion(t):
    'instrucciones : instrucciones instruccion '
    t[0] = t[1]
    t[0].agregar(t[2])


def p_instrucciones_inicio(t):
    'instrucciones : instruccion '
    t[0] = ListaInstruccion([t[1]])
#===================================Structs================
def p_declaracion_struct(t):
    'instruccion : STRUCT IDENTIFICADOR LLAA instrucciones LLAC'

#==============================Definicion De COntenido Instruccioon===============
def p_sentencia_encapsulado(t):
    '''instruccion : LLAA  instrucciones LLAC'''
    t[0]=t[2]

def p_sentencia_encapsulado_vacia(t):
    '''instruccion : LLAA   LLAC'''
    t[0] = ListaInstruccion([])

def p_instruccion_ciclo(t):
    'instruccion : instruccion_ciclo'
    t[0]=t[1]

def p_instruccion_abierta_inst(t):
    'instruccion : instruccion_abierta'
    t[0]=t[1]

def p_instruccion_llamado_metodos(t):
    'instruccion : instruccion_llamar_metodo'
    t[0]=t[1]

#================================Llamado De Metodos===========
def p_llamar_retorno_metodo(t):
    'instruccion_llamar_metodo : RETURN expresiones PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0]=FuncReturn(t[2],tp)

def p_llamar_funcion_generica(t):
    'instruccion_llamar_metodo : IDENTIFICADOR PARA listado_parametros PARC PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0] = LlamarFuncMetodo(t[1],t[3],tp)
def p_llamar_scanf(t):
    'instruccion_llamar_metodo : PRINTF PARA listado_parametros PARC PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncPrintF(t[3],tp)

def p_listatdo_parametros_muchos_posibles(t):
    'listado_parametros : listado_parametros COMA expresiones'
    t[0]=t[1]
    t[0].append(t[3])

def p_listatdo_parametros_solo_val(t):
    'listado_parametros : expresiones'
    t[0]=[t[1]]

def p_listatdo_parametros_solo_s(t):
    'listado_parametros : '
    t[0]=[]

#===============================Instrucciones CIclicos=================
def p_instruccion_while(t):
    'instruccion_ciclo : WHILE PARA expresiones PARC   instruccion '
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncWhile(t[3], t[5], tp)


def p_instruccion_do_while(t):
    'instruccion_ciclo : DO  instruccion  WHILE PARA expresiones PARC PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncDoWhile(t[5], t[2], tp)

def p_instruccion_a_normal(t):
    'instruccion_ciclo : variaciones'
    t[0]=t[1]

def p_instruccion_variacioin_mas(t):
    'variaciones : IDENTIFICADOR MASDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1], t[2], tp)

def p_instruccion_variacioin_menos(t):
    'variaciones : IDENTIFICADOR MENOSDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1], t[2], tp)



def p_instruccion_for(t):
    'instruccion_ciclo : FOR PARA instruccion  expresiones PUNTOCOMA   finfor PARC instruccion'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncFor(t[3],t[4],t[6],t[8], tp)

def p_instruciion_for_no_epsilon(t):
    'finfor : instruccion'
    t[0] = t[1]

def p_instruciion_for_epsilon(t):
    'finfor : '
    t[0] = None



#=========================================Instrucciones Booleanos=============
def p_instruccion_abierta_definicion_solo_if(t):
    '''instruccion_abierta : IF PARA expresiones PARC instruccion'''
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]=FuncIf(t[3],t[5],None,tp)
def p_instruccion_abierta_definicion_if_else(t):
    '''instruccion_abierta :  IF PARA expresiones PARC instruccion ELSE instruccion'''
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncIf(t[3], t[5], t[7], tp)

def p_instruccion_abierta_definicion_switch(t):
    '''instruccion_abierta :  SWITCH PARA expresiones PARC LLAA switch_corpo LLAC'''
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]= FuncSwitch(t[3],t[6],tp)

def p_instrucccion_abierta_cuerpo_swtich_mult(t):
    'switch_corpo : switch_corpo switch_corpo_salida'
    t[0] = t[1]
    t[0].append(t[2])
def p_instrucccion_abierta_cuerpo_swtich_solo(t):
    'switch_corpo : switch_corpo_salida'
    t[0]=[t[1]]

def p_instrucccion_abierta_cuerpo_swtich_inter(t):
    'switch_corpo_salida : CASE expresiones DOBLEPUNTO instrucciones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]=CuerpoSwitch(t[2], t[4],tp)

def p_instrucccion_abierta_cuerpo_swtich_inter_defecto(t):
    'switch_corpo_salida : DEFAULT DOBLEPUNTO instrucciones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]=CuerpoSwitch(None,t[3],tp)
#=========================================Instruccion Declaracions===============
def p_tipo(t):
    '''tipo : CHAR
            | INT
            | DOUBLE
            | FLOAT'''
    if t[1]=="char":
        t[0]=2
    elif t[1]=="int":
        t[0]=0
    elif t[1]=="double":
        t[0]=1
    elif t[1]=="float":
        t[0]=2
    else:
        t[0]=-1




def p_instruccion_declaracion(t):
    'instruccion : tipo mdecla IGUAL expresiones PUNTOCOMA'


    global entrada
    tp = find_column(entrada, t.slice[3])
    t[0] = Declaracion(t[2], t[4], t[1], tp)


def p_instruccion_asignacion(t):
    'instruccion : mdecla m_igual expresiones PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[4])
    t[0] = Asignacion(t[1], t[3],t[2], tp)

def p_instruccion_igualaciones(t):
    '''m_igual : IGUAL
            | MASIGUAL
            | MENOSIGUAL
            | PORIGUAL
            | DIVIGUAL
            | SHIFTIIGUAL
            | SHIFTDIGUAL
            | ANDIGUAL
            | XORIGUAL
            | ORIGUAL'''
    t[0] = t[1]

def p_muchas_declaraciones_variables(t):
    'mdecla : mdecla COMA IDENTIFICADOR'
    t[0] = t[1]
    t[0].append(t[3])


def p_muchas_declaraciones_variables_ini(t):
    'mdecla : IDENTIFICADOR'
    t[0] = [t[1]]




def p_expresiones_binarias(t):
    '''expresiones : expresiones OR expresiones
                    | expresiones AND expresiones

                    | expresiones ORB expresiones
                    | expresiones XORB expresiones
                    | expresiones ANDB expresiones

                    | expresiones IGUALDOBLE expresiones
                    | expresiones DIFERENTE expresiones


                    | expresiones MAYOR expresiones
                    | expresiones MAYORIGUAL expresiones
                    | expresiones MENOR expresiones
                    | expresiones MENORIGUAL expresiones

                    | expresiones SHIFTI expresiones
                    | expresiones SHIFTD expresiones

                    | expresiones MAS expresiones
                    | expresiones MENOS expresiones

                    | expresiones POR expresiones
                    | expresiones MOD expresiones
                    | expresiones DIVIDIDO expresiones'''

    global entrada
    tp = find_column(entrada, t.slice[2])
    t[0] = NodoBinario(t[1], t[2], t[3], tp)


def p_expresiones_unarias(t):
    '''expresiones : MENOS expresiones %prec UMENOS
                    | MAS expresiones %prec UMAS
                    | NOTB expresiones
                    | ANDB expresiones %prec UAND
                    | NOT expresiones '''

    global entrada
    tp = find_column(entrada, t.slice[1])

    t[0] = NodoUnario(t[1], t[2], tp)


def p_expresiones_sola(t):
    'expresiones : valor'
    t[0] = t[1]



def p_expresiones_parentesis(t):
    'expresiones : PARA expresiones PARC'
    t[0] = t[2]


def p_valor_entero(t):
    'valor : ENTERO'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Hoja(Temporal(t[1], 0), tp)

def p_valor_decimal(t):
    'valor : DECIMAL'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Hoja(Temporal(t[1], 1), tp)


def p_valor_cadena(t):
    'valor : CADENA'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Hoja(Temporal(t[1], 2), tp)

def p_valor_variable(t):
    'valor : IDENTIFICADOR'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = ValorVariable(t[1], tp)

def p_valor_variable_inc(t):
    'expresiones : IDENTIFICADOR MASDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1],t[2], tp)

def p_valor_variable_dec(t):
    'expresiones : IDENTIFICADOR MENOSDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1],t[2], tp )

def p_valor_funcion_llamado(t):
    'valor : IDENTIFICADOR PARA listado_parametros PARC'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = LlamarFuncMetodo(t[1],t[3], tp)

def p_error(t):
    print("Error sintáctico en '%s'" % t)


def find_column(input, token):
    if token is None:
        return (0, 0)
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1, token.lineno)


entrada = ""


def analizar_ascendente(input: str):
    # Construyendo el analizador léxico
    lexer = lex.lex()
    global entrada
    entrada = input
    parsito = yacc.yacc()
    return parsito.parse(input)
