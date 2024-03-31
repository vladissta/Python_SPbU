# from Decorators_HW.time_log_decorator import log_execution_time
import random


class BinaryHeap:
    def __init__(self, heap_list=[]):
        self.heap_list = heap_list
        self.size = len(heap_list)

    def __str__(self):
        return ' '.join([str(el) for el in self.heap_list[1:]])

    @property
    def heap_list(self):
        return self._heap_list

    @heap_list.setter
    def heap_list(self, bh_list):
        self._heap_list = [0] + bh_list
        self.size = len(bh_list)

        for pos in range(len(bh_list) // 2, 0, -1):
            self._swap_down(pos)

    def _swap_up(self, position):
        while position > 0:
            if self.heap_list[position] < self.heap_list[position // 2]:
                self.heap_list[position], self.heap_list[position // 2] = \
                    self.heap_list[position // 2], self.heap_list[position]
            else:
                break
            position //= 2

    def insert(self, value):
        self.heap_list.append(value)
        self.size += 1
        self._swap_up(self.size)

    def _swap_down(self, position):
        while position * 2 < self.size:
            if self.heap_list[position * 2] > self.heap_list[position * 2 + 1]:
                min_child_idx = position * 2 + 1
                next_pos = position * 2 + 1
            else:
                min_child_idx = position * 2
                next_pos = position * 2

            if self.heap_list[position] > self.heap_list[min_child_idx]:
                self.heap_list[position], self.heap_list[min_child_idx] = \
                    self.heap_list[min_child_idx], self.heap_list[position]
            else:
                break
            position = next_pos

    def delete_node(self, value):
        for pos, val in enumerate(self.heap_list):
            if val == value:
                if pos == self.size:
                    self.heap_list.pop()
                    self.size -= 1
                else:
                    self.heap_list[pos] = self.heap_list.pop()
                    self.size -= 1
                    if self.heap_list[pos] < self.heap_list[pos // 2]:
                        self._swap_up(pos)
                    else:
                        self._swap_down(pos)
                    break


# @log_execution_time
def _insert_test(heap: BinaryHeap, n_iter: int, integer_limit: int):
    for _ in range(n_iter):
        heap.insert(
            random.randint(1, integer_limit)
        )


# @log_execution_time
def _remove_test(heap: BinaryHeap):
    heap.delete_node(heap.heap_list[-1])


if __name__ == '__main__':
    heap = BinaryHeap()

    _insert_test(heap, 10, 100)
    print(heap.heap_list)
    _remove_test(heap)
    print(heap.heap_list)
