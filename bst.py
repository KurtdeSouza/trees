class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


def add(root, node):
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            add(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            add(root.left, node)


def find(root, node):
    print(root.val)
    if root.val < node.val:
        if root.val < node.val < root.right.val or root.right is None:
            print(node.val, "is not in this tree")
        else:
            find(root.right, node)
    if root.val > node.val:
        if root.val < node.val < root.left.val or root.left is None:
            print(node.val, "is not in this tree")
        else:
            find(root.left, node)


def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)


def printLeast(root):
    if root.left:
        printLeast(root.left)
    else:
        print(root.val)


def printMost(root):
    if root.right:
        printMost(root.right)
    else:
        print(root.val)


def printTree(node, space):
    # Base case
    if (node == None):
        return
    space += 5
    printTree(node.right, space)
    spacing = space - 5
    print(end=" " * spacing)
    print(node.val)
    printTree(node.left, space)


if __name__ == "__main__":
    valid = True
    start = int(input("Please enter a root: "))
    r = Node(start)
    while valid:
        try:
            n = int(input("enter a int for a node or type exit to stop adding nodes: "))
            add(r, Node(n))
            valid = True
        except ValueError:
            valid = False
    find(r, Node(1))
    printTree(r, 0)
