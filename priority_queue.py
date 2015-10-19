

class Heap(object):

    def __init__(self):
        self.items = []

    def root(self):
        if not self.items:
            return None
        return self.items[0]

    def push(self, item):
        self.items.append(item)
        self.heap_up(index=len(self.items)-1)

    def peek(self):
        if not self.items:
            return None
        return self.items[0]

    def pop(self):
        if not self.items:
            return None

        #swap
        self.swap(0, len(self.items)-1)

        #obtainning result
        result = self.items[len(self.items)-1]
        del self.items[len(self.items)-1]

        #rearrange
        self.heap_down()
        return result

    def swap(self, index_1, index_2):
        self.items[index_1], self.items[index_2] = self.items[index_2], self.items[index_1]

    def heap_up(self, index=0):
        if index > 0:
            if self.items[index].priority > self.items[index/2].priority:
                self.swap(index, index/2)
                self.heap_up(index=index/2)

    def heap_down(self, index=0):
        child_1 = 2 * index + 1
        child_2 = 2 * index + 2

        selected_index = child_1
        if child_1 >= len(self.items):
            return
        elif child_2 < len(self.items) and self.items[child_1].priority < self.items[child_2].priority:
            selected_index = child_2

        self.swap(index, selected_index)
        self.heap_down(index=selected_index)


    def generator(self):
        while self.peek():
            result = self.pop()
            yield result

class Priority(object):

    def __init__(self, value, priority):
        self.priority = priority
        self.value = value

heap = Heap()
#print "C"
heap.push(Priority("C",4))
#print "D"
heap.push(Priority("D",3))
#print "F"
heap.push(Priority("F",1))
#print "A"
heap.push(Priority("A",6))
#print "E"
heap.push(Priority("E",2))
#print "B"
heap.push(Priority("B",5))

for item in heap.generator():
    print item.value
