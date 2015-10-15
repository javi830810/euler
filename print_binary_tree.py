

class BTree(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def bfs(self):
        print self.value

        stack = [self]
        level_stack = []

        while stack:
            first = stack[0]
            del stack[0]

            if first.left:
                level_stack.append(self.left)
            if first.right:
                level_stack.append(self.right)

            if not stack:
                level = ""
                for x in level_stack:
                    level += str(x.value) + " "
                if level:
                    print level
                stack = level_stack

tree = BTree(1, BTree(2),BTree(3))


tree.bfs()
