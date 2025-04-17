class Process:
    def __init__(self, pid: int, arrival_time: int, total_burst_time: int):
        self._pid: int = pid
        self._arrival_time: int = arrival_time
        self._total_burst_time: int = total_burst_time
        self._remaining_time: int = total_burst_time  # Starts equal to total burst time
        self._start_time: int = None
        self._end_time: int = None
        self._waiting_time: int = 0
        self._state: str = "new"  # Possible states: new, ready, running, finished

    # Read-only properties
    @property
    def pid(self):
        return self._pid

    @property
    def arrival_time(self):
        return self._arrival_time

    @property
    def total_burst_time(self):
        return self._total_burst_time

    @property
    def remaining_time(self):
        return self._remaining_time

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @property
    def waiting_time(self):
        return self._waiting_time

    @property
    def state(self):
        return self._state

    # Writable properties
    @remaining_time.setter
    def remaining_time(self, time: int):
        self._remaining_time = time

    @start_time.setter
    def start_time(self, time: int):
        self._start_time = time

    @end_time.setter
    def end_time(self, time: int):
        self._end_time = time

    @waiting_time.setter
    def waiting_time(self, time: int):
        self._waiting_time = time

    @state.setter
    def state(self, new_state: str):
        self._state = new_state
