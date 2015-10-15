

class Tree(object):
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def pre_order(self):
        print self.value

        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print self.value
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print self.value


t = Tree(7)
t1 = Tree(4)
t2 = Tree(11)
t11 = Tree(3)
t12 = Tree(5)
t111 = Tree(1)
t112 = Tree(4)
t21 = Tree(8)
t22 = Tree(15)
t221 = Tree(12)


t.left = t1
t.right = t2

t2.left = t21
t2.right = t22
t22.left = t221


t1.left = t11
t1.right = t12

t11.left = t111
t11.right = t112



t.in_order()
