class Element:
    """
    Element of linked list.
    Stores information about value and next (linked) element -
    None if it is the last element in the list
    """

    def __init__(self, value: int):
        self.value = value
        self.next_element = None


class LinkedList:
    """
    Linked list stores information about head (first) element and different useful methods
    """

    def __init__(self):
        self.first_element = None

    def is_empty(self):
        """
        :return: If empty - True, if not - False
        """
        return not self.first_element  # if First element == None, then there are no elements

    def __len__(self):
        """
        :return: length of the linked list
        """
        current_element = self.first_element
        length = 0
        while current_element:
            length += 1
            current_element = current_element.next_element
        return length

    def search_element(self, num):
        """
        Searches element with value == num in linked list and returns whether element was found
        :param num: number to search in linked list
        :return: If found - True, if not - False
        """
        current_element = self.first_element
        # if iterated to the end of the list (current_element == None)
        # then there is no such element in the list
        while current_element:
            if current_element.value == num:
                return True  # found !
            current_element = current_element.next_element  # next iteration
        return False

    def add_element(self, num):
        """
        Adds element with value == num to the head of the linked list
        :param num: number to add to the head of the linked list
        :return: None
        """
        element_to_add = Element(num)
        element_to_add.next_element = self.first_element
        self.first_element = element_to_add

    def remove_element(self, num):
        """
        Removes element with value == num from the linked list
        :param num: number to remove from the linked list
        :return: None
        """
        current_element = self.first_element
        previous_element = None

        # if iterated to the end of the list (current_element == None)
        # then there is no such element in the list
        while current_element:
            if current_element.value == num:  # if found the value
                if not previous_element:  # if found element is the first element
                    self.first_element = current_element.next_element  # making next element the head
                    return
                else:  # connect previous and next elements -> current element is deleted
                    previous_element.next_element = current_element.next_element
                    current_element.next_element = None
                    return
            # next iteration
            previous_element = current_element
            current_element = current_element.next_element

        print(f'There is no {num} in list')  # if cycle is ended without returning, then print


if __name__ == '__main__':
    print('TESTS:')
    llist = LinkedList()
    llist.add_element(2)
    llist.add_element(4)
    llist.add_element(8)

    assert not llist.search_element(3), "ERORR 1"
    print('PASSED 1')
    assert llist.search_element(4), "ERORR 2"
    print('PASSED 2')

    llist.remove_element(4)
    llist.add_element(1)
    llist.add_element(5)

    assert not llist.search_element(4), "ERROR 3"
    print('PASSED 3')
    assert llist.search_element(5), "ERROR 4"
    print('PASSED 4')

    assert len(llist) == 4, "ERROR 5"
    print('PASSED 5')
