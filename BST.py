class BST:

    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.parent = None

    def insert(self, val):
        current = self
        while True:
            if val >= current.value:
                if current.r is None:
                    current.r = BST(val)
                    current.r.parent = current
                    break
                else:
                    current = current.r
            elif val < current.value:
                if current.l is None:
                    current.l = BST(val)
                    current.l.parent = current
                    break
                else:
                    current = current.l
        