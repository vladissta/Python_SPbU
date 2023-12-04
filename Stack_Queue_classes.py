class Stack:

    def __init__(self):
        self.stack_list = []

    def __len__(self):
        return len(self.stack_list)

    def pop(self):
        self.stack_list.pop()

    def push(self, num):
        self.stack_list.append(num)

    @property
    def top_element(self):
        return self.stack_list[~0]


class Queue:

    def __init__(self):
        self.queue_list = []

    def __len__(self):
        return len(self.queue_list)

    def dequeue(self):
        self.queue_list.pop()

    def enqueue(self, num):
        self.queue_list.insert(0, num)

    @property
    def last_element(self):
        return self.queue_list[0]

    @property
    def first_element(self):
        return self.queue_list[~0]


if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.push(4)

    assert stack.top_element == 4, 'ERROR 1'
    print('PASSED 1')
    assert len(stack) == 3, 'ERROR 2'
    print('PASSED 2')

    stack.pop()
    assert len(stack) == 2, 'ERROR 3'
    print('PASSED 3')

    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    assert queue.first_element == 3, 'ERROR 4'
    print('PASSED 4')
    assert queue.last_element == 5, 'ERROR 5'
    print('PASSED 5')

    queue.dequeue()
    assert queue.first_element == 4, 'ERROR 6'
    print('PASSED 6')
