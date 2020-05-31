import copy
class Node(object):
    def __init__(self, name):
        self.name = name
        self.parent = self
        self.rank = 0
    
    def find(self):
        if self.parent != self:
            self.parent = self.parent.find()
        return self.parent
    
    def merge(self, other):
        root1 = self.find()
        root2 = other.find()
        if root1 == root2:
            return False
        if root1.rank > root2.rank:
            root2.parent = root1
            
        elif root1.rank < root2.rank:
            root1.parent = root2
        else:
            root1.parent = root2
            root2.rank = root2.rank + 1
        return True
    
    
class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.node = Node(name)

class Edge(object):
    
    def __init__(self, weight, startVertex, endVertex):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.weight = weight
        
    def __cmp__(self, other):
        return cmp(self.weight, other.weigh)
    
    def __lt__(self, other):
        return self.weight < other.weight

    
    
    
    
    
class KruskalAlgorythm(object):
    
    def createSpanningTree(self, edgeList):
        edges = copy.deepcopy(edgeList)
        edges.sort()
        output = []
        for edge in edges:
            if edge.startVertex.node.merge(edge.endVertex.node):
                output.append(edge)
        for item in output:
            print(item.startVertex.name, "-", item.endVertex.name, item.weight)
        
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




edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)
edgeList.append(edge10)
edgeList.append(edge11)



ka = KruskalAlgorythm()

def cop(edgeList):
    edges = copy.deepcopy(edgeList)
    
if __name__=='__main__':
    from timeit import Timer
    
    t = Timer("cop(edgeList)", "from __main__ import edgeList, cop")
    t1 = Timer("ka.createSpanningTree(edgeList)", "from __main__ import edgeList, ka")
    print(t.timeit(number=1000))