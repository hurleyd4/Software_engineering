import unittest
from lca import Node
from lca import findLCA
from lca import findPath

class testLCA(unittest.TestCase):

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    def test_null_tree(self):
        self.assertEqual( findLCA(None,3,4), -1)
        self.assertEqual( findPath(None,1,1), False)

    def test_root_only(self):
        root = Node(1)
        self.assertEqual( findLCA(root,1,1), 1)

    def test_invalid_key(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root,4,8),-1)

    def test_invalid_type(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        path =[]
        self.assertEqual(findLCA(root,path,"text"),-1)

    def test_successful_lca(self):          #           BST Example
        root = Node(6)                      #
        root.left = Node(4)                 #               6
        root.right = Node(2)                #
        root.left.left = Node(5)            #       4               2
        root.left.right = Node(1)           #
        root.right.left = Node(7)           #   5       1       7       3
        root.right.right = Node(3)          #
        root.right.right.right = Node(8)    #                               8
        self.assertEqual(findLCA(root,1,5),4)
        self.assertEqual(findLCA(root,7,4),6)
        self.assertEqual(findLCA(root,8,3),3)
        self.assertEqual(findLCA(root,1,8),6)

if __name__ == '__main__':
    unittest.main()
