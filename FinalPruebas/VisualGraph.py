from copy import deepcopy
import pydot, os
from datetime import datetime

class FordFulkersonAlgorithm:
    def __init__(self,s,d,g):
        self.src = []
        self.src.append(s)
        self.src.append(0)
        self.src.append(0)
        self.dest = d
        self.augPaths = []
        self.augPathsGraph = []
        self.graph = g
        self.createGraph()


    def createGraph(self, graph = None,augPath=None,flag=0):
        self.G = pydot.Dot(graph_name="ford", graph_type="digraph",rankdir="LR",nodesep=0.5, pad=.1)
        if graph == None and augPath == None:
            for k in self.graph:
                node = pydot.Node(k,fontname="Bold",style="filled", fillcolor="green")
                self.G.add_node(node)
            for k, j in  self.graph.items():
                for e in range (1,len(j)):
                    st = str(j[e][2])+'/' + str(j[e][1])
                    edge = pydot.Edge(k, j[e][0],label=st,fontname="Bold",arrowhead='vee')
                    self.G.add_edge(edge)
            self.augPathsGraph.append(self.G)
        elif augPath == None:
            G = pydot.Dot(graph_name="ford", graph_type="digraph",rankdir="LR",nodesep=.5, pad=.1)
            for k in graph:
                node = pydot.Node(k,fontname="Bold",style="filled", fillcolor="green")
                G.add_node(node)
            for k, j in  graph.items():
                for e in range (1,len(j)):
                    st = str(j[e][2])+'/' + str(j[e][1])
                    edge = pydot.Edge(k, j[e][0],label=st,fontname="Bold",arrowhead='vee')
                    G.add_edge(edge)
#             im = Image(G.create_png())
#             display(im)
            if flag != 0:
                self.augPathsGraph.append(G)
        else:
            G = pydot.Dot(graph_name="ford", graph_type="digraph",rankdir="LR",nodesep=.5, pad=.1)
            for k in graph:
                node = pydot.Node(k,fontname="Bold",style="filled", fillcolor="green")
                G.add_node(node)
            temp = []
            for k, j in  graph.items():
                for e in range (1,len(j)):
                    st = str(j[e][2])+'/' + str(j[e][1])
                    edge = pydot.Edge(k, j[e][0],label=st,fontname="Bold",arrowhead='vee')
                    G.add_edge(edge)
            for  i in range(len(augPath)-1):
                value = self.graph[augPath[i][0]]
                for j in range(1,len(value)):
                    if value[j][0] == augPath[i+1][0]:
                        temp.append(str(value[j][2])+'/'+str(value[j][1]))
            for i in range(len(augPath)-1):
                G.del_edge(augPath[i][0],augPath[i+1][0])
                edge = pydot.Edge(augPath[i][0],augPath[i+1][0],label=temp[i],\
                                  fontname="Bold",arrowhead='vee',color='red')
                G.add_edge(edge)
            self.augPathsGraph.append(G)

    def showGraph(self, graph=None):
        if graph == None:
            im = Image(self.G.create_png())
            display(im)
        else:
            self.createGraph(graph)

    def checkPath(self,path, graph3,mini):
        i = 0
        src = path[i][0]
        dest = path[-1][0]
        while src != dest:
            for n in range(1, len(graph3[src])):
                if graph3[src][n][0] == path[i+1][0]:
                    if graph3[src][n][2]+mini > graph3[src][n][1] or \
                    graph3[src][n][2] == graph3[src][n][1] : #n = node
                        return False
                    break
            i+=1
            src = path[i][0]
        return True

    def updateWeigth(self,s , d, mi):
        for i in range(1, len(self.graph[s])):
            if self.graph[s][i][0] == d:
                self.graph[s][i][2] += mi
                return 0

    def augumentedPaths(self, src, dest, graph, path=[]):
        graph[src[0]][0] = True
        path.append(src)
        src = src[0]
        if src == dest:
            temp = deepcopy(path)
            self.augPaths.append(temp)
        else:
            for i in range(1, len(graph[src])):
                if graph[graph[src][i][0]][0] == False:
                    self.augumentedPaths(graph[src][i], dest, graph , path)
        path.pop()
        graph[src][0] = False

    def maximumFlow(self):
        self.augumentedPaths(self.src, self.dest, self.graph)
        maxFlow = 0
        for p in self.augPaths:
            mini = []
            for j in range(1, len(p)):
                mini.append(p[j][1])
            mini = min(mini)
            if self.checkPath(p, self.graph, mini):
                maxFlow += mini
                for j in range(len(p)-1):
                    self.updateWeigth(p[j][0] , p[j+1][0],mini)
                self.createGraph(self.graph, p)
        self.createGraph(self.graph,None,1)
        return maxFlow



pref1Group=""
pref2Group=""
nombres1Group=[]
nombres2Group=[]
n1Group=0
n=0
def cambiarNombre(name):
    if(name==0):
        return "s"
    elif (name<=n1Group):
        if(len(nombres1Group)>0):
            return nombres1Group[name-1]
        return pref1Group+str(name)
    elif (name<=n-2):
        if(len(nombres2Group)>0):
            return nombres2Group[name-n1Group]
        return pref2Group+str(name-n1Group)
    else:
        return "t"

def adyacenciaAGrafo(graph,nPrimerGrupo,nSegundoGrupo,nombresPrimerGrupo=[],nombresSegundoGrupo=[],prefijoPrimerGrupo="",prefijoSegundoGrupo=""):
    grafo={}
    global n1Group,pref1Group,pref2Group,nombres1Group,nombres2Group,n
    pref1Group=prefijoPrimerGrupo
    pref2Group=prefijoSegundoGrupo
    nombres1Group=nombresPrimerGrupo
    nombres2Group=nombresSegundoGrupo
    n1Group=nPrimerGrupo
    n=nPrimerGrupo+nSegundoGrupo+2

    for x in range(n):
        # print("Hola-"+str(x)+"->"+cambiarNombre(x))
        grafo[cambiarNombre(x)]=[False]
        for i in range(n):
            if (graph[x][i]!=0):
                grafo[cambiarNombre(x)].append([cambiarNombre(i),graph[x][i],0])
    
    src = 's'
    dest = 't'
    obj = FordFulkersonAlgorithm(src, dest, grafo)
    obj.maximumFlow()

    now= datetime.now()
    today = now.strftime("%d-%m-%Y-%H-%M-%S") + "/"
    # print graphs
    j = 0
    for i in obj.augPathsGraph:
        if not os.path.exists('Graphs/'+today):
            os.makedirs("Graphs/"+today)
        i.write_png('Graphs/'+today+ str(j)+'.png')
        #im = Image(i.create_png())
        j+=1
        #display(im)


def adyacenciaAGrafo2(graph,n,prefijo="",src="s",dest="t"):
    grafo={}

    for x in range(n):
        # print("Hola-"+str(x)+"->"+cambiarNombre(x))
        grafo[str(x)]=[False]
        for i in range(n):
            if (graph[x][i]!=0):
                grafo[str(x)].append([str(i),graph[x][i],0])
    
    obj = FordFulkersonAlgorithm(src, dest, grafo)
    obj.maximumFlow()

    now= datetime.now()
    today = now.strftime("%d-%m-%Y-%H-%M-%S") + "/"
    # print graphs
    j = 0
    for i in obj.augPathsGraph:
        if not os.path.exists('Graphs/'+today):
            os.makedirs("Graphs/"+today)
        i.write_png('Graphs/'+today+ str(j)+'.png')
        #im = Image(i.create_png())
        j+=1
        #display(im)
