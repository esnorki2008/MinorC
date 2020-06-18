from Contenido.Analizadores.MinorCSintactico import analizar_ascendente
from Contenido.TablaDeSimbolos import TablaDeSimbolos

rst=analizar_ascendente("8/2*(2+2)")
rst.ejecutar_3D(TablaDeSimbolos())
