class Element:
    def __init__(self, value: int):
        self.value = value
        self.next_element = None


class LinkedList:
    def __init__(self):
        self.first_element = None

    def is_empty(self):
        return not self.first_element

    def __len__(self):
        current_element = self.first_element
        length = 0
        while current_element:
            length += 1
            current_element = current_element.next_element
        return length

    def search_element(self, num):
        current_element = self.first_element
        while current_element:
            if current_element.value == num:
                return True
            current_element = current_element.next_element
        return False

    def add_element(self, num):
        element_to_add = Element(num)
        element_to_add.next_element = self.first_element
        self.first_element = element_to_add

    def remove_element(self, num):
        current_element = self.first_element
        previous_element = None

        while current_element:
            if current_element.value == num:
                if not previous_element:
                    self.first_element = current_element.next_element
                    return
                else:
                    previous_element.next_element = current_element.next_element
                    current_element.next_element = None
                    return
            previous_element = current_element
            current_element = current_element.next_element

        print(f'There is no {num} in list')


if __name__ == '__main__':
    llist = LinkedList()
    llist.add_element(2)
    llist.add_element(4)
    llist.add_element(8)

    assert not llist.search_element(3), "ERORR 1"
    print('PASSED 1')
    assert llist.search_element(4), "ERORR 2"
    print('PASSED 2')

    llist.remove_element(4)
    llist.remove_element(5)
    llist.add_element(1)
    llist.add_element(5)

    assert not llist.search_element(4), "ERROR 3"
    print('PASSED 3')
    assert llist.search_element(5), "ERROR 4"
    print('PASSED 4')

    assert len(llist) == 4, "ERROR 5"
    print('PASSED 5')
