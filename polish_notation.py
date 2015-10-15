

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def peek(self):
        if not self.stack:
            return None
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if not self.stack:
            return None
        elem = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack)-1]

        return elem

    def generator(self):
        x = self.pop()
        if x:
            yield x

def is_op(op):
    return op == '+' or op == '-' or op == '/' or op == '*'

def solve_op(num1,num2,op):
    if op == '+':
        return float(num1) + float(num2)
    elif op == '-':
            return float(num1) - float(num2)
    elif op == '*':
        return float(num1) * float(num2)
    elif op == '/':
        return float(num1) / float(num2)


def polish_notation(str):

    stack = Stack()
    stack_2 = Stack()

    for x in str.strip().split(' ')[::-1]:
        stack.push(x)

    while stack.peek():
        elem = stack.pop()

        if not is_op(elem):
            stack_2.push(elem)
        else:
            stack_2.push(solve_op(stack_2.pop(), stack_2.pop(), elem))

    return stack_2.pop()


print polish_notation("4 1 + 2.5 *")
