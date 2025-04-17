import csv
from process import Process
from typing import List
from circularly_linked_list import CircularLinkedList


class ProcessLoader:

    def __init__(self):
        self._processes = []

    @staticmethod
    def open_file(path: str):
        with open(path, newline='') as csvfile:
            return list(csv.reader(csvfile, delimiter=","))

    @staticmethod
    def load_processes(path: str) -> CircularLinkedList:
        reader = ProcessLoader.open_file(path)
        cll: CircularLinkedList = CircularLinkedList()

        iterator = iter(reader)
        next(iterator)  # Skip header line

        for row in iterator:
            pid = int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            process = Process(pid, arrival, burst)
            cll.add_last(process)

        return cll
