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

    def findAllPaths(self, root, end, path=[]):
        graph = self.__graph_dict
        path = path + [root]
        if root == end:
            return [path]
        if root not in graph:
            return []
        paths = []
        for vertex in graph[root]:
            if vertex not in path:
                extended_paths = self.findAllPaths(vertex,
                                                     end,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    # Returns LCA if node n1 , n2 are present in the given
    # binary tre otherwise return -1
    def findLCA(self, root, n1, n2):

        # To store paths to n1 and n2 from the root
        path1 = []
        path2 = []
        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        path1 = self.findAllPaths(root,n1)
        path2 = self.findAllPaths(root,n2)

        if path1 == [] or path2 == []:
            return -1;

        # Compare the paths to get the first different value
        possibleLCAs = []
        for x in path1:
            i = 0
            for y in path2:
                while(i < len(x) and i < len(y)):
                    if x[i] != y[i]:
                        break
                    i += 1
                if(x[i-1] == n1 or x[i-1] == n2):
                    return x[i-1];
                else:
                    possibleLCAs.append(x[i-1])

        set_of_lcas = remove_duplicates(possibleLCAs)
        if len(set_of_lcas) > 1:
            return self.findDeepestLCA(root, set_of_lcas)
        else:
            return set_of_lcas[0]


    def findDeepestLCA(self, root, set):
        maxLength = 0
        currentLength = 0
        lca = root
        paths = []
        for i in set:
            paths = self.findAllPaths(root, i)
            for j in paths:
                currentLength = len(j)
                if(currentLength > maxLength):
                    maxLength = currentLength
                    lca = i
        return lca

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
