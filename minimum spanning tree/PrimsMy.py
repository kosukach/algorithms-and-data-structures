import heapq
import copy
class Vertex(object):

    def __init__(self, name):
        self.visited = False
        self.name = name
        self.adjacenciesList = []

class Edge(object):

    def __init__(self, weight, startVertex, endVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.endVertex  = endVertex

    def __lt__(self, other):
        return self.weight < other.weight
    
    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)




"""node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edge(100,node1,node2)

edge3 = Edge(1000,node1,node3)

edge5 = Edge(0.01,node3,node2)


node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge3)
node2.adjacenciesList.append(edge1)
node2.adjacenciesList.append(edge5)
node3.adjacenciesList.append(edge3)
node3.adjacenciesList.append(edge5)"""
vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")
vertex7 = Vertex("g")

edge1 = Edge(2,vertex1,vertex2)
edge2 = Edge(6,vertex1,vertex3)
edge3 = Edge(5,vertex1,vertex5)
edge4 = Edge(10,vertex1,vertex6)
edge5 = Edge(3,vertex2,vertex4)
edge6 = Edge(3,vertex2,vertex5)
edge7 = Edge(1,vertex3,vertex4)
edge8 = Edge(2,vertex3,vertex6)
edge9 = Edge(4,vertex4,vertex5)
edge10 = Edge(5,vertex4,vertex7)
edge11 = Edge(5,vertex6,vertex7)

vertex1.adjacenciesList.append(edge1)
vertex1.adjacenciesList.append(edge2)
vertex1.adjacenciesList.append(edge3)
vertex1.adjacenciesList.append(edge4)
vertex2.adjacenciesList.append(edge1)
vertex2.adjacenciesList.append(edge5)
vertex2.adjacenciesList.append(edge6)
vertex3.adjacenciesList.append(edge1)
vertex3.adjacenciesList.append(edge7)
vertex3.adjacenciesList.append(edge8)
vertex4.adjacenciesList.append(edge5)
vertex4.adjacenciesList.append(edge7)
vertex4.adjacenciesList.append(edge9)
vertex4.adjacenciesList.append(edge10)
vertex5.adjacenciesList.append(edge3)
vertex5.adjacenciesList.append(edge6)
vertex5.adjacenciesList.append(edge9)
vertex6.adjacenciesList.append(edge4)
vertex6.adjacenciesList.append(edge11)
vertex6.adjacenciesList.append(edge8)
vertex7.adjacenciesList.append(edge10)
vertex6.adjacenciesList.append(edge11)


class Prims(object):

    


    def spanningTree(self, startVertex):
        heap = []
        spanningTreeEdges = []
        
        return self.createSpanningTree(heap, copy.deepcopy(startVertex), spanningTreeEdges)

    def createSpanningTree(self, heap, vertex, spanningTreeEdges):

        
        vertex.visited = True
        for edge in vertex.adjacenciesList:
            heapq.heappush(heap, edge)
        
        mindGewicht = heapq.heappop(heap)
        
        while mindGewicht.startVertex.visited and mindGewicht.endVertex.visited:
            mindGewicht = heapq.heappop(heap)
            if not heap:
                return spanningTreeEdges
        
        spanningTreeEdges.append(mindGewicht)
        print( mindGewicht.startVertex.name, "-", mindGewicht.endVertex.name)
        if mindGewicht.startVertex.visited:
            spanningTreeEdges = self.createSpanningTree(heap, mindGewicht.endVertex, spanningTreeEdges)
        else:
            spanningTreeEdges = self.createSpanningTree(heap, mindGewicht.startVertex, spanningTreeEdges)

        return spanningTreeEdges

pp = Prims()

def cop(vertex):
    vertex = copy.deepcopy(vertex)
if __name__=='__main__':
    from timeit import Timer
    
    t = Timer("pp.spanningTree(vertex1)", "from __main__ import pp, vertex1")
    t1 = Timer("cop(vertex1)", "from __main__ import cop, vertex1")
    print(t1.timeit(number=1000))