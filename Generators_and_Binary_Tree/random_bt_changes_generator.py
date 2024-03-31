import random
from BinaryTree import BinaryHeap, _insert_test


def random_changes_generator(binary_heap: BinaryHeap, n_iter=1000, max_value_insert=1000):
    # fun_list = [binary_heap.delete_node, binary_heap.insert]

    for _ in range(n_iter):

        if binary_heap.size == 0:
            fun_idx = 1
        else:
            fun_idx = random.randint(0, 1)

        if fun_idx:
            num_to_insert = random.randint(1, max_value_insert)
            binary_heap.insert(num_to_insert)
        else:
            idx_to_delete = random.randint(1, binary_heap.size)
            binary_heap.delete_node(binary_heap.heap_list[idx_to_delete])

        yield binary_heap


if __name__ == '__main__':
    heap = BinaryHeap()
    _insert_test(heap, 10, 30)
    rcg = random_changes_generator(heap, 1, 30)

    print(heap.heap_list)

    for _ in range(5):
        heap = next(rcg)

    print(heap.heap_list)
