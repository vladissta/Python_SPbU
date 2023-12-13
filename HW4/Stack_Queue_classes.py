class Stack:
    """
    Stack class stores elements of stack and useful methods and attributes to interact with it
    """

    def __init__(self):
        self.stack_list = []

    def __len__(self):
        return len(self.stack_list)

    def pop(self):
        """
        Returns top element of the stack and deletes it from stack
        :return: top element
        """
        if len(self):
            return self.stack_list.pop()
        else:
            raise IndexError('Empty Stack!')

    def push(self, num: int):
        """
        Pushes new element to the top of the stack
        :param num: number to add to the top of the stack
        :return: None
        """
        self.stack_list.append(num)

    @property
    def top_element(self):
        """
        :return: top element
        """
        return self.stack_list[~0]


class Queue:
    """
    Class Queue stores elements of queue and useful methods and attributes to interact with it
    """

    def __init__(self):
        self.queue_list = []

    def __len__(self):
        return len(self.queue_list)

    def dequeue(self):
        """
        Returns first (next) element in the queue and deletes it from the queue
        :return: first (next) element in the queue
        """
        if len(self):
            return self.queue_list.pop()
        else:
            raise IndexError('Empty Queue!')

    def enqueue(self, num: int):
        """
        Adds new element to the end of the queue
        :param num: number to add to queue
        :return: None
        """
        self.queue_list.insert(0, num)

    @property
    def last_element(self):
        """
        :return: last element in the queue
        """
        return self.queue_list[0]

    @property
    def first_element(self):
        """
        :return: first element in the queue
        """
        return self.queue_list[~0]


if __name__ == '__main__':
    print('Small tests:')

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
