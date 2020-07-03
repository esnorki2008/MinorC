import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
import re
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
import ascendente as g
import AnalizadorDescendente.descendente as d
import ast.Entorno as TS
import ast.Instruccion as Instruccion
import ast.GoTo as GoTo
import ast.Declaracion as Declaracion
import Primitivas.Exit as Exit
import Condicionales.If as If
import ast.AST as AST
import Reporteria.Error as Error
import Reporteria.ReporteErrores as ReporteErrores
import Reporteria.ReporteTablaSimbolos as ReporteTablaSimbolos
import Reporteria.ReporteAST as ReporteAST
import ValorImplicito.Asignacion as Asignacion
import ValorImplicito.Conversion as Conversion
import Reporteria.ReporteGramatical as ReporteGramatical


class Ui_MainWindow(object):

    resultChanged = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 30, 900, 450))
        self.tabWidget.setObjectName("tabWidget")
        #=========================================AGREGAR TABS===============
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")

        self.tab_reporte = QtWidgets.QWidget()
        self.tab_reporte.setObjectName("tab_reporte")
        self.tabWidget.addTab(self.tab_reporte, "Reportes De Minor C")
        #==========================================AGREGAR COSAS A LAS TABS=====
        self.tabWidget_textos_augus = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_textos_augus.setGeometry(QtCore.QRect(0, 30, 450, 400))
        self.tabWidget_textos_augus.setObjectName("tabWidget_textos_augus")

        self.tab_augus_optimo = QtWidgets.QWidget()
        self.tab_augus_optimo.setObjectName("tab_augus_optimo")
        self.tabWidget_textos_augus.addTab(self.tab_augus_optimo, "Augus Optimizado")

        self.tab_augus_normal = QtWidgets.QWidget()
        self.tab_augus_normal.setObjectName("tab_augus_normal")
        self.tabWidget_textos_augus.addTab(self.tab_augus_normal, "Augus Sin Optimizar")
        #============================================Editor=====================
        


        self.tabWidget_reportes_minor_c = QtWidgets.QTabWidget(self.tab_reporte)
        self.tabWidget_reportes_minor_c.setGeometry(QtCore.QRect(5, 30, 880, 380))
        self.tabWidget_reportes_minor_c.setObjectName("tabWidget_reportes_minor_c_genera")

        
        #==========================================Agregar Tabs AL TAB==================
        #============================================TAB DEL ARBOL=================
        self.tab_minor_reporte_arbol = QtWidgets.QWidget()
        self.tab_minor_reporte_arbol.setObjectName("tab_minor_reporte_arbol")
        self.tabWidget_reportes_minor_c.addTab(self.tab_minor_reporte_arbol, "Reporte Arbol")

        self.frame_reporte_grafico =QtWidgets.QScrollArea(self.tab_minor_reporte_arbol)
        self.frame_reporte_grafico.setGeometry(QtCore.QRect(5, 30, 870, 330))
        self.frame_reporte_grafico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_reporte_grafico.setWidgetResizable(True)
        self.frame_reporte_grafico.setObjectName("frame_reporte_grafico")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 868, 329))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.frame_reporte_grafico.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.lbl_graphviz = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.lbl_graphviz.setMaximumSize(QtCore.QSize(16777215, 16777215))
        #self.lbl_graphviz.setMinimumSize(QtCore.QSize(5000,500))
        self.lbl_graphviz.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_graphviz.setText("")
        self.lbl_graphviz.setScaledContents(False)
        self.lbl_graphviz.setObjectName("lbl_graphviz")
        self.verticalLayout_2.addWidget(self.lbl_graphviz)
        
        #=======================================TAB DE REPORTE GRAMATICAL======================
        self.tab_minor_reporte_gramatical = QtWidgets.QWidget()
        self.tab_minor_reporte_gramatical.setObjectName("tab_minor_reporte_gramatical")
        self.tabWidget_reportes_minor_c.addTab(self.tab_minor_reporte_gramatical, "Reporte Gramatical")

        self.frame_reporte_gramatical =QtWidgets.QScrollArea(self.tab_minor_reporte_gramatical)
        self.frame_reporte_gramatical.setGeometry(QtCore.QRect(5, 30, 870, 330))
        self.frame_reporte_gramatical.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_reporte_gramatical.setWidgetResizable(True)
        self.frame_reporte_gramatical.setObjectName("frame_reporte_gramatical")

        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 868, 329))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.frame_reporte_gramatical.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.lbl_reporte_gramatical = QtWidgets.QLabel(self.scrollAreaWidgetContents_5)
        self.lbl_reporte_gramatical.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_reporte_gramatical.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_reporte_gramatical.setText("")
        self.lbl_reporte_gramatical.setScaledContents(False)
        self.lbl_reporte_gramatical.setObjectName("lbl_reporte_gramatical")
        self.verticalLayout_5.addWidget(self.lbl_reporte_gramatical)
        
        #=======================================TAB DE ERRORES======================
        self.tab_minor_reporte_errores = QtWidgets.QWidget()
        self.tab_minor_reporte_errores.setObjectName("tab_minor_reporte_errores")
        self.tabWidget_reportes_minor_c.addTab(self.tab_minor_reporte_errores, "Reporte Errores")

        self.frame_reporte_errores =QtWidgets.QScrollArea(self.tab_minor_reporte_errores)
        self.frame_reporte_errores.setGeometry(QtCore.QRect(5, 30, 870, 330))
        self.frame_reporte_errores.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_reporte_errores.setWidgetResizable(True)
        self.frame_reporte_errores.setObjectName("frame_reporte_errores")

        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 868, 329))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.frame_reporte_errores.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        
        self.lbl_reporte_errores = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.lbl_reporte_errores.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_reporte_errores.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_reporte_errores.setText("")
        self.lbl_reporte_errores.setScaledContents(False)
        self.lbl_reporte_errores.setObjectName("lbl_reporte_errores")
        self.verticalLayout_6.addWidget(self.lbl_reporte_errores)
        #=======================================TAB DE TABLA DE SIMBOLO======================
        self.tab_minor_reporte_tabla = QtWidgets.QWidget()
        self.tab_minor_reporte_tabla.setObjectName("tab_minor_reporte_tabla")
        self.tabWidget_reportes_minor_c.addTab(self.tab_minor_reporte_tabla, "Reporte Tabla De Simbolos")

        self.frame_reporte_tabla =QtWidgets.QScrollArea(self.tab_minor_reporte_tabla)
        self.frame_reporte_tabla.setGeometry(QtCore.QRect(5, 30, 870, 330))
        self.frame_reporte_tabla.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_reporte_tabla.setWidgetResizable(True)
        self.frame_reporte_tabla.setObjectName("frame_reporte_tabla")

        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 868, 329))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.frame_reporte_tabla.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        
        self.lbl_reporte_tabla = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.lbl_reporte_tabla.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_reporte_tabla.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_reporte_tabla.setText("")
        self.lbl_reporte_tabla.setScaledContents(False)
        self.lbl_reporte_tabla.setObjectName("lbl_reporte_tabla")
        self.verticalLayout_7.addWidget(self.lbl_reporte_tabla)
        #============================================Reporte Optimizacion==================
        self.tab_minor_reporte_optimizacion = QtWidgets.QWidget()
        self.tab_minor_reporte_optimizacion.setObjectName("tab_minor_reporte_optimizacion")
        self.tabWidget_reportes_minor_c.addTab(self.tab_minor_reporte_optimizacion, "Reporte De Optimizacion")

        self.frame_reporte_optimizacion =QtWidgets.QScrollArea(self.tab_minor_reporte_optimizacion)
        self.frame_reporte_optimizacion.setGeometry(QtCore.QRect(5, 30, 870, 330))
        self.frame_reporte_optimizacion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_reporte_optimizacion.setWidgetResizable(True)
        self.frame_reporte_optimizacion.setObjectName("frame_reporte_optimizacion")

        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 868, 329))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.frame_reporte_optimizacion.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        
        self.lbl_reporte_optimizacion = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.lbl_reporte_optimizacion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_reporte_optimizacion.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_reporte_optimizacion.setText("")
        self.lbl_reporte_optimizacion.setScaledContents(False)
        self.lbl_reporte_optimizacion.setObjectName("lbl_reporte_tabla")
        self.verticalLayout_8.addWidget(self.lbl_reporte_optimizacion)
        #============================================Reporte Metodos==================
        self.tab_minor_reporte_metodos = QtWidgets.QWidget()
        self.tab_minor_reporte_metodos.setObjectName("tab_minor_reporte_metodos")
        self.tabWidget_reportes_minor_c.addTab(self.tab_minor_reporte_metodos, "Reporte De Metodos")

        self.frame_reporte_metodos =QtWidgets.QScrollArea(self.tab_minor_reporte_metodos)
        self.frame_reporte_metodos.setGeometry(QtCore.QRect(5, 30, 870, 330))
        self.frame_reporte_metodos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_reporte_metodos.setWidgetResizable(True)
        self.frame_reporte_metodos.setObjectName("frame_reporte_metodos")

        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 868, 329))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.frame_reporte_metodos.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        
        self.lbl_reporte_metodos = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.lbl_reporte_metodos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lbl_reporte_metodos.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_reporte_metodos.setText("")
        self.lbl_reporte_metodos.setScaledContents(False)
        self.lbl_reporte_metodos.setObjectName("lbl_reporte_tabla")
        self.verticalLayout_9.addWidget(self.lbl_reporte_metodos)
        #============================================FIN DE TAB
        self.frameCodigo = QtWidgets.QFrame(self.tab_augus_optimo)
        self.frameCodigo.setGeometry(QtCore.QRect(0, 30, 430, 350))
        self.frameCodigo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCodigo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCodigo.setObjectName("frameCodigo")
        
        
        self.frameCodigo_normal = QtWidgets.QFrame(self.tab_augus_normal)
        self.frameCodigo_normal.setGeometry(QtCore.QRect(0, 30, 430, 350))
        self.frameCodigo_normal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCodigo_normal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCodigo_normal.setObjectName("frameCodigo_normal")

        self.frameCodigo_minor = QtWidgets.QFrame(self.tab)
        self.frameCodigo_minor.setGeometry(QtCore.QRect(450, 40, 450, 392))
        self.frameCodigo_minor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCodigo_minor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCodigo_minor.setObjectName("frameCodigo_minor")

        self.scrollDebug = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollDebug.setGeometry(QtCore.QRect(900, 30, 280, 471))
        self.scrollDebug.setWidgetResizable(False)
        self.scrollDebug.setObjectName("scrollDebug")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 339, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 341, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.scrollDebug.setWidget(self.scrollAreaWidgetContents)


        

        self.frameConsola = QtWidgets.QFrame(self.centralwidget)
        self.frameConsola.setGeometry(QtCore.QRect(0, 500, 1180, 160))
        self.frameConsola.setAutoFillBackground(True)
        self.frameConsola.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameConsola.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameConsola.setObjectName("frameConsola")
        
        
        
        self.consola = QtWidgets.QPlainTextEdit(self.frameConsola)
        self.consola.setGeometry(QtCore.QRect(10, 0, 1180, 160))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)


        font2 = QtGui.QFont()
        font2.setFamily("Consolas")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(100)
        font2.setKerning(True)


        self.consola.setFont(font2)
        self.consola.setAutoFillBackground(False)
        #self.consola.setTextFormat(QtCore.Qt.RichText)
        self.consola.setObjectName("consola")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 1001, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1011, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuPrograma = QtWidgets.QMenu(self.menubar)
        self.menuPrograma.setObjectName("menuPrograma")
        self.menuReportes = QtWidgets.QMenu(self.menubar)
        self.menuReportes.setObjectName("menuReportes")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionArbir = QtWidgets.QAction(MainWindow)
        self.actionArbir.setObjectName("actionArbir")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionCerrrar = QtWidgets.QAction(MainWindow)
        self.actionCerrrar.setObjectName("actionCerrrar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCopiar = QtWidgets.QAction(MainWindow)
        self.actionCopiar.setObjectName("actionCopiar")
        self.actionPegar = QtWidgets.QAction(MainWindow)
        self.actionPegar.setObjectName("actionPegar")
        self.actionCortar = QtWidgets.QAction(MainWindow)
        self.actionCortar.setObjectName("actionCortar")
        self.actionBuscar = QtWidgets.QAction(MainWindow)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionReemplazar = QtWidgets.QAction(MainWindow)
        self.actionReemplazar.setObjectName("actionReemplazar")
        self.actionEjecutar_Descendente = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_Descendente.setObjectName("actionEjecutar_Descendente")
        self.actionEjecutar_minor = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_minor.setObjectName("actionEjecutar_minor")
        self.actionEjecutar_minor_debug = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_minor_debug.setObjectName("actionEjecutar_minor_debug")
        self.actionEjecutar_minor_normal = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_minor_normal.setObjectName("actionEjecutar_minor_normal")
        self.actionEjecutar_minor_debug_normal = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_minor_debug_normal.setObjectName("actionEjecutar_minor_debug_normal")
        self.actionEjecutar_Ascendente = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_Ascendente.setObjectName("actionEjecutar_Ascendente")
        self.actionEjecutar_Paso_a_Paso_Ascendente = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_Paso_a_Paso_Ascendente.setObjectName("actionEjecutar_Paso_a_Paso_Ascendente")
        self.actionTabla_de_Simbolos = QtWidgets.QAction(MainWindow)
        self.actionTabla_de_Simbolos.setObjectName("actionTabla_de_Simbolos")
        self.actionErrores = QtWidgets.QAction(MainWindow)
        self.actionErrores.setObjectName("actionErrores")
        self.actionAST = QtWidgets.QAction(MainWindow)
        self.actionAST.setObjectName("actionAST")
        self.actionGramatical = QtWidgets.QAction(MainWindow)
        self.actionGramatical.setObjectName("actionGramatical")

        self.actionreportes_minor_c_gramatical = QtWidgets.QAction(MainWindow)
        self.actionreportes_minor_c_gramatical.setObjectName("reportes_minor_c_gramatical")
        self.actionreportes_minor_c_reglas_usadas = QtWidgets.QAction(MainWindow)
        self.actionreportes_minor_c_reglas_usadas.setObjectName("reportes_minor_c_reglas_usadas")
        self.actionreportes_minor_c_errores = QtWidgets.QAction(MainWindow)
        self.actionreportes_minor_c_errores.setObjectName("reportes_minor_c_errores")
        self.actionreportes_minor_c_graphviz = QtWidgets.QAction(MainWindow)
        self.actionreportes_minor_c_graphviz.setObjectName("reportes_minor_c_graphviz")
        self.actionreportes_tabla_de_simbolos = QtWidgets.QAction(MainWindow)
        self.actionreportes_tabla_de_simbolos.setObjectName("reportes_tabla_de_simbolos")
        self.actionreportes_minor_c_reporte_metodos = QtWidgets.QAction(MainWindow)
        self.actionreportes_minor_c_reporte_metodos.setObjectName("reportes_minor_c_reporte_metodos")
        

        self.actionAyuda = QtWidgets.QAction(MainWindow)
        self.actionAyuda.setObjectName("actionAyuda")
        self.actionAcercaDe = QtWidgets.QAction(MainWindow)
        self.actionAcercaDe.setObjectName("actionAcercaDe")

        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionArbir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionCerrrar)
        self.menuArchivo.addAction(self.actionSalir)
        self.menuPrograma.addAction(self.actionEjecutar_minor)
        self.menuPrograma.addAction(self.actionEjecutar_minor_debug)
        self.menuPrograma.addSeparator()
        self.menuPrograma.addAction(self.actionEjecutar_minor_normal)
        self.menuPrograma.addAction(self.actionEjecutar_minor_debug_normal)
        self.menuPrograma.addSeparator()
        self.menuPrograma.addAction(self.actionEjecutar_Descendente)
        self.menuPrograma.addSeparator()
        self.menuPrograma.addAction(self.actionEjecutar_Ascendente)
        self.menuPrograma.addAction(self.actionEjecutar_Paso_a_Paso_Ascendente)

        
        self.menuReportes.addAction(self.actionreportes_minor_c_gramatical)
        self.menuReportes.addAction(self.actionreportes_minor_c_reglas_usadas)
        self.menuReportes.addAction(self.actionreportes_minor_c_errores)
        self.menuReportes.addAction(self.actionreportes_minor_c_graphviz)
        self.menuReportes.addAction(self.actionreportes_tabla_de_simbolos)
        self.menuReportes.addAction(self.actionreportes_minor_c_reporte_metodos)
        self.menuReportes.addSeparator()

        self.menuReportes.addAction(self.actionTabla_de_Simbolos)
        self.menuReportes.addAction(self.actionErrores)
        self.menuReportes.addAction(self.actionAST)
        self.menuReportes.addAction(self.actionGramatical)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcercaDe)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuPrograma.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())


        self.__myFont = QFont()
        self.__myFont.setPointSize(12)
        self.editor_augus()
        self.editor_augus_normal()
        self.editor_minor()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionNuevo.triggered.connect(self.clean)
        self.actionArbir.triggered.connect(self.open)
        self.actionGuardar.triggered.connect(self.save)
        self.actionGuardar_Como.triggered.connect(self.save_as)
        self.actionCerrrar.triggered.connect(self.clear)
        self.actionSalir.triggered.connect(self.exit)
        self.ruta_archivo  = None
        self.actionEjecutar_minor_debug_normal.triggered.connect(self.ejecutar_minor_debug_normal)
        self.actionEjecutar_minor_normal.triggered.connect(self.ejecutar_minor_normal)
        self.actionEjecutar_minor_debug.triggered.connect(self.ejecutar_minor_debug)
        self.actionEjecutar_minor.triggered.connect(self.ejecutar_minor)
        self.actionEjecutar_Ascendente.triggered.connect(self.ascendente)
        self.actionEjecutar_Descendente.triggered.connect(self.descendente)
        self.actionTabla_de_Simbolos.triggered.connect(self.generarTabla)
        self.actionErrores.triggered.connect(self.generarRErrores)
        self.actionGramatical.triggered.connect(self.generarRGramatical)
        self.actionAST.triggered.connect(self.generarAST)
        
        self.actionreportes_minor_c_gramatical.triggered.connect(self.reportes_minor_c_gramatical)
        self.actionreportes_minor_c_reglas_usadas.triggered.connect(self.reportes_minor_c_reglas_usadas)
        self.actionreportes_minor_c_errores.triggered.connect(self.reportes_minor_c_errores)
        self.actionreportes_minor_c_graphviz.triggered.connect(self.reportes_minor_c_graphviz)
        self.actionreportes_tabla_de_simbolos.triggered.connect(self.reportes_tabla_de_simbolos)
        self.actionreportes_minor_c_reporte_metodos.triggered.connect(self.reportes_minor_c_reporte_metodos)
        

        self.actionAcercaDe.triggered.connect(self.acercade)
        self.actionAyuda.triggered.connect(self.ayuda)

        self.ts_global = TS.Entorno(None)
        self.ast =  AST.AST([]) 
        self.listado_gramatical = []
        self.instrucciones = []
        self.hilo_terminado = True
        self.actionEjecutar_Paso_a_Paso_Ascendente.triggered.connect(self.debugger)


        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setItem(0,0, QTableWidgetItem("No."))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Simbolo"))
        self.tableWidget.setItem(0, 2 , QTableWidgetItem("Valor"))

        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 75)
        self.tableWidget.setColumnWidth(2, 175)

        self.consola.setStyleSheet("background-color: black;border: 1px solid black;color:green;") 
        #self.consola.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
    from AProyecto2.Main import Proyecto2
    mi_proyecto2 = Proyecto2()
    def reportes_minor_c_graphviz(self):
        import pydot
        dot_string = self.mi_proyecto2.graphviz_arbol()
        graphs = pydot.graph_from_dot_data(dot_string)
        from PyQt5.QtWidgets import QApplication
        from PyQt5.QtGui import QPixmap
        qp = QPixmap()
        qp.loadFromData(graphs[0].create_png())
        self.lbl_graphviz.resize(qp.size())
        self.lbl_graphviz.setPixmap(qp)

    
    def reportes_minor_c_reporte_metodos(self):
        entrada = self.mi_proyecto2.reporte_metodos_declarados()
        self.lbl_reporte_metodos.setText(entrada)

    def reportes_minor_c_reglas_usadas(self):
        entrada = self.mi_proyecto2.reporte_reglas_utilizadas()
        self.lbl_reporte_optimizacion.setText(entrada)

    def reportes_tabla_de_simbolos(self):
        entrada=self.mi_proyecto2.reporte_tabla_variables()
        self.lbl_reporte_tabla.setText(entrada)

    def reportes_minor_c_gramatical(self):
        entrada=self.mi_proyecto2.reporte_gramatical()
        self.lbl_reporte_gramatical.setText(entrada)

    def reportes_minor_c_errores(self):
        entrada=self.mi_proyecto2.reporte_errores()
        self.lbl_reporte_errores.setText(entrada)

    def limpiar_reportes_minor_c(self):
        self.lbl_reporte_errores.clear()
        self.lbl_reporte_gramatical.clear()
        self.lbl_reporte_tabla.clear()
        self.lbl_graphviz.clear()
        self.lbl_reporte_optimizacion.clear()

    def ejecutar_minor(self):
        entrada=self.editor_minor.text()
        self.editor.setText(self.mi_proyecto2.analizar_minor_c_optimizar_3D(entrada))
       
        self.editor_normal.setText(self.mi_proyecto2.analizar_minor_c(entrada))
        
        self.limpiar_reportes_minor_c()

        #self.reportes_minor_c_gramatical()
        #self.reportes_minor_c_reglas_usadas()
        #self.reportes_minor_c_errores()
        #self.reportes_minor_c_graphviz()
        #self.reportes_tabla_de_simbolos()
        #self.reportes_minor_c_reporte_metodos()
        self.ascendente()
    
    def ejecutar_minor_normal(self):
        entrada=self.editor_minor.text()
        self.editor.setText(self.mi_proyecto2.analizar_minor_c(entrada))
       
        self.editor_normal.setText(self.mi_proyecto2.analizar_minor_c(entrada))
        
        self.limpiar_reportes_minor_c()
        self.ascendente()
        

    def ejecutar_minor_debug(self):
        entrada=self.editor_minor.text()
        self.limpiar_reportes_minor_c()
        self.editor.setText(self.mi_proyecto2.analizar_minor_c_optimizar_3D(entrada))
        self.editor_normal.setText(self.mi_proyecto2.analizar_minor_c(entrada))
        self.debugger()

    def ejecutar_minor_debug_normal(self):
        entrada=self.editor_minor.text()
        self.limpiar_reportes_minor_c()
        self.editor.setText(self.mi_proyecto2.analizar_minor_c(entrada))
        self.editor_normal.setText(self.mi_proyecto2.analizar_minor_c(entrada))
        self.debugger()

        
    def clean(self):
        self.ruta_archivo = None
        self.editor.setText("")
        self.consola.clear()

    def acercade(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("AUGUS IDE\nPrimer Proyecto Compiladores 2 Vacaciones Junio\nElaborado por: Haroldo Arias\nCarnet: 201020247 \n Segundo Proyecto \n Andhy Solis \n 201700886")
        msg.setInformativeText("Python 3.8.3\nPLY\nPyQT\nScintilla")
        msg.setWindowTitle("Acerca de")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def ayuda(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("AUGUS IDE")
        msg.setInformativeText("Puedes encontrar el manual de este proyecto en:\nhttps://tinyurl.com/yabg9why")
        msg.setWindowTitle("Ayuda")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def setTexto(self,texto):
        self.consola.setText(self.consola.text() + texto)

    def generarAST(self):
        reporteAST = ReporteAST.ReporteAST()
        reporteAST.graficar(self.instrucciones)

    def generarTabla(self):
        reporteTablas = ReporteTablaSimbolos.ReporteTablaSimbolos()
        reporteTablas.generarReporte(self.ts_global,self.ast)

    def generarRErrores(self):
        reporteErrores = ReporteErrores.ReporteErrores()
        reporteErrores.generarReporte()

    def generarRGramatical(self):
        listado = self.listado_gramatical 
        reporteGramatical = ReporteGramatical.ReporteGramatical()
        reporteGramatical.generarReporte(listado[0])

    def debugger(self):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setItem(0,0, QTableWidgetItem("No."))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Simbolo"))
        self.tableWidget.setItem(0, 2 , QTableWidgetItem("Valor"))



        if(self.hilo_terminado):
            sys.setrecursionlimit(2147483644)
            self.consola.clear()
            ReporteErrores.func(None,True)
            g.func(0,None)
            g.textoEntrada = self.editor.text()
            instrucciones = g.parse(self.editor.text())
            self.instrucciones = instrucciones
            ts_global = TS.Entorno(None)
            ast = AST.AST(instrucciones) 

            declaracion1 = Declaracion.Declaracion('$ra',0,0,0,"","GLOBAL")
            declaracion2 = Declaracion.Declaracion('$sp',0,0,0,"","GLOBAL")
            declaracion1.ejecutar(ts_global,ast,self,True)
            declaracion2.ejecutar(ts_global,ast,self,True)

            bandera = False
            if(instrucciones != None):
                for ins in instrucciones:
                    try:
                        if(bandera == False and ins.id != "main"):
                            error = Error.Error("SEMANTICO","Error semantico, La primera etiqueta debe ser la etiqueta main:",ins.linea,ins.columna)
                            ReporteErrores.func(error)
                            break
                        else:
                            bandera = True
                        if(ast.existeEtiqueta(ins)):
                            error = Error.Error("SEMANTICO","Error semantico, Ya existe la etiqueta "+ins.id,ins.linea,ins.columna)
                            ReporteErrores.func(error)
                        else:
                            ast.agregarEtiqueta(ins)
                    except:
                            pass
            self.ts_global = ts_global
            self.ast = ast
            self.listado_gramatical = g.func(1,None).copy()

            self.debug()

    def descendente(self):
        sys.setrecursionlimit(2147483644)
        self.consola.clear()
        d.textoEntrada = self.editor.text()
        d.band(1,False)
        ReporteErrores.func(None,True)
        d.func(0,None)
        instrucciones = d.parse(self.editor.text())
        self.instrucciones = instrucciones
        ts_global = TS.Entorno(None)
        ts_global.asignarConsola(self.consola)
        ast = AST.AST(instrucciones) 

        declaracion1 = Declaracion.Declaracion('$ra',0,0,0,"","GLOBAL")
        declaracion2 = Declaracion.Declaracion('$sp',0,0,0,"","GLOBAL")
        declaracion1.ejecutar(ts_global,ast,self,False)
        declaracion2.ejecutar(ts_global,ast,self,False)


        #PRIMERA PASADA PARA GUARDAR TODAS LAS ETIQUETAS
        bandera = False
        if(instrucciones != None):
            for ins in instrucciones:
                try:
                    if(bandera == False and ins.id != "main"):
                        error = Error.Error("SEMANTICO","Error semantico, La primera etiqueta debe ser la etiqueta main:",ins.linea,ins.columna)
                        ReporteErrores.func(error)
                        break
                    else:
                        bandera = True
                    if(ast.existeEtiqueta(ins)):
                        error = Error.Error("SEMANTICO","Error semantico, Ya existe la etiqueta "+ins.id,ins.linea,ins.columna)
                        ReporteErrores.func(error)
                    else:
                        ast.agregarEtiqueta(ins)
                except:
                        pass

        main = ast.obtenerEtiqueta("main")

        if(main != None):
            salir = False
            for ins in main.instrucciones:
                try:
                    if(isinstance(ins,Asignacion.Asignacion) or isinstance(ins,Conversion.Conversion)):
                        ins.setAmbito("main")

                    if(ins.ejecutar(ts_global,ast,self,False) == True):
                        salir = True
                        break
                except:
                    pass
            if(not salir):   
                siguiente = ast.obtenerSiguienteEtiqueta("main")
                if(siguiente!=None):
                    siguiente.ejecutar(ts_global,ast,self,False)
        else:
            error = Error.Error("SEMANTICO","Error semantico, No puede iniciarse el programa ya que no existe la etiqueta main:",0,0)
            ReporteErrores.func(error)

        listado = ReporteErrores.func(None)
        if(len(listado)>0):
            QMessageBox.critical(self.centralwidget, "Errores en Ejecución", "Se obtuvieron errores en la ejecución del Código Ingresado, verifique reporte de Errores")

        self.ts_global = ts_global
        self.ast = ast
        self.listado_gramatical = d.func(1,None).copy()

    def ascendente(self):
        sys.setrecursionlimit(2147483644)
        self.consola.clear()
        ReporteErrores.func(None,True)
        g.textoEntrada = self.editor.text()
        g.func(0,None)
        instrucciones = g.parse(self.editor.text())
        self.instrucciones = instrucciones
        ts_global = TS.Entorno(None)
        ts_global.asignarConsola(self.consola)
        ast = AST.AST(instrucciones) 

        declaracion1 = Declaracion.Declaracion('$ra',0,0,0,"","GLOBAL")
        declaracion2 = Declaracion.Declaracion('$sp',0,0,0,"","GLOBAL")
        declaracion1.ejecutar(ts_global,ast,self,False)
        declaracion2.ejecutar(ts_global,ast,self,False)


        #PRIMERA PASADA PARA GUARDAR TODAS LAS ETIQUETAS
        bandera = False
        if(instrucciones != None):
            for ins in instrucciones:
                try:
                    if(bandera == False and ins.id != "main"):
                        error = Error.Error("SEMANTICO","Error semantico, La primera etiqueta debe ser la etiqueta main:",ins.linea,ins.columna)
                        ReporteErrores.func(error)
                        break
                    else:
                        bandera = True
                    if(ast.existeEtiqueta(ins)):
                        error = Error.Error("SEMANTICO","Error semantico, Ya existe la etiqueta "+ins.id,ins.linea,ins.columna)
                        ReporteErrores.func(error)
                    else:
                        ast.agregarEtiqueta(ins)
                except:
                        pass

        main = ast.obtenerEtiqueta("main")

        if(main != None):
            salir = False
            for ins in main.instrucciones:
                try:
                    if(isinstance(ins,Asignacion.Asignacion) or isinstance(ins,Conversion.Conversion)):
                        ins.setAmbito("main")

                    if(ins.ejecutar(ts_global,ast,self,False) == True):
                        salir = True
                        break
                except:
                    pass
            if(not salir):   
                siguiente = ast.obtenerSiguienteEtiqueta("main")
                if(siguiente!=None):
                    siguiente.ejecutar(ts_global,ast,self,False)
        else:
            error = Error.Error("SEMANTICO","Error semantico, No puede iniciarse el programa ya que no existe la etiqueta main:",0,0)
            ReporteErrores.func(error)

        listado = ReporteErrores.func(None)
        if(len(listado)>0):
            QMessageBox.critical(self.centralwidget, "Errores en Ejecución", "Se obtuvieron errores en la ejecución del Código Ingresado, verifique reporte de Errores")

        self.ts_global = ts_global
        self.ast = ast
        self.listado_gramatical = g.func(1,None).copy()

    def debug(self):
        self.hilo_terminado = False
        main = self.ast.obtenerEtiqueta("main")

        if(main != None):
            salir = False
            self.editor.setCursorPosition(0,0)
            self.editor.setFocus()
            time.sleep(2)
            for ins in main.instrucciones:
                QApplication.processEvents()
                try:
                    self.editor.setCursorPosition(ins.linea-1,0)
                    self.editor.setFocus()
                    time.sleep(2)
                    if(isinstance(ins,Asignacion.Asignacion) or isinstance(ins,Conversion.Conversion)):
                        ins.setAmbito("main")
                    if(ins.ejecutar(self.ts_global,self.ast,self,True) == True):
                        salir = True
                        break
                    
                    contador = 1
                    self.tableWidget.setRowCount(0)
                    self.tableWidget.setRowCount(100)
                    self.tableWidget.setItem(0,0, QTableWidgetItem("No."))
                    self.tableWidget.setItem(0,1, QTableWidgetItem("Simbolo"))
                    self.tableWidget.setItem(0, 2 , QTableWidgetItem("Valor"))
                    for key in self.ts_global.tabla:
                        s = self.ts_global.tabla[key]
                        self.tableWidget.setItem(contador,0, QTableWidgetItem(str(contador)))
                        self.tableWidget.setItem(contador,1, QTableWidgetItem(s.id))
                        self.tableWidget.setItem(contador, 2 , QTableWidgetItem(str(s.valor)))
                        contador = contador + 1 
                    
                    
                except:
                    pass
            
            if(not salir):   
                siguiente = self.ast.obtenerSiguienteEtiqueta("main")
                if(siguiente!=None):
                    siguiente.ejecutar(self.ts_global,self.ast,self,True)
        else:
            error = Error.Error("SEMANTICO","Error semantico, No puede iniciarse el programa ya que no existe la etiqueta main:",0,0)
            ReporteErrores.func(error)
        listado = ReporteErrores.func(None)
        if(len(listado)>0):
            QMessageBox.critical(self.centralwidget, "Errores en Ejecución", "Se obtuvieron errores en la ejecución del Código Ingresado, verifique reporte de Errores")
        self.hilo_terminado = True
        #print ("Terminado hilo ")

    def exit(self):
        sys.exit()

    def clear(self):
        self.ruta_archivo = None
        self.editor.setText("")

    def open(self):
        root = tk.Tk()
        root.withdraw()
        ruta = filedialog.askopenfilename(title="Seleccione un archivo de Entrada")
        if not ruta: return
        try:
            f = open(ruta,"r")
            input = f.read()
            self.editor_minor.setText(input)
            f.close()
            self.ruta_archivo = ruta
        except Exception as e:
            raise
            QMessageBox.critical(self.centralwidget,'Error Cargando el Archivo', 'No es posible abrir el archivo: %r' % ruta)

    def save(self):
        if(self.ruta_archivo==None):
            root = tk.Tk()
            root.withdraw()
            ruta = filedialog.asksaveasfilename(title="Seleccione la ruta donde desea guardar el Archivo",filetypes=[('all files', '.*'), ('text files', '.txt')])
        else:
            ruta = self.ruta_archivo
        if not ruta: return
        try:
            f = open(ruta,"w")
            f.write(self.editor.text())
            f.close()
        except Exception as e:
            raise
            QMessageBox.critical(self.centralwidget,'Error Guardando el Archivo', 'No es posible guardar el archivo: %r' % ruta)

    def save_as(self):
        ruta = filedialog.asksaveasfilename(title="Seleccione la ruta donde desea guardar el Archivo",filetypes=[('all files', '.*'), ('text files', '.txt')])
        if not ruta: return
        try:
            f = open(ruta,"w")
            f.write(self.editor.text())
            f.close()
            self.ruta_archivo = ruta
        except Exception as e:
            raise
            QMessageBox.critical(self.centralwidget,'Error Guardando el Archivo', 'No es posible guardar el archivo: %r' % ruta)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IDE AUGUS - HAROLDO PABLO ARIAS MOLINA - 201020247 ----MINOR C -ANDHY LIZANDRO SOLIS OSORIO - 201700886"))
        #self.consola.setText(_translate("MainWindow", ""))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuPrograma.setTitle(_translate("MainWindow", "Programa"))
        self.menuReportes.setTitle(_translate("MainWindow", "Reportes"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionArbir.setText(_translate("MainWindow", "Abrir"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como"))
        self.actionCerrrar.setText(_translate("MainWindow", "Cerrrar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))

        self.actionEjecutar_minor_debug.setText(_translate("MainWindow", "Ejecutar MinorC-Augus_PASO A PASO"))
        self.actionEjecutar_minor.setText(_translate("MainWindow", "Ejecutar MinorC-Augus"))
        self.actionEjecutar_Descendente.setText(_translate("MainWindow", "Ejecutar Descendente"))
        self.actionEjecutar_Ascendente.setText(_translate("MainWindow", "Ejecutar Ascendente"))
        self.actionEjecutar_Paso_a_Paso_Ascendente.setText(_translate("MainWindow", "Ejecutar Paso a Paso Ascendente"))
        self.actionTabla_de_Simbolos.setText(_translate("MainWindow", "Tabla de Simbolos"))
        self.actionErrores.setText(_translate("MainWindow", "Errores"))
        self.actionAST.setText(_translate("MainWindow", "AST"))
        self.actionGramatical.setText(_translate("MainWindow", "Gramatical"))

        self.actionEjecutar_minor_normal.setText(_translate("MainWindow", "Ejecutar MinorC_Sin Optimizacion"))
        self.actionEjecutar_minor_debug_normal.setText(_translate("MainWindow", "Ejecutar MinorC-Augus_PASO A PASO Sin Optimizacion"))
        
        self.actionreportes_minor_c_gramatical.setText(_translate("MainWindow", "MinorC Reporte Gramatical"))
        self.actionreportes_minor_c_reglas_usadas.setText(_translate("MainWindow", "MinorC Reporte Optimizacion"))
        self.actionreportes_minor_c_errores.setText(_translate("MainWindow", "MinorC Reporte Errores"))
        self.actionreportes_minor_c_graphviz.setText(_translate("MainWindow", "MinorC Reporte Graphviz"))
        self.actionreportes_tabla_de_simbolos.setText(_translate("MainWindow", "MinorC Reporte Tabla De Simbolos"))
        self.actionreportes_minor_c_reporte_metodos.setText(_translate("MainWindow", "MinorC Reporte Reporte De Metodos"))
        
        self.actionAyuda.setText(_translate("MainWindow", "Ayuda"))
        self.actionAcercaDe.setText(_translate("MainWindow", "Acerca de"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Archivo Entrada"))

    def editor_augus(self):
         #************************************************ REGLAS DEL LENGUAJE AUGUS *****************************************
        self.editor = QsciScintilla()
        self.editor.setText("")              
        self.editor.setLexer(None)           
        self.editor.setUtf8(True)             
        self.editor.setFont(self.__myFont)    

        #AJUSTES DE TEXTO
        self.editor.setWrapMode(QsciScintilla.WrapWord)
        self.editor.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.editor.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        #FIN DE LINEA
        self.editor.setEolMode(QsciScintilla.EolWindows)
        self.editor.setEolVisibility(False)

        #SANGRIA
        self.editor.setIndentationsUseTabs(False)
        self.editor.setTabWidth(4)
        self.editor.setIndentationGuides(True)
        self.editor.setTabIndents(True)
        self.editor.setAutoIndent(True)

        self.editor.setCaretForegroundColor(QColor("#ff0000ff"))
        self.editor.setCaretLineVisible(True)
        self.editor.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.editor.setCaretWidth(2)

        # MARGENES
        self.editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.editor.setMarginWidth(0, "0000")  #con este se puede quitar la linea
        self.editor.setMarginsForegroundColor(QColor("#ff888888"))

        #SE COLOCAN LAS REGLAS DEL EDITOR
        self.__lexer = QsciLexerRuby(self.editor)
        self.editor.setLexer(self.__lexer)

        self.__lyt = QVBoxLayout()
        self.frameCodigo.setLayout(self.__lyt)
        self.__lyt.addWidget(self.editor)
    def editor_augus_normal(self):
         #************************************************ REGLAS DEL LENGUAJE AUGUS *****************************************
        self.editor_normal = QsciScintilla()
        self.editor_normal.setText("")              
        self.editor_normal.setLexer(None)           
        self.editor_normal.setUtf8(True)             
        self.editor_normal.setFont(self.__myFont)    

        #AJUSTES DE TEXTO
        self.editor_normal.setWrapMode(QsciScintilla.WrapWord)
        self.editor_normal.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.editor_normal.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        #FIN DE LINEA
        self.editor_normal.setEolMode(QsciScintilla.EolWindows)
        self.editor_normal.setEolVisibility(False)

        #SANGRIA
        self.editor_normal.setIndentationsUseTabs(False)
        self.editor_normal.setTabWidth(4)
        self.editor_normal.setIndentationGuides(True)
        self.editor_normal.setTabIndents(True)
        self.editor_normal.setAutoIndent(True)

        self.editor_normal.setCaretForegroundColor(QColor("#ff0000ff"))
        self.editor_normal.setCaretLineVisible(True)
        self.editor_normal.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.editor_normal.setCaretWidth(2)

        # MARGENES
        self.editor_normal.setMarginType(0, QsciScintilla.NumberMargin)
        self.editor_normal.setMarginWidth(0, "0000")  #con este se puede quitar la linea
        self.editor_normal.setMarginsForegroundColor(QColor("#ff888888"))

        #SE COLOCAN LAS REGLAS DEL editor_normal
        self.editor_normal.setLexer(QsciLexerRuby(self.editor_normal))

        self.__lyt1 = QVBoxLayout()
        self.frameCodigo_normal.setLayout(self.__lyt1)
        self.__lyt1.addWidget(self.editor_normal)

    def editor_minor(self):
         #************************************************ REGLAS DEL LENGUAJE AUGUS *****************************************
        self.editor_minor = QsciScintilla()
        self.editor_minor.setText("")              
        self.editor_minor.setLexer(None)           
        self.editor_minor.setUtf8(True)             
        self.editor_minor.setFont(self.__myFont)    

        #AJUSTES DE TEXTO
        self.editor_minor.setWrapMode(QsciScintilla.WrapWord)
        self.editor_minor.setWrapVisualFlags(QsciScintilla.WrapFlagByText)
        self.editor_minor.setWrapIndentMode(QsciScintilla.WrapIndentIndented)

        #FIN DE LINEA
        self.editor_minor.setEolMode(QsciScintilla.EolWindows)
        self.editor_minor.setEolVisibility(False)

        #SANGRIA
        self.editor_minor.setIndentationsUseTabs(False)
        self.editor_minor.setTabWidth(4)
        self.editor_minor.setIndentationGuides(True)
        self.editor_minor.setTabIndents(True)
        self.editor_minor.setAutoIndent(True)

        self.editor_minor.setCaretForegroundColor(QColor("#ff0000ff"))
        self.editor_minor.setCaretLineVisible(True)
        self.editor_minor.setCaretLineBackgroundColor(QColor("#1f0000ff"))
        self.editor_minor.setCaretWidth(2)

        # MARGENES
        self.editor_minor.setMarginType(0, QsciScintilla.NumberMargin)
        self.editor_minor.setMarginWidth(0, "0000")  #con este se puede quitar la linea
        self.editor_minor.setMarginsForegroundColor(QColor("#ff888888"))

        #SE COLOCAN LAS REGLAS DEL editor_minor
        self.editor_minor.setLexer(QsciLexerCPP(self.editor_minor))

        self.__lyt2 = QVBoxLayout()
        self.frameCodigo_minor.setLayout(self.__lyt2)
        self.__lyt2.addWidget(self.editor_minor)

interfaz = None

def getUI():
    global interfaz
    return interfaz.consola

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(10**9)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(MainWindow.windowFlags() | QtCore.Qt.CustomizeWindowHint)
    MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    interfaz = ui
    MainWindow.show()
    sys.exit(app.exec_())


