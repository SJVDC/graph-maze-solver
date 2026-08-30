import heapq
from src.heuristica.calculator import distancia_manhattan

def busqueda_a_estrella(grafo, inicio, meta):
    h_inicio = distancia_manhattan( inicio, meta )
    frontera = [ ( h_inicio, 0, [ inicio ] ) ]
    
    # 1. costos_g es un diccionario
    costos_g = { inicio: 0 }

    while frontera:
        _, costo_g, camino = heapq.heappop( frontera )
        nodo_actual = camino[ -1 ]

        if nodo_actual == meta:
            return camino

        # 2. Verificar el orden del desempaquetado: (vecino, peso)
        for vecino, peso_arista in grafo.obtener_vecinos( nodo_actual ):
            nuevo_costo_g = costo_g + peso_arista

            # 3. Comprobar si el vecino ya tiene un menor costo registrado
            if vecino not in costos_g or nuevo_costo_g < costos_g[ vecino ]:
                # IMPORTANTE: Guardar en la clave del diccionario, no reasignar la variable
                costos_g[ vecino ] = nuevo_costo_g
                
                h_vecino = distancia_manhattan( vecino, meta )
                f_costo = nuevo_costo_g + h_vecino
                
                nuevo_camino = list( camino )
                nuevo_camino.append( vecino )
                heapq.heappush( frontera, ( f_costo, nuevo_costo_g, nuevo_camino ) )

    return None