def procesar_laberinto( matriz ):
    """
    la matriz debe ser cuadrada
    """
    dimension_n = len( matriz )
    salida = None 
    meta = None 

    for fila in range( dimension_n ) :
        for col in range( dimension_n ) :
            valor = matriz [ fila ] [ col ]

            if ( valor == 2 ) : salida = ( fila, col )
            if ( valor == 3 ) : meta = ( fila, col )

    return dimension_n, salida, meta