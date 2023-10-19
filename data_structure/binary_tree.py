class BinaryTree:
    def __init__(self, key=0):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key: int):
        if self.key == key:
            return

        if self.key < key:
            if self.left is None:
                self.left = self.__class__(key)
            else:
                self.left.insert(key)

        else:
            if self.right is None:
                self.right = self.__class__(key)
            else:
                self.right.insert(key)
