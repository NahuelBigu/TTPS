


public class Main{
    class MaxFlow {
    static int V; // Number of vertices in graph
    int rGraph[][];
    /* Devuelve verdadero si hay una ruta desde la fuente 's' hacia 't' 
    en el gráfico residual. También llena parent[] para almacenar la 
    ruta */
    boolean bfs(int rGraph[][], int s, int t, int parent[])
    {
        // Create a visited array and mark all vertices as
        // not visited
        boolean visited[] = new boolean[V];
        for (int i = 0; i < V; ++i)
            visited[i] = false;
 
        // Create a queue, enqueue source vertex and mark
        // source vertex as visited
        LinkedList<Integer> queue
            = new LinkedList<Integer>();
        queue.add(s);
        visited[s] = true;
        parent[s] = -1;
 
        // Standard BFS Loop
        while (queue.size() != 0) {
            int u = queue.poll();
 
            for (int v = 0; v < V; v++) {
                if (visited[v] == false
                    && rGraph[u][v] > 0) {
                    // If we find a connection to the sink
                    // node, then there is no point in BFS
                    // anymore We just have to set its parent
                    // and can return true
                    queue.add(v);
                    parent[v] = u;
                    visited[v] = true;
                    if (v == t) {
                        return true;
                    }
                    
                }
            }
        }
 
        // We didn't reach sink in BFS starting from source,
        // so return false
        return false;
    }
 
    // Returns tne maximum flow from s to t in the given
    // graph
    int fordFulkerson(int graph[][], int s, int t)
    {
        int u, v;
 
        // Create a residual graph and fill the residual
        // graph with given capacities in the original graph
        // as residual capacities in residual graph
 
        // Residual graph where rGraph[i][j] indicates
        // residual capacity of edge from i to j (if there
        // is an edge. If rGraph[i][j] is 0, then there is
        // not)
        rGraph[][] = new int[V][V];
 
        for (u = 0; u < V; u++)
            for (v = 0; v < V; v++)
                rGraph[u][v] = graph[u][v];
 
        // This array is filled by BFS and to store path
        int parent[] = new int[V];
 
        int max_flow = 0; // There is no flow initially
 
        // Augment the flow while tere is path from source
        // to sink
        while (bfs(rGraph, s, t, parent)) {
            // Find minimum residual capacity of the edhes
            // along the path filled by BFS. Or we can say
            // find the maximum flow through the path found.
            int path_flow = Integer.MAX_VALUE;
            for (v = t; v != s; v = parent[v]) {
                u = parent[v];
                path_flow
                    = Math.min(path_flow, rGraph[u][v]);
            }
 
            // update residual capacities of the edges and
            // reverse edges along the path
            for (v = t; v != s; v = parent[v]) {
                u = parent[v];
                rGraph[u][v] -= path_flow;
                rGraph[v][u] += path_flow;
            }
 
            // Add path flow to overall flow
            max_flow += path_flow;
        }
 
        // Return the overall flow
        return max_flow;
    }
    }

    public static void main(String[] args){
        StringBuilder sb = new StringBuilder();
        while (true){
            int nCat= nextInt();
            int nPro= nextInt();

            if(nCat == 0 && nPro==0){
                break;
            }

            int n=nCat+nPro+2;
            int s=0;
            int t=n-1;
            int [][] grafo= new int[n][n];
            int sumaTotal=0
            for(int i=1;i<=nCat;i++){
                grafo[i][t]=nextInt();
                sumaTotal+=grafo[i][t];
            }

        
            for(int i=nCat+1;i<n-1;i++){
                int catOfProblem= nextInt();
                grafo[s][i]=1; // conecto del source a los problemas
                for(int j=0;j<catOfProblem;j++){
                    int cat= nextInt();
                    graph[i][cat]=1;
                }
            }


            MaxFlow m = new MaxFlow();
            m.V=n;
            if(m.fordFulkerson(grafo,s,t)==sumaTotal){
                sb.append(1).append("\n");
                 for(int i=1;i<=nCat;i++){
                      for(int j=nCat+1;j<n-1;j++){
                          if (m.rGraph[i][j] == 1){
                              sb.append(j-nCat).append(" ");
                          }
                      }
                      sb.append("\n");
                 }
            }else{
                sb.append(0).append("\n");
            }

        }
        System.out.print(sb);
    }

}

