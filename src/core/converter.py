from src.core.Graph import Grafo

def matriz_a_grafo( matriz ) :
    num_filas = len( matriz )
    if num_filas > 0 : 
        num_cols = len( matriz[ 0 ] )
    else : 
        num_cols = 0
    grafo = Grafo()

    #movimientos permitidos, en 2D
    movimientos = [ ( -1, 0 ), ( 1, 0 ), ( 0, -1 ), ( 0, 1 ) ]

    for fila in range( num_filas ) :
        for col in range( num_cols ) :
            valor_actual = matriz[ fila ][ col ]

            #solo procesar cada celda valida
            if valor_actual != 1 : 
                nodo_actual = ( fila, col )
                grafo.agregar_nodo( nodo_actual )
                for df, dc in movimientos : 
                    nueva_fila, nueva_col = fila +df, col + dc

                    if ( 0 <= nueva_fila < num_filas and 0 <= nueva_col < num_cols ) :
                        valor_vecino = matriz[ nueva_fila ][ nueva_col ]

                        if ( valor_vecino != 1 ) : 
                            nodo_vecino = ( nueva_fila, nueva_col )
                            grafo.agregar_arista( nodo_actual, nodo_vecino, peso = 1 )

    return grafo