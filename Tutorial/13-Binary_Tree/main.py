from Binary_Tree import *


def main():
    tree = BinaryTree()
    tree.add_node(10)
    tree.add_node(20)
    tree.add_node(5)

    print tree.root.data
    print tree.root.right.data
    print tree.root.left.data

    tree.printTree()
if __name__ == "__main__":
    main()
