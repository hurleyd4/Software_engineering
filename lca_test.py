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

    def test_invalid_path(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        path =[]
        self.assertEqual(findPath(1,path,8),False)


if __name__ == '__main__':
    unittest.main()
