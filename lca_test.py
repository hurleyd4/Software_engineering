import unittest
from lca import Graph

class testLCA(unittest.TestCase):

    def test_null_tree(self):                           #testing both functions for null binary search trees
        g = {}
        graph = Graph(g)
        self.assertEqual(graph.findLCA(None,"a","b"), -1)        #as there is no root the function should return -1
        self.assertEqual(graph.findPath("a","b"), None)    #as there is no root the function should return False
        self.assertEqual(graph.findAllPaths("a","b"), [])

    def test_root_only(self):                           #testing for a tree with only one node
        g = {"a"}                                  #setting root equal to nodewith key 1
        graph = Graph(g)
        path =[]                                        #empty path to pass into findPath function
        self.assertEqual(graph.findPath("a","a"), ["a"])  #confirming that path can be found when only the root is available
        self.assertEqual(graph.findLCA("a","a","a"), "a")         #confirming that the path that was found gives the correct lca for only root
        self.assertEqual(graph.findAllPaths("a","a"), [["a"]])

    def test_invalid_key(self):                         #testing for an invalid node entry
        g = { "a" : ["b","c"],
              "b" : ["d"],
              "c" : ["d", "e"],
            }
        graph = Graph(g)
        path =[]                                        #
        self.assertEqual(graph.findPath("a",8), None)      #the key 8 is invalid, should return None and print "Invalid key input"
        self.assertEqual(graph.findLCA("a",8, 9),-1)           #again 8 is invalid, should return -1
        self.assertEqual(graph.findAllPaths("a","f"), [])

    def test_invalid_type(self):                        #testing for an invald type entry
        g = { "a" : ["b","c"],
              "b" : ["d"],
              "c" : ["d", "e"],
            }
        graph = Graph(g)
        path =[]                                        #
        self.assertEqual(graph.findLCA("a",path,"text"),-1)  #a string should return -1 when passed in as a key
        #self.assertEqual(graph.findLCA(path,-10,"text"),-1)   #path is not a valid root and again text the incorrect input for a key

    def test_successful_basic_lca(self):          #           BST Example
        g = { "a" : ["b","c"],
              "b" : ["c","d"],
              "c" : ["d", "e"],
              "d" : ["e","f"],
              "e" : ["f"]
            }
        graph = Graph(g)
        #self.assertEqual(graph.findLCA("a","b","e"),"a")#these tests are to show that LCA works as intended
        #self.assertEqual(graph.findLCA("a","d","e"),"a")
        #self.assertEqual(graph.findLCA("a","a","d"),"a")
        #self.assertEqual(graph.findLCA("a","c","d"),"a")
        #self.assertEqual(graph.findLCA("a","b","b"),"b") # testing to see if the lca of a node is itself
        #self.assertEqual(graph.findAllPaths("a","d"),[["a","b","d"],["a","c","d"]])
        #graph.findLCA("a","c","d")

    #will add a test for a more complicated DAG

if __name__ == '__main__':
    unittest.main()
