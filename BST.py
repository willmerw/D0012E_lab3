class BST:

    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.parent = None

    def insert(self, val):
        if val >= self.value:
            if self.r is None:
                self.r = BST( val)
                self.r.parent = self
            else:
                self.r.insert(val)


        elif val < self.value:
            if self.l is None:
                self.l = BST(val)
                self.l.parent = self
            else:
                self.l.insert(val)