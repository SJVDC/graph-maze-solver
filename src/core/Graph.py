class Grafo : 
    def __init__( self ) : 
        self.lista_adyacencia = {}

    def agregar_nodo( self, nodo ) :
        if nodo not in self.lista_adyacencia :
            self.lista_adyacencia[ nodo ] = []

    def agregar_arista( self, origen, destino, peso = 1 ) :
        self.agregar_nodo( origen )
        self.agregar_nodo( destino )

        if ( destino, peso ) not in self.lista_adyacencia[ origen ] :
            self.lista_adyacencia[ origen ].append( ( destino, peso ) ) 
        if ( origen, peso ) not in self.lista_adyacencia[ destino ] : 
            self.lista_adyacencia[ destino ].append( ( origen, peso ) )

    def obtener_vecinos( self, nodo ) :
        return self.lista_adyacencia.get( nodo, [] )

    def __repr__( self ) : 
        return f"Grafo con {len(self.lista_adyacencia)} nodos."