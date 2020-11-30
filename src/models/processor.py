from src.models.task import Task
from typing import List

class Processor:

    def __init__(self):
        self.time_units: List[Task] = []

    def add_time_unit(self):
        if self.last_task_ended():
            self.time_units.append(None)
        else:
            self.time_units.append(self.get_current_task())

    def is_free(self):
        return not self.get_current_task()

    def set_task(self, task: Task):
        self.time_units[len(self.time_units) - 1] = task

    def last_task_ended(self):
        last_task = self.get_current_task()
        return (not last_task) or last_task.compute_time <= (len(self.time_units) - self.get_task_last_start_time(last_task))

    def get_current_task(self):
        if len(self.time_units) == 0:
            return None
        return self.time_units[len(self.time_units) - 1]

    def get_task_last_start_time(self, task: Task):
        last_started_time = len(self.time_units) - 1
        found = False
        while last_started_time >= 0:
            if (self.time_units[last_started_time] == task):
                found = True
            elif found:
                return last_started_time + 1
            last_started_time -= 1
        if not found and last_started_time == -1:
            return -1
        else:
            return last_started_time + 1