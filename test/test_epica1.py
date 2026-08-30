import sys
import os

#esta linea me permite importar carpetas de mi propio proyecto, en este caso "graph-maze-solver"
sys.path.append( os.path.abspath( os.path.join( os.path.dirname( __file__ ), ".." ) ) )

from data.maze_example import LABERINTO_EJEMPLO_10X10
from data.maze_example import LABERINTO_PRUEBA_3X3
from src.io.LeerLaberinto import procesar_laberinto

def probar_epica_1() :
    n, inicio, meta = procesar_laberinto( LABERINTO_EJEMPLO_10X10 )
    print( f"[TEST EPICA 1] N: {n}, Inicio: {inicio}, Meta {meta}")

if __name__ == "__main__" :
    probar_epica_1()