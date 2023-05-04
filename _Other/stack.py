class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


stack = Stack()
op = '+-*/'
line = input()
for elem in line.split():
    if elem in op:
        second = stack.pop()
        first = stack.pop()
        if elem == '+':
            stack.push(first + second)
        elif elem == '-':
            stack.push(first - second)
        elif elem == '*':
            stack.push(first * second)
        elif elem == '/':
            stack.push(first // second)
    else:
        stack.push(int(elem))
print(stack.pop())
