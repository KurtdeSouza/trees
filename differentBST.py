class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

    def insert(self, key):
        if self:
            if key < self.val:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            if key > self.val:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.val = key

    def remove(self, key):
        if self.val == key:
            if self.right and self.left:
                temp = self.right
                self = self.left
                self.right = temp
                return self
            else:
                if self.left:
                    return self.left  # promote the left subtree
                else:
                    return self.right  # promote the right subtree
        else:
            if self.val > key:  # key should be in the left subtree
                self.left = self.left.remove(key)
            else:  # key should be in the right subtree
                self.right = self.right.remove(key)
        return self

    def PrintTree(self, space):
        if self is None:
            return
        space += 5
        if self.right:
            self.right.PrintTree(space)
        spacing = space - 5
        print(end=" " * spacing)
        print(self.val)
        if self.left:
            self.left.PrintTree(space)


if __name__ == "__main__":
    root = Node(5)
    root.insert(8)
    root.insert(10)
    root.insert(9)
    root.insert(11)
    root.PrintTree(0)
    root.remove(8)
    root.PrintTree(0)
