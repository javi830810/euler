

class Tree(object):

    def __init__(self, value=None, nodes=None):
        self.nodes = nodes
        self.value = value


def is_palindrome(level):
    for x in xrange(0,len(level)):
        if level[x].value != level[len(level)-x-1].value:
            return False
    return True

def is_mirror(tree):
    queue = [tree]

    while True:
        current_level = level(queue)
        if not current_level:
            return True
        elif not is_palindrome(current_level):
            return False
        queue = current_level

def level(queue):
    level = []
    while queue:
        el = queue[0]
        queue.remove(el)
        level += el.nodes or []
    return level


tree = Tree(0, [
    Tree(1,[
        Tree(3), Tree(2)
    ]),
    Tree(1,[
        Tree(2), Tree(3)
    ])
])

print is_mirror(tree)
