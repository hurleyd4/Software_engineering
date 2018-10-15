# Python Program for Lowest Common Ancestor in a Binary Tree
# O(n) solution to find LCS of two given values n1 and n2

# A binary tree node
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

        try:
            # Baes Case
            if path == None:
                path = []

            graph = self.__graph_dict
            path = path + [start_vertex]

            # Check if k is found in left or right sub-tree
            if ((root.left != None and findPath(root.left, path, k)) or
                    (root.right!= None and findPath(root.right, path, k))):
                return True

                # If not present in subtree rooted with root, remove
            # root from path and return False

            path.pop()
            return False

        except AttributeError as error:     #prevents error being thrown for invalid input
            print "Invalid key input"

    # Returns LCA if node n1 , n2 are present in the given
    # binary tre otherwise return -1
    def findLCA(self, root, n1, n2):

        # To store paths to n1 and n2 fromthe root
        path1 = []
        path2 = []

        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        path1 = self.find_path(root,n1)
        path2 = self.find_path(root, n2)

        # Compare the paths to get the first different value
        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]
