import math


class Heap(object):

    def __init__(self):
        self.nodes = []

    def track(self, n):
        self.nodes.append(n)
        self.swap_up(len(self.nodes)-1)

    def swap_up(self, index):
        if self.nodes[index/2] > self.nodes[index]:
            self.nodes[index/2], self.nodes[index] = self.nodes[index], self.nodes[index/2]
            return swap_up(index/2)

    def getRankNumber(self, n):
        for x in xrange(0, len(self.nodes)):
            if self.nodes[x] == n:
                return math.floor(math.log(x)) + 1

        return -1


heap = Heap()

heap.track(1)
heap.track(2)
heap.track(3)
heap.track(4)
heap.track(5)

print heap.getRankNumber(int(5)) + 1
