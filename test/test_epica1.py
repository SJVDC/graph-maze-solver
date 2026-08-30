import sys
import os
sys.path.append( os.path.abspath( os.path.join( os.path.dirname( __file__ ), ".." ) ) )
from src.io.LeerLaberinto import procesar_laberinto

def probar_epica_1( ruta_txt ) :
    if not os.path.exists( ruta_txt ) : 
        print( f"ERROR, el archivo '{ruta_txt}' no fue encontrado" )
        return

    try : 
        matriz, filas, cols, inicio, meta = procesar_laberinto( ruta_txt )

        print(f"\n--- Prueba Exitosa para: {ruta_txt} ---")
        print(f"Dimensiones: {filas} x {cols}")
        print(f"Salida (2): {inicio}")
        print(f"Meta (3): {meta}")
    except Exception as e :
        print(f"Error al procesar el archivo '{ruta_txt}': {e}")

def test_laberinto_estructura() :
    ruta_archivo = os.path.join( os.path.dirname( os.path.dirname( __file__ ) ), "data", "laberinto.txt" )
    matriz, filas, cols, inicio, meta = procesar_laberinto( ruta_archivo )

    assert filas == 34
    assert cols == 34
    assert inicio == ( 0, 0 )
    assert meta == ( 17, 17 )
    assert len( matriz ) == 34
    assert all( len( fila ) == 34 for fila in matriz )

if __name__ == "__main__" :
    if len( sys.argv ) > 1 : ruta_archivo = sys.argv[ 1 ]
    else : ruta_archivo = input( "Ingrese la ruta del archivo .txt: " ).strip()
probar_epica_1( ruta_archivo )
