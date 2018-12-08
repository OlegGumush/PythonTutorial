class Node(object) :
    def __init__(self  , data):
        self.left = None
        self.right = None
        self.data = data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data


class BinaryTree(object) :

    def __init__(self):
        self.root = None

    def add_node(self , data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self.root = self._add_node(self.root ,data)

    def _add_node(self, tree , data):
        if tree == None :
            return Node(data)

        if(data < tree.getData()):
            tree.left = self._add_node(tree.getLeft(), data)
        else :
            tree.right = self._add_node(tree.getRight(), data)

        return tree

    def printTree(self):
        print 'inorder'
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print str(node.data) + ' '
            self._printTree(node.right)

print ('start binary class ')
b = BinaryTree()
b.add_node(5)
b.printTree()
print ('end binary class ')











