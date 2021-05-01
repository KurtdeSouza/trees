class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree():
    def __init__(self):
        self.LEAF = Node(0)
        self.LEAF.color = 0
        self.LEAF.left = None
        self.LEAF.right = None
        self.root = self.LEAF

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.right == x:
            x.parent.right = y
        else:
            x.parent.left = y
        x.parent = y
        y.left = x

    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.LEAF:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.right == x:
            x.parent.right = y
        else:
            x.parent.left = y
        x.parent = y
        y.right = x

    def fix_insert(self, node):
        # case 0, node is root so color it black and done
        if self.root == node:
            node.color = 0
            return
        parent = node.parent
        # case 1, parent is not red
        if parent.color == 0:
            return
        # case 2, parent is root
        if parent.parent is None:
            parent.color = 0
            return
        # case 3, parent is left/right child and is red
        else:
            # parent is right child
            if parent.key > parent.parent.key:
                # case 3a) uncle is red
                if parent.parent.left.color == 1:
                    parent.color = 0
                    parent.parent.left.color = 0
                    parent.parent.color = 1
                    self.fix_insert(parent.parent)
                    return
                # case 3b) uncle is black
                else:
                    # case 3b1), node is left child of parent
                    if parent.key > node.key:
                        parent.parent.color = 1
                        node.color = 0
                        self.rotate_right(parent)
                        self.rotate_left(parent.parent)
                        return
                    # case 3b2) node is right child of parent
                    else:
                        parent.color = 0
                        parent.parent.color = 1
                        self.rotate_left(parent.parent)
                        return
            else:
                # case 3a) uncle is red
                if parent.parent.right.color == 1:
                    parent.color = 0
                    parent.parent.right.color = 0
                    parent.parent.color = 1
                    self.fix_insert(parent.parent)
                    return
                # case 3b) uncle is black
                else:
                    # case 3b1), node is left child of parent
                    if parent.key > node.key:
                        parent.color = 0
                        parent.parent.color = 1
                        self.rotate_right(parent.parent)
                        return
                    # case 3b2) node is right child of parent
                    else:
                        parent.parent.color = 1
                        node.color = 0
                        self.rotate_left(parent)
                        self.rotate_right(parent.parent)
                        return

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.LEAF
        node.right = self.LEAF
        node.color = 1

        parent = None
        current = self.root
        while current != self.LEAF:
            parent = current
            if node.key > current.key:
                current = current.right
            else:
                current = current.left
        if parent is None:
            self.root = node
        else:
            node.parent = parent
            if node.key > parent.key:
                parent.right = node
            else:
                parent.left = node
        self.fix_insert(node)

    def printTree(self, space, node):
        if node is self.LEAF:
            return
        space += 5
        self.printTree(space, node.right)
        spacing = space - 5
        print(end=" " * spacing)
        if node.color == 1:
            print(node.key, "Red")
        else:
            print(node.key, "Black")
        self.printTree(space, node.left)

    def print(self):
        self.printTree(0, self.root)


if __name__ == '__main__':
    tree = RedBlackTree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(4)
    tree.insert(3)
    tree.insert(6)

    tree.print()
