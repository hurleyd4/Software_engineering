import unittest
from lca import Graph

class testLCA(unittest.TestCase):

    def test_null_tree(self):                           #testing both functions for null binary search trees
        g = {}
        graph = Graph(g)
        self.assertEqual(graph.findLCA(None,"a","b"), -1)        #as there is no root the function should return -1
        self.assertEqual(graph.findAllPaths("a","b"), [])

    def test_root_only(self):                           #testing for a tree with only one node
        g = {"a"}                                  #setting root equal to nodewith key 1
        graph = Graph(g)
        path =[]                                        #empty path to pass into findPath function
        self.assertEqual(graph.findLCA("a","a","a"), "a")         #confirming that the path that was found gives the correct lca for only root
        self.assertEqual(graph.findAllPaths("a","a"), [["a"]])

    def test_invalid_key(self):                         #testing for an invalid node entry
        g = { "a" : ["b","c"],
              "b" : ["d"],
              "c" : ["d", "e"],
            }
        graph = Graph(g)
        path =[]                                        #
        self.assertEqual(graph.findLCA("a",8, 9),-1)           #again 8 is invalid, should return -1
        self.assertEqual(graph.findAllPaths("a","f"), [])


    def test_successful_basic_lca(self):          #           BST Example
        g = { "a" : ["b","c"],
              "b" : ["c","d","e"],
              "c" : ["f"],
              "d" : ["e", "f"],
              "e" : ["f"]
            }
        graph = Graph(g)
        self.assertEqual(graph.findLCA("a","b","e"),"b")#these tests are to show that LCA works as intended
        self.assertEqual(graph.findLCA("a","d","e"),"d")
        self.assertEqual(graph.findLCA("a","a","d"),"a")
        self.assertEqual(graph.findLCA("a","c","d"),"b")
        self.assertEqual(graph.findLCA("a","b","b"),"b") # testing to see if the lca of a node is itself
        self.assertEqual(graph.findAllPaths("a","e"),[ ["a","b","d","e"], ["a","b","e"]])
        self.assertEqual(graph.findLCA("a","f","e"),"e")

    def test_successful_complex_lca(self):          #           BST Example
        g = { 15 :[1,2,3,4],
              1 :[5,9],
              2 :[6,10],
              3 :[7,11],
              4 :[8,12],
              5 :[13],
              6 :[13],
              7 :[13],
              8 :[13],
              9 :[14],
              10 :[14],
              11 :[14],
              12 :[14]
            }
        graph = Graph(g)
        self.assertEqual(graph.findLCA(15,13,10),2)#these tests are to show that LCA works as intended
        self.assertEqual(graph.findLCA(15,5,9),1)
        self.assertEqual(graph.findLCA(15,6,13),6)
        self.assertEqual(graph.findLCA(15,8,3),15)
        self.assertEqual(graph.findLCA(15,2,2),2) # testing to see if the lca of a node is itself
        self.assertEqual(graph.findLCA(15,14,5),1)



if __name__ == '__main__':
    unittest.main()
