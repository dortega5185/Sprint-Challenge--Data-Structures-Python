class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # Insert the given value into the tree

    def insert(self, value):
        # make a new BSTNode with our value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        # Which direction?
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)  # this will return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
