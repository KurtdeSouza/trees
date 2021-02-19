class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.color = 0  # 0 is black, 1 is red
        self.val = value


# Rules:
# 1. Every node is either red or black
# 2. Every leaf (nil) node is black
# 3. If a node is red, then both of its children are black.
# 4. Every simple path from a node to a lead node has the same number of black nodes (including the leaf)
# 5. the root is black.

def Remove(root, node):
    if root is None:
        return root
    if node < root.val:
        root.left = Remove(root.left, node)
    elif node > root.val:
        root.right = Remove(root.right, node)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        elif root.left is None:
            temp = root.right
            root = None
            return temp
        temp = root.left
        temp.right = root.right
        root = None
        return temp


''' 
when making parent, set node.right.parent = current node, node.left.parent = current node
'''


def Insert(r, root, node):
    if root.val < node.val:
        if root.right is None:
            root.right = node
            node.parent = root
            node.color = 1
            recolor(r, node)
        else:
            Insert(r, root.right, node)
    else:
        if root.left is None:
            root.left = node
            node.parent = root
            node.color = 1
            recolor(r, node)
        else:
            Insert(r, root.left, node)


def recolor(root, node):
    if root is node:
        root.color = 0

        return
    if node.parent.color == 1:
        if node.parent.parent:
            if node.parent.val < node.parent.parent.val:
                # left child
                if node.parent.parent.right:
                    if node.parent.parent.right.color == 1:
                        # uncle is red
                        node.parent.color, node.parent.parent.right.color = 0, 0  # change parent and uncle to black
                        node.parent.parent.color = 1  # change grandparent to red
                        recolor(root, node.parent.parent)
                    else:
                        if node.val < node.parent.val:
                            LeftLeft(node)
                        else:
                            LeftRight(node)
            else:
                # right child
                if node.parent.parent.left.color == 1:
                    # uncle is red
                    node.parent.color, node.parent.parent.left.color = 0, 0  # change parent and uncle to black
                    node.parent.parent.color = 1  # change grandparent to red
                    recolor(root, node.parent.parent)
                if node.val > node.parent.val:
                    RightLeft(node)
                else:
                    RightRight(node)


def LeftLeft(node):
    # left left case
    temp = node.parent.parent
    temp.right = node.parent.parent.right
    node.parent.parent = node.parent
    node.parent.left = node
    node.parent.right = temp
    node.parent.color = 0
    node.parent.right = 1


def LeftRight(node):
    temp = node.parent
    node.parent = node
    node.left = temp
    LeftLeft(node)


def RightRight(node):
    temp = node.parent.parent
    temp.left = node.parent.parent.left
    node.parent.parent = node.parent
    node.parent.right = node
    node.parent.left = temp
    node.parent.color, node.parent.left.color = 0, 1


def RightLeft(node):
    temp = node.parent
    node.parent = node
    node.right = temp
    RightRight(node)


def printTree(node, space):
    if node is None:
        return
    space += 5

    printTree(node.right, space)
    spacing = space - 5
    print(end=" " * spacing)
    if node.color == 0:
        color = "black"
    else:
        color = "red"
    print(node.val, color)
    printTree(node.left, space)


if __name__ == "__main__":
    r = Node(5)

    Insert(r, r, Node(3))
    printTree(r, 0)
    print("here")
    Insert(r, r, Node(4))
    printTree(r, 0)
    Insert(r, r, Node(2))
    printTree(r, 0)
    Insert(r, r, Node(7))
    Insert(r, r, Node(6))
    Insert(r, r, Node(8))
    printTree(r, 0)
