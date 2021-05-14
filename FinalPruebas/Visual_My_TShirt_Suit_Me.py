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


cases=int( stdin.readline().strip() )
for _ in range(cases):
    firstLine=stdin.readline().split()
    #firstLine[0] es el numero de remeras firstLine[1] es el numero de voluntarios
    nTshirts=int(firstLine[0])
    nVolun=int(firstLine[1])

    
    n=nVolun+6+2 # El grafo va a tener tantos nodos como   los 6 talles(XXL,XL,L,M,S,XS) + voluntarios + 2 nodos que serian el s y el t para el Ford Fulkerson
    s=0    #Primer nodo
    t=n-1  #Ultimo nodo
    graph=[[0] * n for i in range(n)]  # Los primeros nCat numeros van a pertenecer a 


    # Seteo las aristas que van desde los talles a t para definir la cantidad de remeras que pueden tener.
    for x in range(1,7): # 6 talles
        graph[x][t]=nTshirts/6
    
    # Seteo las aristas que van desde s hacia el nodo "problema".
    for x in range(1,nVolun+1):
        graph[s][x+6]=1

    talles= {"XXL":1,"XL":2,"L":3,"M":4,"S":5,"XS":6}
    # Las siguientes nVolun lineas contienen dos talles posibles
    for i in range(1,nVolun+1):
        i= 6+i # La posicion va a ser la siguiente a la de los talles.
        voluntario_talles=stdin.readline().split() 
        graph[i][talles[voluntario_talles[0]]]=1
        graph[i][talles[voluntario_talles[1]]]=1
    
  
    VisualGraph.adyacenciaAGrafo(graph,6,nVolun,nombresPrimerGrupo=list(talles.keys()))
   
    g = Graph(graph)

    # for x in range(n):
    #     print(graph[x])

    if (g.EdmondsKarp(s, t) == nVolun):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
       
    
    # for x in range(n):
    #     print(g.graph[x])

    # if ((max_flow(graph,s, t)) == cantidadMaxima):
    #     print("1")
    #     for x in range(1,nCat+1):
    #         aux=""
    #         for iProblem in range(nCat+1,n-1):
    #             if (F[x][iProblem] == -1):
    #                 aux+=str(iProblem-nCat)+" "
    #         print(aux)
    # else:
    #     print("0")


    # for x in range(len(F)):
    #     print(F[x])
    
    