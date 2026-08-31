import time
from src.search.busqueda_ciega import busqueda_anchura, busqueda_profundidad
from src.search.busqueda_informada import busqueda_a_estrella

def medir_algoritmo(funcion_busqueda, grafo, inicio, meta) : 
    tiempo_inicio = time.perf_counter()
    camino = funcion_busqueda( grafo, inicio, meta ) 
    tiempo_fin = time.perf_counter()

    tiempo_ms = ( tiempo_fin - tiempo_inicio ) * 1000

    if camino : 
        pasos = len( camino )
        exito = True
    else : 
        pasos = 0
        exito = False

    return {
        "tiempo_ms": tiempo_ms,
        "pasos": pasos,
        "camino": camino,
        "exito": exito,
    }

def evaluar_todos( grafo, inicio, meta ) :
    resultados = {
        "BFS": medir_algoritmo(busqueda_anchura, grafo, inicio, meta),
        "DFS": medir_algoritmo(busqueda_profundidad, grafo, inicio, meta),
        "A*": medir_algoritmo(busqueda_a_estrella, grafo, inicio, meta),
    }

    return resultados