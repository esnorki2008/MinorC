from .MinorCLexico import *
import ply.lex as lex
import ply.yacc as yacc
from AProyecto2.Contenido.Instrucciones.NodoBinario import NodoBinario
from AProyecto2.Contenido.Instrucciones.Hoja import Hoja
from AProyecto2.Contenido.Instrucciones.Temporal import Temporal
from AProyecto2.Contenido.Instrucciones.Listas.ListaInstruccion import ListaInstruccion
from AProyecto2.Contenido.Instrucciones.Listas.ListaMetodos import ListaMetodos
from AProyecto2.Contenido.Instrucciones.Declaracion import Declaracion
from AProyecto2.Contenido.Instrucciones.NodoUnario import NodoUnario
from AProyecto2.Contenido.Instrucciones.ValorVariable import ValorVariable
from AProyecto2.Contenido.Instrucciones.Asignacion import Asignacion

from AProyecto2.Contenido.Instrucciones.Sentencias.FuncFor import FuncFor
from AProyecto2.Contenido.Instrucciones.Sentencias.FuncWhile import FuncWhile
from AProyecto2.Contenido.Instrucciones.Sentencias.FuncDoWhile import FuncDoWhile
from AProyecto2.Contenido.Instrucciones.Sentencias.FuncIf import FuncIf
from AProyecto2.Contenido.Instrucciones.Sentencias.FuncMetodo import FuncMetodo
from  AProyecto2.Contenido.Instrucciones.Sentencias.LlamarFuncMetodo import LlamarFuncMetodo
from AProyecto2.Contenido.Instrucciones.Sentencias.FuncReturn import FuncReturn
from AProyecto2.Contenido.Instrucciones.Sentencias.CuerpoSwitch import CuerpoSwitch
from AProyecto2.Contenido.Instrucciones.Sentencias.FuncSwitch import FuncSwitch
from AProyecto2.Contenido.Instrucciones.Sentencias.Variaciones import Variaciones

from AProyecto2.Contenido.Instrucciones.FuncionesPropias.FuncPrintF import FuncPrintF
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.FuncScanf import FuncScanF
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.FuncSizeof import FuncSizeof
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.FuncBreak import FuncBreak
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.FuncContinue import FuncContinue
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.Cast import Cast
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.Ternario import Ternario
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.FuncLabel import FuncLabel
from AProyecto2.Contenido.Instrucciones.FuncionesPropias.Goto import Goto


from AProyecto2.Contenido.Instrucciones.Estructuras.ContenidoStruct import ContenidoStruct
from AProyecto2.Contenido.Instrucciones.Estructuras.DefinirStruct import DefinirStruct
from AProyecto2.Contenido.Instrucciones.Estructuras.DeclaracionStruct import DeclaracionStruct
from AProyecto2.Contenido.Instrucciones.Estructuras.AsignarStruct import AsignarStruct
from AProyecto2.Contenido.Instrucciones.Estructuras.ValorStruct import ValorStruct

precedence = (
    ('right', 'INTERROGACION', 'DOBLEPUNTO'),
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
    ('right', 'UMENOS', 'UMAS', 'NOT', 'NOTB','UAND','MASDOBLE','MENOSDOBLE','CASTINT','CASTDOUBLE','CASTFLOAT','CASTCHAR'),
)


def p_inicio(t):
    'inicio    : lista_metodos'
    t[0] = t[1]
    global min_lst_repga
    repg_inst='inicio : lista_metodo'
    repga_sema="t[0]=t[1]"
    min_lst_repga.append((repg_inst,repga_sema))

    
def p_metodos_lista(t):
    'lista_metodos : lista_metodos metodos'
    t[0]=t[1]
    t[0].agregar(t[2])

    global min_lst_repga
    repg_inst = 'lista_metodos : lista_metodos metodos'
    repga_sema = '''t[0]=t[1]
    t[0].agregar(t[2])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_metodos_lista_solo(t):
    'lista_metodos :  metodos'
    t[0]=ListaMetodos([t[1]])

    global min_lst_repga
    repg_inst = 'lista_metodos :  metodos'
    repga_sema = '''t[0]=ListaMetodos([t[1]])'''
    min_lst_repga.append((repg_inst, repga_sema))
#=================================Declaracion Global Variables=========
def p_declaracion_var_glonal(t):
    'metodos : instruccion'
    t[0] = t[1]

    global min_lst_repga
    repg_inst = 'metodos : instruccion'
    repga_sema = '''t[0] = t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))
#===================================Structs================
def p_declaracion_struct_a(t):
    'metodos : STRUCT IDENTIFICADOR LLAA muhco_decla_struct LLAC PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0] = DefinirStruct(t[2], t[4], tp)

    global min_lst_repga
    repg_inst = 'metodos : STRUCT IDENTIFICADOR LLAA muhco_decla_struct LLAC'
    repga_sema = '''tp = find_column(entrada, t.slice[1])
    t[0] = DefinirStruct(t[2], t[4], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_declaracion_struct_lista(t):
    'muhco_decla_struct : muhco_decla_struct decla_struct'
    t[0]=t[1]
    t[0].append(t[2])

    global min_lst_repga
    repg_inst = 'muhco_decla_struct : muhco_decla_struct decla_struct'
    repga_sema = '''t[0]=t[1]
    t[0].append(t[2])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_declaracion_struct_epsilon(t):
    'muhco_decla_struct : decla_struct'
    t[0]=[t[1]]

    global min_lst_repga
    repg_inst = 'muhco_decla_struct : decla_struct'
    repga_sema = '''t[0]=[t[1]]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_declaracion_struct_puntual(t):
    'decla_struct : tipo mdecla  corche PUNTOCOMA'
    tp = find_column(entrada, t.slice[4])
    t[0]=ContenidoStruct(t[1],t[2],tp,t[3])

    global min_lst_repga
    repg_inst = 'decla_struct : tipo mdecla  PUNTOCOMA'
    repga_sema = '''tp = find_column(entrada, t.slice[3])
    t[0]=ContenidoStruct(t[1],t[2],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

#===============================Metodos==========
def p_metodos_declara(t):
    'metodos : tipo IDENTIFICADOR PARA parametros PARC instruccion'
    tp = find_column(entrada, t.slice[2])
    t[0]=FuncMetodo(t[2],t[4],t[6],tp)

    global min_lst_repga
    repg_inst = 'metodos : tipo IDENTIFICADOR PARA parametros PARC instruccion'
    repga_sema = '''tp = find_column(entrada, t.slice[2])
    t[0]=FuncMetodo(t[2],t[4],t[6],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_metodos_declara_parametros_muchos(t):
    'parametros : parametros COMA tipo IDENTIFICADOR'
    t[0]=t[1]
    tupla = (t[3], t[4])
    t[0].append(tupla)

    global min_lst_repga
    repg_inst = 'parametros : parametros COMA tipo IDENTIFICADOR'
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_metodos_declara_parametros_solo(t):
    'parametros : tipo IDENTIFICADOR'
    t[0]=[]
    tupla = (t[1], t[2])
    t[0].append(tupla)

    global min_lst_repga
    repg_inst = 'parametros : tipo IDENTIFICADOR'
    repga_sema = '''t[0]=[]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_metodos_declara_parametros_solo_va(t):
    'parametros : '
    t[0]=[]

    global min_lst_repga
    repg_inst = 'parametros : '
    repga_sema = '''t[0]=[]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion(t):
    'instrucciones : instrucciones instruccion '
    t[0] = t[1]
    t[0].agregar(t[2])

    global min_lst_repga
    repg_inst = 'instrucciones : instrucciones instruccion '
    repga_sema = '''t[0] = t[1]
    t[0].agregar(t[2])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instrucciones_inicio(t):
    'instrucciones : instruccion '
    t[0] = ListaInstruccion([t[1]])

    global min_lst_repga
    repg_inst = 'instrucciones : instruccion '
    repga_sema = '''t[0] = ListaInstruccion([t[1]])'''
    min_lst_repga.append((repg_inst, repga_sema))
#=============================Etiquetas==========================================
def p_sentencia_etiqueta_definicion(t):
    '''instruccion : IDENTIFICADOR DOBLEPUNTO'''
    tp = find_column(entrada, t.slice[1])
    t[0]=FuncLabel(t[1],tp)
def p_sentencia_etiqueta_goto(t):
    '''instruccion : GOTO IDENTIFICADOR PUNTOCOMA'''
    tp = find_column(entrada, t.slice[1])
    t[0] = Goto(t[2], tp)
#==============================Definicion De COntenido Instruccioon===============
def p_sentencia_encapsulado(t):
    '''instruccion : LLAA  instrucciones LLAC'''
    t[0]=t[2]

    global min_lst_repga
    repg_inst = '''instruccion : LLAA  instrucciones LLAC'''
    repga_sema = '''t[0]=t[2]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_sentencia_encapsulado_vacia(t):
    '''instruccion : LLAA   LLAC'''
    t[0] = ListaInstruccion([])

    global min_lst_repga
    repg_inst = '''instruccion : LLAA   LLAC'''
    repga_sema = '''t[0] = ListaInstruccion([])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_ciclo(t):
    'instruccion : instruccion_ciclo'
    t[0]=t[1]

    global min_lst_repga
    repg_inst = 'instruccion : instruccion_ciclo'
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_abierta_inst(t):
    'instruccion : instruccion_abierta'
    t[0]=t[1]

    global min_lst_repga
    repg_inst = 'instruccion : instruccion_abierta'
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_llamado_metodos(t):
    'instruccion : instruccion_llamar_metodo'
    t[0]=t[1]

    global min_lst_repga
    repg_inst = 'instruccion : instruccion_llamar_metodo'
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

#===============================Instrucciones Internas========
def p_interna_break(t):
    'instruccion_llamar_metodo : BREAK  PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0]=FuncBreak(tp)

    global min_lst_repga
    repg_inst = 'instruccion_llamar_metodo : BREAK  PUNTOCOMA'
    repga_sema = '''tp = find_column(entrada, t.slice[1])
    t[0]=FuncBreak(tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_interna_continue(t):
    'instruccion_llamar_metodo : CONTINUE  PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0]=FuncContinue(tp)

    global min_lst_repga
    repg_inst = 'instruccion_llamar_metodo : CONTINUE  PUNTOCOMA'
    repga_sema = '''tp = find_column(entrada, t.slice[1])
    t[0]=FuncContinue(tp)'''
    min_lst_repga.append((repg_inst, repga_sema))
#================================Llamado De Metodos===========
def p_llamar_retorno_metodo(t):
    'instruccion_llamar_metodo : RETURN expresiones PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0]=FuncReturn(t[2],tp)

    global min_lst_repga
    repg_inst = 'instruccion_llamar_metodo : RETURN expresiones PUNTOCOMA'
    repga_sema = '''tp = find_column(entrada, t.slice[1])
    t[0]=FuncReturn(t[2],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_llamar_funcion_generica(t):
    'instruccion_llamar_metodo : IDENTIFICADOR PARA listado_parametros PARC PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0] = LlamarFuncMetodo(t[1],t[3],tp)

    global min_lst_repga
    repg_inst = 'instruccion_llamar_metodo : IDENTIFICADOR PARA listado_parametros PARC PUNTOCOMA'
    repga_sema = '''tp = find_column(entrada, t.slice[1])
    t[0] = LlamarFuncMetodo(t[1],t[3],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_llamar_printf_algo(t):
    'instruccion_llamar_metodo : PRINTF PARA listado_parametros PARC PUNTOCOMA'
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncPrintF(t[3],tp)

    global min_lst_repga
    repg_inst = 'instruccion_llamar_metodo : PRINTF PARA listado_parametros PARC PUNTOCOMA'
    repga_sema = '''tp = find_column(entrada, t.slice[1])
    t[0] = FuncPrintF(t[3],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_listatdo_parametros_muchos_posibles(t):
    'listado_parametros : listado_parametros COMA expresiones'
    t[0]=t[1]
    t[0].append(t[3])

    global min_lst_repga
    repg_inst =  'listado_parametros : listado_parametros COMA expresiones'
    repga_sema = '''t[0]=t[1]
    t[0].append(t[3])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_listatdo_parametros_solo_val(t):
    'listado_parametros : expresiones'
    t[0]=[t[1]]

    global min_lst_repga
    repg_inst = 'listado_parametros : expresiones'
    repga_sema = '''t[0]=[t[1]]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_listatdo_parametros_solo_s(t):
    'listado_parametros : '
    t[0]=[]

    global min_lst_repga
    repg_inst = 'listado_parametros : '
    repga_sema = '''t[0]=[]'''
    min_lst_repga.append((repg_inst, repga_sema))

#===============================Instrucciones CIclicos=================
def p_instruccion_while(t):
    'instruccion_ciclo : WHILE PARA expresiones PARC   instruccion '
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncWhile(t[3], t[5], tp)

    global min_lst_repga
    repg_inst = 'instruccion_ciclo : WHILE PARA expresiones PARC   instruccion '
    repga_sema = '''t[0] = FuncWhile(t[3], t[5], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_do_while(t):
    'instruccion_ciclo : DO  instruccion  WHILE PARA expresiones PARC PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncDoWhile(t[5], t[2], tp)

    global min_lst_repga
    repg_inst = 'instruccion_ciclo : DO  instruccion  WHILE PARA expresiones PARC PUNTOCOMA'
    repga_sema = '''t[0] = FuncDoWhile(t[5], t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_a_normal(t):
    'instruccion_ciclo : variaciones'
    t[0]=t[1]

    global min_lst_repga
    repg_inst = 'instruccion_ciclo : variaciones'
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_variacioin_mas(t):
    'variaciones : IDENTIFICADOR MASDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1], t[2], tp)

    global min_lst_repga
    repg_inst = 'variaciones : IDENTIFICADOR MASDOBLE'
    repga_sema = '''t[0] = Variaciones(t[1], t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_variacioin_menos(t):
    'variaciones : IDENTIFICADOR MENOSDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1], t[2], tp)

    global min_lst_repga
    repg_inst = 'variaciones : IDENTIFICADOR MENOSDOBLE'
    repga_sema = '''t[0] = Variaciones(t[1], t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_for(t):
    'instruccion_ciclo : FOR PARA instruccion  expresiones PUNTOCOMA   finfor PARC instruccion'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncFor(t[3],t[4],t[6],t[8], tp)

    global min_lst_repga
    repg_inst = 'instruccion_ciclo : FOR PARA instruccion  expresiones PUNTOCOMA   finfor PARC instruccion'
    repga_sema = '''t[0] = FuncFor(t[3],t[4],t[6],t[8], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruciion_for_no_epsilon(t):
    'finfor : instruccion'
    t[0] = t[1]

    global min_lst_repga
    repg_inst = 'finfor : instruccion'
    repga_sema = '''t[0] = t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruciion_for_epsilon(t):
    'finfor : '
    t[0] = None

    global min_lst_repga
    repg_inst = 'finfor : '
    repga_sema = '''t[0] = None'''
    min_lst_repga.append((repg_inst, repga_sema))


#=========================================Instrucciones Booleanos=============
def p_instruccion_abierta_definicion_solo_if(t):
    '''instruccion_abierta : IF PARA expresiones PARC instruccion'''
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]=FuncIf(t[3],t[5],None,tp)

    global min_lst_repga
    repg_inst = '''instruccion_abierta : IF PARA expresiones PARC instruccion'''
    repga_sema = '''t[0]=FuncIf(t[3],t[5],None,tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_abierta_definicion_if_else(t):
    '''instruccion_abierta :  IF PARA expresiones PARC instruccion ELSE instruccion'''
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncIf(t[3], t[5], t[7], tp)

    global min_lst_repga
    repg_inst = '''instruccion_abierta :  IF PARA expresiones PARC instruccion ELSE instruccion'''
    repga_sema = '''t[0] = FuncIf(t[3], t[5], t[7], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_abierta_definicion_switch(t):
    '''instruccion_abierta :  SWITCH PARA expresiones PARC LLAA switch_corpo LLAC'''
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]= FuncSwitch(t[3],t[6],tp)

    global min_lst_repga
    repg_inst = '''instruccion_abierta :  SWITCH PARA expresiones PARC LLAA switch_corpo LLAC'''
    repga_sema = '''t[0]= FuncSwitch(t[3],t[6],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instrucccion_abierta_cuerpo_swtich_mult(t):
    'switch_corpo : switch_corpo switch_corpo_salida'
    t[0] = t[1]
    t[0].append(t[2])

    global min_lst_repga
    repg_inst = 'switch_corpo : switch_corpo switch_corpo_salida'
    repga_sema = '''t[0] = t[1]
    t[0].append(t[2])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instrucccion_abierta_cuerpo_swtich_solo(t):
    'switch_corpo : switch_corpo_salida'
    t[0]=[t[1]]

    global min_lst_repga
    repg_inst = 'switch_corpo : switch_corpo_salida'
    repga_sema = '''t[0]=[t[1]]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instrucccion_abierta_cuerpo_swtich_inter(t):
    'switch_corpo_salida : CASE expresiones DOBLEPUNTO instrucciones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]=CuerpoSwitch(t[2], t[4],tp)

    global min_lst_repga
    repg_inst = 'switch_corpo_salida : CASE expresiones DOBLEPUNTO instrucciones'
    repga_sema = '''t[0]=CuerpoSwitch(t[2], t[4],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instrucccion_abierta_cuerpo_swtich_inter_defecto(t):
    'switch_corpo_salida : DEFAULT DOBLEPUNTO instrucciones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]=CuerpoSwitch(None,t[3],tp)

    global min_lst_repga
    repg_inst = 'switch_corpo_salida : DEFAULT DOBLEPUNTO instrucciones'
    repga_sema = '''t[0]=CuerpoSwitch(None,t[3],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

#=========================================Instruccion Declaracions===============
def p_tipo(t):
    '''tipo : CHAR
            | INT
            | DOUBLE
            | VOID
            | FLOAT'''
    if t[1]=="char":
        t[0]=2
    elif t[1]=="int":
        t[0]=0
    elif t[1]=="void":
        t[0]=0
    elif t[1]=="double":
        t[0]=1
    elif t[1]=="float":
        t[0]=1
    else:
        t[0]=t[2]

    global min_lst_repga
    repg_inst = '''tipo : CHAR
            | INT
            | DOUBLE
            | FLOAT'''
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

#=====================================Arreglos===============
def p_mucho_corchete(t):
    'corche : corche CORA expresiones CORC'
    t[0]=t[1]
    t[0].append(t[3])

    global min_lst_repga
    repg_inst = 'corche : corche CORA expresiones CORC'
    repga_sema = '''t[0]=t[1]
    t[0].append(t[3])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_mucho_corchete_epsilon(t):
    'corche : '
    t[0]=[]

    global min_lst_repga
    repg_inst = 'corche : '
    repga_sema = '''t[0]=[]'''
    min_lst_repga.append((repg_inst, repga_sema))

#===================Operaciones Con Structs==============
def p_instruccion_declaracion_struct(t):
    'instruccion : STRUCT IDENTIFICADOR IDENTIFICADOR corche PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0]=DeclaracionStruct(t[2],t[3],tp,t[4])

    global min_lst_repga
    repg_inst = 'instruccion : STRUCT IDENTIFICADOR IDENTIFICADOR corche PUNTOCOMA'
    repga_sema = '''t[0]=DeclaracionStruct(t[2],t[3],tp,t[4])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_asignar_valor_struct(t):
    'instruccion : IDENTIFICADOR  PUNTO  IDENTIFICADOR m_igual expresiones PUNTOCOMA'
    tp = find_column(entrada, t.slice[3])
    t[0]=AsignarStruct(t[1],t[3],t[5],t[4],tp)


    global min_lst_repga
    repg_inst = 'instruccion : IDENTIFICADOR  PUNTO  IDENTIFICADOR m_igual expresiones PUNTOCOMA'
    repga_sema = '''t[0]=AsignarStruct(t[1],t[3],t[5],t[4],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))


#====================Operaciones Con Variables Simples=========
def p_instruccion_asignacion(t):
    'instruccion : mdecla corche arre_str_val m_igual expresiones PUNTOCOMA '
    global entrada
    tp = find_column(entrada, t.slice[6])
    if t[3] is None:
        t[0] = Asignacion(t[1], t[5],t[4], tp,t[2])
    else:
        t[0] = t[0]=AsignarStruct(t[1],t[3],t[5],t[4],tp,t[2])

    global min_lst_repga
    repg_inst = 'instruccion : mdecla corche arre_str_val m_igual expresiones PUNTOCOMA '
    repga_sema = '''t[0] = t[0]=AsignarStruct(t[1],t[3],t[5],t[4],tp,t[2])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_a(t):
    'arre_str_val :   PUNTO IDENTIFICADOR  '
    t[0]=t[2]

    global min_lst_repga
    repg_inst = 'arre_str_val :   PUNTO IDENTIFICADOR  '
    repga_sema = '''t[0]=t[2]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_b(t):
    'arre_str_val : '
    t[0] = None

    global min_lst_repga
    repg_inst = 'arre_str_val : '
    repga_sema = '''t[0] = None'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_declaracion(t):
    'decla_con : tipo mdecla  IGUAL expresiones masinde  PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[3])
    t[0]=t[5]
    t[0].homogenizar_tipos(t[1]);
    t[0].agregar(Declaracion(t[2], t[4], t[1], tp))

    global min_lst_repga
    repg_inst = 'decla_con : tipo mdecla  IGUAL expresiones masinde PUNTOCOMA'
    repga_sema = '''t[0].agregar(Declaracion(t[2], t[4], t[1], tp))'''
    min_lst_repga.append((repg_inst, repga_sema))


def p_isntruccion_decla(t):
    'instruccion : def_decla '
    t[0]=t[1]

    global min_lst_repga
    repg_inst = 'instruccion : def_decla '
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_isntruccion_decla_real(t):
    '''def_decla : decla_con
                | decla_epsi '''
    t[0]=t[1]

    global min_lst_repga
    repg_inst = '''def_decla : decla_con
                | decla_epsi '''
    repga_sema = '''t[0]=t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_declaracion_vac(t):
    'decla_epsi : tipo mdecla  PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[3])
    t[0]= ListaInstruccion([(Declaracion(t[2], None, t[1], tp))])

    global min_lst_repga
    repg_inst = 'decla_epsi : tipo mdecla corche  PUNTOCOMA'
    repga_sema = '''t[0]= ListaInstruccion([(Declaracion(t[2], None, t[1], tp,t[3]))])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_declaracion_arra_no_Pob(t):
    'decla_epsi : tipo mdecla corchelle pob_val PUNTOCOMA'
    global entrada
    tp = find_column(entrada, t.slice[5])
    t[0]= ListaInstruccion([(Declaracion(t[2], None, t[1], tp,t[3],t[4]))])

    global min_lst_repga
    repg_inst = 'decla_epsi : tipo mdecla corche  PUNTOCOMA'
    repga_sema = '''t[0]= ListaInstruccion([(Declaracion(t[2], None, t[1], tp,t[3]))])'''
    min_lst_repga.append((repg_inst, repga_sema))


def p_val_arreglo_posible_valor(t):
    'pob_val : IGUAL LLAA val_arri LLAC'
    t[0]=t[3]

def p_val_arreglo_posible_valor_solitario(t):
    'pob_val : IGUAL expresiones'
    t[0]=[t[2]]

def p_val_arreglo_posible_valor_epsilon(t):
    'pob_val : '
    t[0] = None

def p_val_arreglo_posible_valor_dos_dimensiones(t):
    'pob_val : IGUAL LLAA val_two LLAC'
    t[0]=t[3]

def p_val_arreglo_posible_valor_dos_dimensiones_recursivo(t):
    'val_two :  val_two COMA LLAA val_arri LLAC '
    t[0]=t[1]
    t[0].append(t[4])

def p_val_arreglo_posible_valor_dos_dimensiones_epsi(t):
    'val_two :  LLAA val_arri LLAC '
    t[0]=[t[2]]

def p_val_arreglo_mucho(t):
    'val_arri : val_arri COMA expresiones'
    t[0]=t[1]
    t[0].append(t[3])

def p_val_arreglo_epsilon(t):
    'val_arri : expresiones'
    t[0]=[t[1]]


def p_instruccion_mucha_declaracion_algo(t):
    'masinde : masinde COMA mdecla IGUAL expresiones   '
    global entrada
    tp = find_column(entrada, t.slice[2])
    t[0]=t[1]
    t[0].agregar(Declaracion(t[3],t[5],None,tp))

    global min_lst_repga
    repg_inst = 'masinde : masinde COMA mdecla IGUAL expresiones   '
    repga_sema = '''t[0].agregar(Declaracion(t[3],t[5],None,tp))'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_mucha_declaracion_epsilon(t):
    'masinde : '
    t[0] = ListaInstruccion([])

    global min_lst_repga
    repg_inst = 'masinde : '
    repga_sema = '''t[0] = ListaInstruccion([])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_instruccion_igualaciones(t):
    '''m_igual : IGUAL
            | MASIGUAL
            | MENOSIGUAL
            | PORIGUAL
            | DIVIGUAL
            | MODIGUAL
            | SHIFTIIGUAL
            | SHIFTDIGUAL
            | ANDIGUAL
            | XORIGUAL
            | ORIGUAL'''
    t[0] = t[1]

    global min_lst_repga
    repg_inst = 'm_igual : IGUAL'
    repga_sema = '''t[0] = t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_muchas_declaraciones_variables(t):
    'mdecla : mdecla COMA IDENTIFICADOR'
    t[0] = t[1]
    t[0].append(t[3])

    global min_lst_repga
    repg_inst = 'mdecla : mdecla COMA IDENTIFICADOR'
    repga_sema = '''t[0] = t[1]
    t[0].append(t[3])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_muchas_declaraciones_variables_ini(t):
    'mdecla : IDENTIFICADOR'
    t[0] = [t[1]]

    global min_lst_repga
    repg_inst = 'mdecla : IDENTIFICADOR'
    repga_sema = '''t[0] = [t[1]]'''
    min_lst_repga.append((repg_inst, repga_sema))


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

    global min_lst_repga
    repg_inst = 'expresiones : expresiones OR expresiones'
    repga_sema = '''t[0] = NodoBinario(t[1], t[2], t[3], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_ternario(t):
    'expresiones : expresiones INTERROGACION expresiones DOBLEPUNTO expresiones'
    global entrada
    tp = find_column(entrada, t.slice[2])
    t[0] = Ternario(t[1],t[3],t[5],tp)

    global min_lst_repga
    repg_inst = 'expresiones : expresiones INTERROGACION expresiones DOBLEPUNTO expresiones'
    repga_sema = '''t[0] = Ternario(t[1],t[3],t[5],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_expresiones_unarias(t):
    '''expresiones : MENOS expresiones %prec UMENOS
                    | MAS expresiones %prec UMAS
                    | NOTB expresiones
                    | ANDB expresiones %prec UAND
                    | NOT expresiones '''

    global entrada
    tp = find_column(entrada, t.slice[1])

    t[0] = NodoUnario(t[1], t[2], tp)

    global min_lst_repga
    repg_inst = 'expresiones : MENOS expresiones %prec UMENOS'
    repga_sema = '''t[0] = NodoUnario(t[1], t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_expresiones_sola(t):
    'expresiones : valor'
    t[0] = t[1]

    global min_lst_repga
    repg_inst = 'expresiones : valor'
    repga_sema = '''t[0] = t[1]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_expresiones_parentesis(t):
    'expresiones : PARA expresiones PARC'
    t[0] = t[2]

    global min_lst_repga
    repg_inst = 'expresiones : PARA expresiones PARC'
    repga_sema = '''t[0] = t[2]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_entero(t):
    'valor : ENTERO'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Hoja(Temporal(t[1], 0), tp)

    global min_lst_repga
    repg_inst = 'valor : ENTERO'
    repga_sema = '''t[0] = Hoja(Temporal(t[1], 0), tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_decimal(t):
    'valor : DECIMAL'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Hoja(Temporal(t[1], 1), tp)

    global min_lst_repga
    repg_inst = 'valor : DECIMAL'
    repga_sema = '''t[0] = Hoja(Temporal(t[1], 1), tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_cadena(t):
    'valor : CADENA'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Hoja(Temporal(t[1], 2), tp)

    global min_lst_repga
    repg_inst = 'valor : CADENA'
    repga_sema = '''t[0] = Hoja(Temporal(t[1], 2), tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_variable(t):
    'valor : IDENTIFICADOR'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = ValorVariable(t[1], tp)

    global min_lst_repga
    repg_inst = 'valor : IDENTIFICADOR'
    repga_sema = '''t[0] = ValorVariable(t[1], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_mucho_corchete_lleno(t):
    'corchelle : corchelle CORA expresiones CORC'
    t[0]=t[1]
    t[0].append(t[3])

    global min_lst_repga
    repg_inst = 'corchelle : corchelle CORA expresiones CORC'
    repga_sema = '''tt[0]=t[1]
    t[0].append(t[3])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_mucho_corchete_lleno_siempre(t):
    'corchelle : CORA expresiones CORC'
    t[0]=[t[2]]

    global min_lst_repga
    repg_inst = 'corchelle : CORA expresiones CORC'
    repga_sema = '''t[0]=[t[2]]'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_variable_arreglo(t):
    'valor : IDENTIFICADOR corchelle'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = ValorVariable(t[1], tp,t[2])

    global min_lst_repga
    repg_inst = 'valor : IDENTIFICADOR corchelle'
    repga_sema = '''t[0] = ValorVariable(t[1], tp,t[2])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_variable_inc(t):
    'expresiones : IDENTIFICADOR MASDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1],t[2], tp)

    global min_lst_repga
    repg_inst = 'expresiones : IDENTIFICADOR MASDOBLE'
    repga_sema = '''t[0] = Variaciones(t[1],t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_variable_dec(t):
    'expresiones : IDENTIFICADOR MENOSDOBLE'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Variaciones(t[1],t[2], tp )

    global min_lst_repga
    repg_inst = 'expresiones : IDENTIFICADOR MENOSDOBLE'
    repga_sema = '''t[0] = Variaciones(t[1],t[2], tp )'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_struct_llamado(t):
    'valor : IDENTIFICADOR  PUNTO IDENTIFICADOR'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = ValorStruct(t[1],t[3], tp)

    global min_lst_repga
    repg_inst = 'valor : IDENTIFICADOR  PUNTO IDENTIFICADOR'
    repga_sema = '''t[0] = ValorStruct(t[1],t[3], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_variable_arreglo_struct(t):
    'valor : IDENTIFICADOR corchelle PUNTO IDENTIFICADOR'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = ValorStruct(t[1],t[4], tp,t[2])

    global min_lst_repga
    repg_inst = 'valor : IDENTIFICADOR corchelle PUNTO IDENTIFICADOR'
    repga_sema = '''t[0] = ValorStruct(t[1],t[4], tp,t[2])'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_cast_int(t):
    'valor : CASTINT expresiones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Cast(t[1],t[2],tp)

    global min_lst_repga
    repg_inst = 'valor : CASTINT expresiones'
    repga_sema = '''t[0] = Cast(t[1],t[2],tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_cast_char(t):
    'valor : CASTCHAR expresiones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Cast(t[1], t[2], tp)

    global min_lst_repga
    repg_inst = 'valor : CASTCHAR expresiones'
    repga_sema = '''t[0] = Cast(t[1], t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_cast_Float(t):
    'valor : CASTFLOAT expresiones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Cast(t[1], t[2], tp)

    global min_lst_repga
    repg_inst = 'valor : CASTFLOAT expresiones'
    repga_sema = '''t[0] = Cast(t[1], t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_cast_double(t):
    'valor : CASTDOUBLE expresiones'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = Cast(t[1], t[2], tp)

    global min_lst_repga
    repg_inst = 'valor : CASTDOUBLE expresiones'
    repga_sema = '''t[0] = Cast(t[1], t[2], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_fuseizeof_expre(t):
    'valor : SIZEOF PARA expresiones PARC'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncSizeof(t[3],tp)

    global min_lst_repga
    repg_inst = 'valor : SCANF PARA exepresiones PARC'
    repga_sema = '''t[0] = FuncSizeOf(tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_fusizeof_tipo(t):
    'valor : SIZEOF PARA tipo PARC'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncSizeof(None,tp,t[3])

    global min_lst_repga
    repg_inst = 'valor : SCANF PARA exepresiones PARC'
    repga_sema = '''t[0] = FuncSizeOf(tp)'''
    min_lst_repga.append((repg_inst, repga_sema))


def p_valor_scanf(t):
    'valor : SCANF PARA PARC'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = FuncScanF(tp)

    global min_lst_repga
    repg_inst = 'valor : SCANF PARA PARC'
    repga_sema = '''t[0] = FuncScanF(tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_valor_funcion_llamado(t):
    'valor : IDENTIFICADOR PARA listado_parametros PARC'
    global entrada
    tp = find_column(entrada, t.slice[1])
    t[0] = LlamarFuncMetodo(t[1],t[3], tp)

    global min_lst_repga
    repg_inst = 'valor : IDENTIFICADOR PARA listado_parametros PARC'
    repga_sema = '''t[0] = LlamarFuncMetodo(t[1],t[3], tp)'''
    min_lst_repga.append((repg_inst, repga_sema))

def p_error(t):
    from AProyecto2.Contenido.Analizadores.MinorCSintactico import list_er,entrada
    #print(id(list_er))
    if t is None:
        from AProyecto2.Contenido.TablaDeSimbolos import Error
        tp =(0,0)
        list_er.append(Error("Error Analizando","Se llego al fin del archivo",1,tp))
    else:
        tp = find_column(entrada, t)
        #print("Error sintáctico en '%s'" % t)
        from AProyecto2.Contenido.TablaDeSimbolos import Error
        list_er.append(Error("Error Analizando","No se esperaba el token "+str(t.value),1,tp))

def find_column(input, token):
    if token is None:
        return (0, 0)
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return ((token.lexpos - line_start) + 1, token.lineno)

list_er = []
entrada = ""
min_lst_repga =[]
def analizar_ascendente(input: str,lst_reporte_gramatical :[],lerror):
    # Construyendo el analizador léxico
    global list_er
    list_er=lerror.lst_errores
    #print(str(id(list_er))+"---")
    global entrada,min_lst_repga
    entrada = input
    lexer = lex.lex()
    parsito = yacc.yacc()
    min_lst_repga=lst_reporte_gramatical
    return parsito.parse(input)
