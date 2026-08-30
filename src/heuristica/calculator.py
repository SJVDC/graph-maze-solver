def distancia_manhattan( nodo_actual, nodo_meta ) : 
    return abs( nodo_actual[ 0 ] - nodo_meta[ 0 ] ) + abs( nodo_actual[ 1 ] - nodo_meta[ 1 ] ) 

def generador_tabla_heuristica( grafo, nodo_meta ) : 
    lista_heuristica = {}
    for nodo in grafo.lista_adyacencia :
        lista_heuristica[ nodo ] = distancia_manhattan( nodo, nodo_meta )

    return lista_heuristica