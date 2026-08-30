def procesar_laberinto( ruta_archivo ) :
    matriz = []

    with open( ruta_archivo, 'r', encoding = 'utf-8' ) as ruta :
        for linea in ruta :
            linea = linea.strip()
            if not linea :
                continue

            if linea.startswith( '(' ) and linea.endswith( ')' ) :
                continue

            linea_limpia = linea.replace( '[', ' ' ).replace( ']', ' ' ).replace( ',', ' ' ).replace( '(', ' ' ).replace( ')', ' ' )
            celdas = linea_limpia.split()

            if celdas :
                fila = [ int( celda ) for celda in celdas ]
                matriz.append( fila )

    if not matriz :
        return matriz, 0, 0, None, None

    num_filas = len( matriz )
    num_cols = len( matriz[ 0 ] )
    inicio = None
    meta = None

    for i in range( num_filas ) :
        for j in range( num_cols ) :
            valor = matriz[ i ][ j ]
            if valor == 2:
                inicio = ( i, j )
            elif valor == 3:
                meta = ( i, j )

    return matriz, num_filas, num_cols, inicio, meta