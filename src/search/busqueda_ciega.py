from collections import deque

def busqueda_anchura( grafo, inicio, meta ) : 
    cola = deque( [ [ inicio ] ] )
    visitados = { inicio }

    while cola : 
        camino = cola.popleft()
        nodo_actual = camino[ -1 ]

        if ( nodo_actual == meta ) : return camino

        for vecino, _ in grafo.obtener_vecinos( nodo_actual ) :
            if vecino not in visitados : 
                visitados.add( vecino )
                nuevo_camino = list( camino )
                nuevo_camino.append( vecino )
                cola.append( nuevo_camino )

    return None

def busqueda_profundidad( grafo, inicio, meta ) :
    pila = [ [ inicio ] ]
    visitados = set()

    while pila : 
        camino = pila.pop()
        nodo_actual = camino[ -1 ]

        if (nodo_actual == meta ) : return camino

        if nodo_actual not in visitados : 
            visitados.add( nodo_actual )

            for vecino, _ in grafo.obtener_vecinos( nodo_actual ) :
                if vecino not in visitados : 
                    nuevo_camino = list( camino )
                    nuevo_camino.append( vecino )
                    pila.append( nuevo_camino )

    return None