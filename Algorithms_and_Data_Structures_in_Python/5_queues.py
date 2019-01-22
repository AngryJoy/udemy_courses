# define a queue class: First In First Out
class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        return self.queue.append(data)

    def dequeue(self):
        first_out = self.queue[0]
        del self.queue[0]
        return first_out

    def peek(self):
        return self.queue[0]

    @property
    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('xxx')
    queue.enqueue('jj')
    queue.enqueue(9999)
    print("size after enqueuing: ", queue.size)
    print("dequeue: ", queue.dequeue())
    print("size after dequeuing: ", queue.size)
    print("peek: ", queue.peek())
    print(queue.size)
