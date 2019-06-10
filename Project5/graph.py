from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []
        self.visited = False


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        self.list_of_vertices = []

        fp = open(filename)
        line = fp.readlines()
        for item in line:
            item = item.strip("\n")
            item = item.split(" ")
            v1 = item[0]
            v2 = item[1]
            self.add_vertex(v1)
            self.add_vertex(v2)
            self.add_edge(v1, v2)
        fp.close()

    def add_vertex(self, key):
        '''Add vertex to graph, only if the vertex is not already in the graph.'''
        for item in self.list_of_vertices:
            if key is item.id:
                return

        vertex = Vertex(key)
        self.list_of_vertices.append(vertex)

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        for item in self.list_of_vertices:
            if item.id is key:
                return item

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        one = self.get_vertex(v1)
        two = self.get_vertex(v2)
        one.adjacent_to.append(two)
        two.adjacent_to.append(one)


    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        loo = []
        for item in self.list_of_vertices:
            if item.id not in loo:
                loo += [item.id]
        return sorted(loo)

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        ans = []
        stack = Stack(20)
        verts = self.get_vertices()
        for item in verts:
            object = self.get_vertex(item)
            stack.push(object)
            while stack.is_empty() is False:
                v = stack.pop()
                if v.visited is False:
                    v.visited = True
                    if v.id not in ans:
                        ans.append(v.id)
                    for i in v.adjacent_to:
                        stack.push(i)
        return ans

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        ans = []
        queue = Queue(20)
        verts = self.get_vertices()
        for item in verts:
            object = self.get_vertex(item)
            queue.push(object)
            while queue.is_empty() is False:
                v = queue.pop()
                if v.visited is False:
                    v.visited = True
                    if v.id not in ans:
                        ans.append(v.id)
                    for i in v.adjacent_to:
                        queue.push(i)
        return ans

