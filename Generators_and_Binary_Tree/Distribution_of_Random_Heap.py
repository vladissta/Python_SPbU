from BinaryTree import BinaryHeap
from random_bt_changes_generator import random_changes_generator
import matplotlib.pyplot as plt

trees = []

for _ in range(100):
    tree_to_random = BinaryHeap()
    rcg = random_changes_generator(tree_to_random, 1000)
    for heap in rcg:
        tree_to_random = heap
    trees.append(tree_to_random)

sizes = [tree.size for tree in trees]
nums = sum([tree.heap_list for tree in trees], [])

_, axes = plt.subplots(1, 2, figsize=(10, 6))
axes[0].hist(sizes, bins=range(min(sizes), max(sizes) + 5, 5))
axes[0].set_title('Distribution of tree sizes')

axes[1].hist(nums, bins=range(min(nums), max(nums) + 50, 50))
axes[1].set_title('Distribution of keys in trees')
plt.show()
