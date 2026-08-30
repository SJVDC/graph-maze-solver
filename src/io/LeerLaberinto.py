def procesar_laberinto( ruta_archivo ) :
    matriz = []

    with open( ruta_archivo, 'r', encoding = 'utf-8' ) as ruta :
        #Recorre el archivo linea por linea
        for linea in ruta :
            #elimina espacios en blanco, tab, \n
            linea = linea.strip()
            #si la linea queda vacia va a la siguiente
            if not linea : continue

            #Se salta la primera linea
            if linea.startswith( '(' ) and linea.endswith( ')' ) : continue

            linea_limpia = linea.replace( '[', ' ' ).replace( ']', ' ' ).replace( ',', ' ' ).replace( '(', ' ' ).replace( ')', ' ' )
            celdas = linea_limpia.split()

            if celdas:
                fila = []
                for celda in celdas:
                    fila.append(int(celda))
    
                matriz.append(fila)

    if not matriz : return matriz, 0, 0, None, None

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