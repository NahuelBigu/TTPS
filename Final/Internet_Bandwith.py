from sys import stdin, stdout
    
#Esta clase representa un grafo dirigido usando una matriz de adyacencia 
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # grafo residual
        self.ROW = len(graph)
        #self.COL = len(gr[0])
 
    '''Devuelve verdadero si hay una ruta desde la fuente 's' hacia 't' 
    en el gráfico residual. También llena parent[] para almacenar la 
    ruta''' 
    def BFS(self, s, t, parent):
        # Marca todos los vertices como no visitados
        visited = [False]*(self.ROW)
 
        # Crea una cola para el BFS
        queue = []
 
        # Marca el nodo ‘s’ como visitado y lo saca de la cola
        queue.append(s)
        visited[s] = True
 
        # BFS Loop
        while queue:
            # Retirar un vértice de la cola
            u = queue.pop(0)
 
            # Obtiene todos los vértices adyacentes del nodo ‘u’
            # Si el adyacente no fue visitado, se lo marca como visitado
            # y se lo encola
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # Si encontramos una conexión con el nodo ‘t’,
                    # entonces ya no tiene sentido en BFS. Solo hay
                    # que establecer su padre y devolver True
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
                    
 
        # No llegamos a ‘t’ en BFS comenzando desde ‘s’
        # así que devuelve False
        return False
             
     
    # Devuelve el flujo máximo de 's' a 't' en el gráfico dado
    def EdmondsKarp(self, source, sink):
 
        # Este arreglo es llenado por el BFS y para almacenar la ruta
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # No hay flujo inicialmente
 
        # Se va a aumentar el flujo mientras haya un camino desde 
        # ‘s’ hasta ‘t’.
        while self.BFS(source, sink, parent) :

            # Buscamos la capacidad residual mínima de los bordes a 
            # lo largo del camino llenado por el BFS. O podemos 
            # encontrar el flujo máximo a través del camino encontrado.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Agrega el flujo de la ruta al flujo general
            max_flow +=  path_flow
 
            # actualizar las capacidades residuales de los bordes y los 
            # bordes inversos a lo largo del camino
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow


case=0
n=int(stdin.readline().strip())
while n != 0:   
    # La segunda linea contiene s t c . s = nodo source  , t = nodo destination , c = cantidad de aristas
    secondLine=stdin.readline().split() 

    s=int(secondLine[0])-1
    t=int(secondLine[1])-1
    c=int(secondLine[2])
    graph=[[0] * n for i in range(n)] 


    # Las siguientes c lineas contienen en 3 datos cada una , los primeros dos son los nodos y el tercero el peso de la arista.
    for _ in range(c):
        arista=stdin.readline().split() 
        nodo1=int(arista[0])-1
        nodo2=int(arista[1])-1
        peso=int(arista[2])
        # Las aristas son bidireccionales
        graph[nodo1][nodo2]+=peso
        graph[nodo2][nodo1]+=peso
       
    g = Graph(graph)
    case+=1
    stdout.write("Network "+str(case)+"\n")
    stdout.write("The bandwidth is "+str(g.EdmondsKarp(s, t))+".\n")
    stdout.write("\n")
    n=int(stdin.readline().strip())
