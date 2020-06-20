from .MinorCLexico import *
import ply.lex as lex
import ply.yacc as yacc
from Contenido.Instrucciones.NodoBinario import NodoBinario
from Contenido.Instrucciones.Hoja import Hoja
from Contenido.Instrucciones.Temporal import Temporal
from Contenido.Instrucciones.ListaInstruccion import ListaInstruccion
from Contenido.Instrucciones.Declaracion import Declaracion
from Contenido.Instrucciones.NodoUnario import NodoUnario
from Contenido.Instrucciones.ValorVariable import ValorVariable
from Contenido.Instrucciones.Asignacion import Asignacion
from Contenido.Instrucciones.Funciones.FuncWhile import  FuncWhile
precedence = (
    ('left','IGUALDOBLE','DIFERENTE'),
    ('left','MAYOR','MAYORIGUAL','MENOR','MENORIGUAL'),
    ('left','SHIFTI','SHIFTD'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO','MOD'),
    ('right','UMENOS','UMAS','NOT','NOTB'),
)
def p_inicio(t):
    'inicio    : instrucciones'
    t[0]=t[1]

def p_instrucciones(t):
    'instrucciones : instrucciones instruccion '
    t[0] = t[1]
    t[0].agregar(t[2])


def p_instrucciones_inicio(t):
    'instrucciones : instruccion '
    t[0]=ListaInstruccion([t[1]])


def p_tipo(t):
    '''tipo : CHAR
            | INT
            | DOUBLE
            | FLOAT
            | IDENTIFICADOR'''
    t[0]=t[1]

def p_instruccion_declaracion(t):
    'instruccion : tipo mdecla IGUAL expresiones PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[3])
    t[0]=Declaracion(t[2], t[4], t[1], tp)

def p_instruccion_asignacion(t):
    'instruccion : mdecla IGUAL expresiones PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[2])
    t[0]=Asignacion(t[1], t[3], tp)

def p_instruccion_while(t):
    'instruccion : WHILE PARA expresiones PARC LLAA instrucciones LLAC'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncWhile(t[3], t[6], tp)

def p_muchas_declaraciones_variables(t):
    'mdecla : mdecla COMA IDENTIFICADOR'
    t[0]=t[1]
    t[0].append(t[3])

def p_muchas_declaraciones_variables_ini(t):
    'mdecla : IDENTIFICADOR'
    t[0]=[t[1]]

def p_expresiones_binarias(t):
    '''expresiones : expresiones IGUALDOBLE expresiones
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
    t[0] =  NodoBinario(t[1],t[2],t[3],tp)


def p_expresiones_unarias(t):
    '''expresiones : MENOS expresiones %prec UMENOS
                    | MAS expresiones %prec UMAS
                    | NOTB expresiones
                    | NOT expresiones '''

    global entrada
    tp = find_column(entrada, t.slice[1])

    t[0]=NodoUnario(t[1],t[2],tp)

def p_expresiones_sola(t):
    'expresiones : valor'
    t[0] = t[1]


def p_expresiones_parentesis(t):
    'expresiones : PARA expresiones PARC'
    t[0] = t[2]


def p_valor_entero(t):
    'valor : ENTERO'
    global  entrada
    tp=find_column(entrada,t.slice[1])
    t[0]= Hoja(Temporal(t[1],0),tp)

def p_valor_variable(t):
    'valor : IDENTIFICADOR'
    global  entrada
    tp=find_column(entrada,t.slice[1])
    t[0]= ValorVariable(t[1],tp)

def p_error(t):
    print("Error sintáctico en '%s'" % t)


def find_column(input, token):
    if token is None:
        return (0,0)
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1, token.lineno)


entrada = ""
def analizar_ascendente(input: str):
    # Construyendo el analizador léxico
    lexer = lex.lex()
    global  entrada
    entrada=input
    parsito = yacc.yacc()
    return parsito.parse(input)

