# Python Program for Lowest Common Ancestor in a Binary Tree
# O(n) solution to find LCS of two given values n1 and n2

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
    def findPath(self, root, end, path = None):

        #try:
            # Baes Case
            if path == None:
                path = []
            graph = self.__graph_dict
            path = path + [root]
            if root == end:
                return path
            if root not in graph:
                return None
            for vertex in graph[root]:
                if vertex not in path:
                    extended_path = self.findPath(vertex,
                                                   end,
                                                   path)
                    if extended_path:
                        return extended_path
            return None

        #except AttributeError as error:     #prevents error being thrown for invalid input
        #    print "Invalid key input"

    # Returns LCA if node n1 , n2 are present in the given
    # binary tre otherwise return -1
    def findLCA(self, root, n1, n2):

        # To store paths to n1 and n2 from the root
        path1 = []
        path2 = []
        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        path1 = self.findPath(root,n1)
        path2 = self.findPath(root,n2)
        print("Path1: ")
        print(path1)
        print("Path2: ")
        print(path2)

        if path1 == None:
            return -1;

        if path2 == None:
            return -1;

        # Compare the paths to get the first different value
        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]
