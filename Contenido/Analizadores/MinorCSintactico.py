from .MinorCLexico import *
import ply.lex as lex
import ply.yacc as yacc
from Contenido.Instrucciones.NodoBinario import NodoBinario
from Contenido.Instrucciones.Hoja import Hoja
from Contenido.Instrucciones.Temporal import Temporal

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),

)
def p_inicio(t):
    'inicio    : expresiones'
    t[0]=t[1]

def p_expresiones(t):
    '''expresiones : expresiones MAS expresiones
                    | expresiones MENOS expresiones
                    | expresiones POR expresiones
                    | expresiones DIVIDIDO expresiones'''
    t[0] =  NodoBinario(t[1],t[2],t[3])


def p_expresiones_sola(t):
    'expresiones : valor'
    t[0] = t[1]


def p_expresiones_parentesis(t):
    'expresiones : PARA expresiones PARC'
    t[0] = t[2]


def p_valor(t):
    'valor : ENTERO'
    t[0]= Hoja(Temporal(t[1],0))

def analizar_ascendente(input: str):
    # Construyendo el analizador léxico
    lexer = lex.lex()
    parsito = yacc.yacc()
    return parsito.parse(input)