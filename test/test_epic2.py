import os 
import sys
sys.path.append( os.path.abspath( os.path.join( os.path.dirname( __file__ ), ".." ) ) )
from src.io.LeerLaberinto import procesar_laberinto
from src.core.converter import matriz_a_grafo

def probar_conversion_grafo( ruta_txt ) : 
    if not os.path.exists( ruta_txt ) : 
        print(f"Error: El archivo '{ruta_txt}' no fue encontrado.")
        return

    matriz, filas, cols, inicio, meta = procesar_laberinto( ruta_txt )

    grafo = matriz_a_grafo( matriz )

    print(f"\n--- Prueba Épica 2: {ruta_txt} ---")
    print(f"Total de nodos transitables construidos: {len(grafo.lista_adyacencia)}")
    print(f"Vecinos del nodo de Salida {inicio}: {grafo.obtener_vecinos(inicio)}")
    print(f"Vecinos del nodo de Meta {meta}: {grafo.obtener_vecinos(meta)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta_archivo = sys.argv[1]
    else:
        ruta_archivo = input("Ingrese la ruta del archivo .txt a probar: ").strip()

    probar_conversion_grafo( ruta_archivo )