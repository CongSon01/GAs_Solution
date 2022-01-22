from Data import Data
from Schedule import Schedule
from Data import Data

'''
Population tổng hợp và chọn ngẫu nhiên quần thể ban đầu.
'''
class Population:
    def __init__(self, size, data: Data):
        self._size = size
        self._data = data
        self._schedule: list[Schedule] = []
        for i in range(0, size):
            self._schedule.append(Schedule(self._data).initialize())

    def getSchedule(self): return self._schedule