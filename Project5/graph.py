from stack_array import * #Needed for Depth First Search
from queue_array import * #Needed for Breadth First Search


class Vertex:
    '''Add additional helper methods if necessary.'''
    def __init__(self, key):
        '''Add other attributes as necessary'''
        self.id = key
        self.adjacent_to = []


class Graph:
    '''Add additional helper methods if necessary.'''
    def __init__(self, filename):
        '''reads in the specification of a graph and creates a graph using an adjacency list representation.  
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is 
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified 
           in the input file should appear on the adjacency list of each vertex of the two vertices associated 
           with the edge.'''
        fp = open(filename)
        line = fp.readlines()
        self.list_of_vertices = []
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
        in_list = False
        for items in self.list_of_vertices:
            if key in items:
                in_list = True
        if in_list is False:
            vertex = Vertex(key)
            self.list_of_vertices.append([vertex.id, vertex.adjacent_to])

    def get_vertex(self, key):
        '''Return the Vertex object associated with the id. If id is not in the graph, return None'''
        for item in self.list_of_vertices:
            if key not in item:
                continue
            elif key not in item and index(key) == len(self.list_of_vertices) - 1:
                return None
            else:
                return item

    def add_edge(self, v1, v2):
        '''v1 and v2 are vertex id's. As this is an undirected graph, add an 
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph'''
        one = self.get_vertex(v1)
        two = self.get_vertex(v2)
        one[1].append(v2)
        two[1].append(v1)


    def get_vertices(self):
        '''Returns a list of id's representing the vertices in the graph, in ascending order'''
        for item in self.list_of_vertices:
            return item[0]

    def conn_components(self): 
        '''Returns a list of lists.  For example, if there are three connected components 
           then you will return a list of three lists.  Each sub list will contain the 
           vertices (in ascending order) in the connected component represented by that list.
           The overall list will also be in ascending order based on the first item of each sublist.
           This method MUST use Depth First Search logic!'''
        pass

    def is_bipartite(self):
        '''Returns True if the graph is bicolorable and False otherwise.
           This method MUST use Breadth First Search logic!'''
        pass
