class Node:

    def __init__(self, value, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev


    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev

    @value.setter
    def value(self, val):
        self._value = val

    @next.setter
    def next(self, next_node):
        self._next = next_node

    @prev.setter
    def prev(self, prev_node):
        self._prev = prev_node
