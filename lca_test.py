import unittest
from lca import Graph

class testLCA(unittest.TestCase):

    def test_null_tree(self):                           #testing both functions for null binary search trees
        g = {}
        self.assertEqual( g.findLCA(None,"a","b"), -1)        #as there is no root the function should return -1
        self.assertEqual( g.findPath("a","b"), False)    #as there is no root the function should return False

    def test_root_only(self):                           #testing for a tree with only one node
        g = {"a"}                                  #setting root equal to nodewith key 1
        path =[]                                        #empty path to pass into findPath function
        self.assertEqual( g.findPath("a","a"), True)  #confirming that path can be found when only the root is available
        self.assertEqual( g.findLCA("a","a","a"), "a")         #confirming that the path that was found gives the correct lca for only root

    def test_invalid_key(self):                         #testing for an invalid node entry
        g = { "a" : ["b","d"],
              "b" : ["c"],
              "c" : ["b", "c", "d", "e"],
              "d" : ["b", "e", "f"],
              "e" : ["c"],
              "f" : ["c"]
            }
        path =[]                                        #
        self.assertEqual(g.findPath("a",8), False)      #the key 8 is invalid, should return False and print "Invalid key input"
        self.assertEqual(g.findLCA("a",8),-1)           #again 8 is invalid, should return -1

    def test_invalid_type(self):                        #testing for an invald type entry
        g = { "a" : ["b","d"],
              "b" : ["c"],
              "c" : ["b", "c", "d", "e"],
              "d" : ["b", "e", "f"],
              "e" : ["c"],
              "f" : ["c"]
            }
        path =[]                                        #
        self.assertEqual(g.findLCA("a",path,"text"),-1)  #a string should return -1 when passed in as a key
        self.assertEqual(g.findLCA(path,-10,"text"),-1)   #path is not a valid root and again text the incorrect input for a key

    def test_successful_lca(self):          #           BST Example
        g = { "a" : ["b","d"],
              "b" : ["c"],
              "c" : ["b", "c", "d", "e"],
              "d" : ["b", "e", "f"],
              "e" : ["c"],
              "f" : ["c"]
            }
        self.assertEqual(g.findLCA(root,1,5),4)#these tests are to show that LCA works as intended
        self.assertEqual(g.findLCA(root,7,4),6)
        self.assertEqual(g.findLCA(root,8,3),3)
        self.assertEqual(g.findLCA(root,1,8),6)
        self.assertEqual(g.findLCA(root,8,8),8) # testing to see if the lca of a node is itself

    #need to begin testing for directed acyclic graph

if __name__ == '__main__':
    unittest.main()
