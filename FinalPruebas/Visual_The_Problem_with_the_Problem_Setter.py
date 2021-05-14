from sys import stdin, stdout
import VisualGraph

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


    
firstLine=stdin.readline().split()
while firstLine != ["0","0"]:
    #firstLine[0] es el numero de categorias firstLine[1] es el numero de problemas
    nCat=int(firstLine[0])
    nPro=int(firstLine[1])
    n=nCat+nPro+2 # El grafo va a tener tantos nodos como categorais + problemas + 2 nodos que serian el s y el t para el Ford Fulkerson
    s=0    #Primer nodo
    t=n-1  #Ultimo nodo
    graph=[[0] * n for i in range(n)]  # Los primeros nCat numeros van a pertenecer a 

    # La segunda linea contiene nCat numeros que hacen referencia a cuantos problemas pueden ser incluidos en la categoria de la posicion i
    secondLine=stdin.readline().split() 
    
    # Seteo las aristas que van desde la categoria a t para definir la cantidad de problemas que pueden tener.
    for x in range(1,nCat+1):
        graph[x][t]=int(secondLine[x-1])
    
    # Seteo las aristas que van desde s hacia el nodo "problema".
    for x in range(1,nPro+1):
        graph[s][x+nCat]=1

    # Las siguientes nPro lineas contienen en primer lugar la cantidad de categorias a las que puede pertenecer y luego esa misma cantidad de numeros que hacen referencia a la categoria
    for iProblem in range(nPro):
        iProblem= nCat+iProblem+1 # La posicion va a ser la siguiente a la de las categorias.
        prob_cat=stdin.readline().split() 
        
        for x in range(int(prob_cat[0])):
            categoria=int(prob_cat[x+1])
            graph[iProblem][categoria]=1
    

   
    cantidadMaxima=0
    for cat in secondLine:
        cantidadMaxima+=int(cat)

    VisualGraph.adyacenciaAGrafo(graph,nCat,nPro,prefijoPrimerGrupo="C-",prefijoSegundoGrupo="P-")

    g = Graph(graph)

    if (g.EdmondsKarp(s, t) == cantidadMaxima):
        stdout.write("1\n")
        for x in range(1,nCat+1):
            aux=""
            for iProblem in range(nCat+1,n-1):
                if (g.graph[x][iProblem] == 1):
                    aux+=str(iProblem-nCat)+" "
            stdout.write(aux+"\n")
    else:
        stdout.write("0\n")


   
    firstLine=stdin.readline().split()
