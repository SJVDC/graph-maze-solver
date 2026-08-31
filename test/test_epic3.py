import sys
import os 
sys.path.append( os.path.abspath( os.path.join( os.path.dirname( __file__ ), ".." ) ) )
from src.core.converter import matriz_a_grafo
from src.io.LeerLaberinto import procesar_laberinto
from src.search.busqueda_ciega import busqueda_profundidad, busqueda_anchura

def probar_epica_3( ruta_txt ) : 
    if not os.path.exists( ruta_txt ) : 
        print(f"Error: El archivo '{ruta_txt}' no fue encontrado.")
        return

    # cargar matriz
    matriz, cols, filas, inicio, meta = procesar_laberinto( ruta_txt )
    # convertir a grafo
    grafo = matriz_a_grafo( matriz )
    #BFs
    ruta_bfs = busqueda_anchura( grafo, inicio, meta )
    #DFs
    ruta_dfs = busqueda_profundidad( grafo, inicio, meta )

    print(f"\n--- Prueba Épica 3: {ruta_txt} ---")
    print(f"Punto Inicio: {inicio} -> Punto Meta: {meta}")

    if ruta_bfs:
        print(f"Ruta BFS encontrada (Pasos: {len(ruta_bfs) - 1}):")
        print(ruta_bfs)
    else:
        print("BFS no encontró un camino hacia la meta.")

    if ruta_dfs:
        print(f"\nRuta DFS encontrada (Pasos: {len(ruta_dfs) - 1}):")
        print(ruta_dfs)
    else:
        print("DFS no encontró un camino hacia la meta.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ruta_archivo = sys.argv[1]
    else:
        ruta_archivo = input(
            "Ingrese la ruta del archivo .txt a probar: "
        ).strip()

    probar_epica_3(ruta_archivo)