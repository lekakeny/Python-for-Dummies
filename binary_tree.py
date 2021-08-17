"""" A binary tree is a data structure in which each node has at most two children, which are referred as the left
child and the right child.

Traversal is a process of visiting all the nodes of a tree.

Traversal can be done In-order, Pre-order or Post-order

"""

"Define the Tree node"


class BinaryTreeNode(object):
    def __init__(self):
        # Tree node should contain data
        self.data = "#"
        # Reference to the left child
        self.leftChild = None
        # Reference to the right child
        self.rightChild = None


"Define the Tree"


def visitBinaryTreeNode(BinaryTreeNode):
    # Hash (#) sign means empty
    if BinaryTreeNode.data is not '#':
        print(BinaryTreeNode.data, end='->')


class BinaryTree(object):
    # A method to create the tree
    def createBinaryTree(self, Root):
        # Read from standard input and store the data as a Binary Tree
        data = input("==>")
        # If we input a # simple then the tree will not continue to have a right and left child
        if data == '#':
            Root = None
        else:
            # Store the data in the node
            Root.data = data
            # Create left child
            Root.leftChild = BinaryTreeNode()
            # Call createBinaryTree for the left child
            self.CreateBinaryTree(Root.leftChild)
            # Create right child
            Root.rightChild = BinaryTreeNode()
            # Call createBinaryTree for the right child
            self.CreateBinaryTree(Root.rightChild)

    def preOrder(self, Root):
        if Root is not None:
            visitBinaryTreeNode(Root)
            self.preOrder(Root.leftChild)
            self.preOrder(Root.rightChild)

    def inOrder(self, Root):
        if Root is not None:
            self.inOrder(Root.leftChild)
            visitBinaryTreeNode(Root)
            self.inOrder(Root.rightChild)

    def postOrder(self, Root):
        if Root is not None:
            self.postOrder(Root.leftChild)
            self.postOrder(Root.rightChild)
            visitBinaryTreeNode(Root)


"Print the Binary Tree"
bTN = BinaryTreeNode()
bT = BinaryTree
bT.createBinaryTree(bTN)
print('Pre-Order: ')
bT.preOrder()
print('\ninOrder: ')
bT.inOrder()
print('Post_Order: ')
bT.postOrder()

# My code is not running well. I hope to improve it soon :)
