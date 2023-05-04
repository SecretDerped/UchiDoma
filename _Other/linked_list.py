class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


n3 = Node('third', None)
n2 = Node('second', n3)
n1 = Node('first', n2)

node = n1
s = input()
index = 1

while node is not None:
    if node.value == s:
        print(index)
        break
    else:
        node = node.next
    index += 1
else:
    print(-1)
