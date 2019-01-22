# define stacks class: Last In First Out
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        # last element is the first to be removed out
        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item

    def peek(self):
        return self.stack[-1]

    @property
    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push('!!!something weird')
    stack.push(11)
    stack.push(22)
    print("size after pushing: ", stack.size)
    print("popped: ", stack.pop())
    print("popped: ", stack.pop())
    print("size after popping: ", stack.size)
    print("peek for last one in: ", stack.peek())
    print("size after peeking: ", stack.size)
