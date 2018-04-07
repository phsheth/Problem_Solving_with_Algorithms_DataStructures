class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.isEmpty())
s.push('4')
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
m.peek()
print(m.peek())


t = Stack()
t.push('x')
t.push('y')
t.push('z')
while not t.isEmpty():
   t.pop()
   t.pop()
print(t.peek())