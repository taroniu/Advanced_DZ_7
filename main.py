from queue import LifoQueue


class Stack:
    def __init__(self):
        self.stack = LifoQueue()

    def is_empty(self):
        return self.stack.empty()

    def push(self, element):
        self.stack.put(element)

    def pop(self):
        return self.stack.get()

    def peek(self):
        element = self.stack.get()
        self.stack.put(element)
        return element

    def size(self):
        return self.stack.qsize()


stack_object = Stack()

print(stack_object.is_empty())
stack_object.push(1)
stack_object.push(2)
stack_object.push(3)
stack_object.push(4)
stack_object.push(5)
print(stack_object.pop())
print(stack_object.peek())
print(stack_object.size())

'''задача 2'''

example1 = '(((([{}]))))'
example2 = '[([])((([[[]]])))]{()}'
example3 = '{{[()]}}'
example4 = '}{}'
example5 = '{{[(])]}}'
example6 = '[[{())}]'


open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(example):
    stack = []
    for i in example:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            position = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[position] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return 'Несбалансированно'
    if len(stack) == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

if __name__ == '__main__':
    print(check(example1))