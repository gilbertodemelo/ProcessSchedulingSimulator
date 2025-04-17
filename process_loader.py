import csv
from process import Process
from typing import List

class ProcessLoader:

    def __init__(self):
        self._processes = []

    @staticmethod
    def open_file(path: str):
        with open(path, newline='') as csvfile:
            return list(csv.reader(csvfile, delimiter=","))

    @staticmethod
    def load_processes(reader) -> List['Process']:
        processes = []
        next(reader) # skip the headers line
        for row in reader:
            pid = int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            process = Process(pid, arrival, burst)
            processes.append(process)
        return processes


