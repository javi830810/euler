

class PrefixTree(object):

    def __init__(self, value=""):
        self.value = value
        self.children = []
        self.word = False

    def insert(self, word):
        if not word:
            return
        for child in self.children:
            if child.value == word[0]:
                return child.insert(word[1:])

        prefix_children = PrefixTree(word[0])
        if len(word) == 1:
            prefix_children.word = True
        else:
            prefix_children.insert(word[1:])
        self.children.append(prefix_children)


    def exists(self, word):
        if not word:
            return True
        for child in self.children:
            if child.value == word[0]:
                return child.exists(word[1:])

        return False

    def words(self, prefix=""):
        words = []
        word_til_now = prefix + self.value
        for child in self.children:
            words += child.words(word_til_now)
        if self.word:
            words.append(word_til_now)
        return words

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return -1
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

class Graph(object):
    def __init__(self):
        self.nodes = []

    @classmethod
    def _build(cls, prefix):
        graph = Graph()
        words = prefix.words()

        nodes = []
        for word in words:
            nodes.append(Node(word))

        for node in nodes:
            graph.nodes.append(node)

            for other_node in nodes:
                if node.value != other_node.value:
                    if hamming_distance(node.value, other_node.value) == 1:
                        node.push_neighboor(other_node)
        return graph


    def word_ladder(self, word1, word2):
        return self._word_ladder(
            filter(lambda x: x.value == word1, self.nodes)[0],
            filter(lambda x: x.value == word2, self.nodes)[0]
        )

    def _word_ladder(self, node1, node2):
        if node1.value == node2.value:
            return 0
        node1.visited = True

        _min = None
        for neighboor in node1.close:
            if neighboor.visited:
                continue

            dist = self._word_ladder(neighboor, node2)
            if _min:
                _min = min(dist,_min)
            else:
                _min = dist
        if not _min:
            return None
        return 1 + _min

class Node(object):
    def __init__(self, value):
        self.value = value
        self.close = []
        self.visited = False

    def push_neighboor(self, node_word):
        self.close.append(node_word)

rt = PrefixTree()
rt.insert('papa')
rt.insert('papalote')
rt.insert('papamovil')
rt.insert('papal')
rt.insert('dog')
rt.insert('cat')
rt.insert('dat')
rt.insert('dot')
rt.insert('bog')
rt.insert('tod')
rt.insert('cog')
rt.insert('pat')
rt.insert('pag')
rt.insert('cold')
rt.insert('cord')
rt.insert('card')
rt.insert('ward')
rt.insert('warm')

graph = Graph._build(rt)

print graph.word_ladder('cat', 'dog')
