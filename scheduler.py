
from process_loader import ProcessLoader
from circularly_linked_list import CircularLinkedList

class Scheduler:

    def __init__(self, path):
        self._cll = ProcessLoader.load_processes(path)


    @property
    def size(self):
        return self._cll.size


