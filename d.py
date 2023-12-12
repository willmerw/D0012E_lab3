
class D:

    def __init__(self, c, value):
        self.c = c
        self.value = value
        self.size = 1
        self.l = None
        self.r = None
        self.parent = None

    def insert(self, val):
        self.size += 1
        if val >= self.value:
            if self.r is None:
                self.r = D(self.c,val)
                self.r.parent = self
            else:
                self.r.insert(val)
                if self.r.size > (self.size * self.c):
                    new_root = self.reorder(self.in_order_walk())
                    self.value = new_root.value
                    self.l = new_root.l
                    self.r = new_root.r

        elif val < self.value:
            if self.l is None:
                self.l = D(self.c, val)
                self.l.parent = self
            else:
                self.l.insert(val)
                if self.l.size > (self.size * self.c):
                    new_root = self.reorder(self.in_order_walk())
                    self.value = new_root.value
                    self.l = new_root.l
                    self.r = new_root.r




    def in_order_walk(self):
        left = []
        right = []
        middle = [self.value]
        if self.l and self.r:
            left = self.l.in_order_walk()
            right = self.r.in_order_walk()
            return left + middle + right
        if self.l:
            return self.l.in_order_walk() + [self.value]
        if self.r:
            return [self.value] + self.r.in_order_walk()
        else:
            return [self.value]

    def reorder(self, ls):

        if len(ls) == 1:
            return D(self.c, ls[0])
        elif len(ls) == 2:
            root = D(self.c, ls[1])
            root.l = D(self.c,ls[0])
            return root

        m = len(ls)//2
        root = D(self.c,ls[m])
        root.l = self.reorder(ls[:m])
        root.l.parent = root
        root.r = self.reorder(ls[m+1:])
        root.r.parent = root
        root.size = root.l.size + root.r.size

        return root












