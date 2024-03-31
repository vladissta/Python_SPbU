from functools import partial

from Generators_and_Binary_Tree.BinaryTree import BinaryHeap, _insert_test

print0 = partial(print, end='')


def tree_into_parentheses_print(tree: BinaryHeap, pos=1):
    if pos <= tree.size:
        print0('(')
        print0(tree.heap_list[pos])
        tree_into_parentheses_print(tree, pos * 2)
        tree_into_parentheses_print(tree, pos * 2 + 1)
        print0(')')


def tree_into_parentheses_return(tree: BinaryHeap, pos=1, current_str=[]):
    if pos <= tree.size:
        current_str.append('(')
        current_str.append(str(tree.heap_list[pos]))
        tree_into_parentheses_return(tree, pos * 2, current_str=current_str)
        tree_into_parentheses_return(tree, pos * 2 + 1, current_str=current_str)
        current_str.append(')')
        return ''.join(current_str)


if __name__ == '__main__':
    tree = BinaryHeap()
    _insert_test(tree, 8, 20)
    print(tree.heap_list)

    tree_str = tree_into_parentheses_return(tree)
    print(tree_str)

