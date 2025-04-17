from node import Node

class CircularLinkedList:

    def __init__(self):
        # self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # @property
    # def head(self):
    #     return self._head

    @property
    def tail(self):
        return self._tail

    @property
    def size(self):
        return self._size

    # @head.setter
    # def head(self, new_head: Node):
    #     self._head = new_head

    @tail.setter
    def tail(self, new_tail: Node):
        self._tail = new_tail

    def add_first(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.tail = new_node
        else:
            # new node will point to tail.next
            new_node.next = self.tail.next

            # tail will point to the new node
            self.tail.next = new_node
        self._size += 1

    def add_last(self, element):
        if self.is_empty():
            self.add_first(element)
        else:
            new_node = Node(element)
            new_node.next = self.tail.next  # new node points to head
            self.tail.next = new_node  # old tail points to new node
            self.tail = new_node  # update tail
            self._size += 1

    def remove_first(self):
        head = self.tail.next
        if self.is_empty():
            raise Exception("Linked list is empty.")
        else:
            head = self.tail.next
            # make tail point to the next after head
            self.tail.next = self.tail.next.next
            head.next = None
        self._size -= 1
        return head.value

    def remove_last(self):
        if self.is_empty():
            raise Exception("Linked list is empty.")

        old_tail = self.tail

        if self.tail.next == self.tail:  # only one element
            self.tail = None
        else:
            prev = self.tail.next  # start from head
            while prev.next != self.tail:
                prev = prev.next
            prev.next = self.tail.next  # point to head
            self.tail = prev
        self._size -= 1
        return old_tail.value

    def __str__(self):
        if self.is_empty():
            return "Empty list"

        result = []
        current = self.tail.next  # head
        while True:
            result.append(str(current.value))
            current = current.next
            if current == self.tail.next:  # back to head
                break
        return " -> ".join(result) + " (circular)"
