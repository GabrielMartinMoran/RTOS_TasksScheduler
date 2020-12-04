from src.planners.planner import Planner
from src.models.task import Task
from typing import List
from math import gcd, floor
from src.models.execution_matrix import ExecutionMatrix
import logging
logger = logging.getLogger(__name__)

class CyclicExecutivePlanner(Planner):

    MAX_PROCESSORS = 1

    def __init__(self, tasks: List[Task], processors: int = 1):
        super().__init__(tasks, processors)
        self.processors = self.MAX_PROCESSORS
        self.calculate_secondary_period()
        self.matrix = None

    def calculate_secondary_period(self):
        # 1st contidion
        try:
            secondary_period = max([x.compute_time for x in self.tasks])
        except ValueError as e:
            logger.error("Provided tasks array is empty")
            secondary_period = 0

        while not self.validate_secondary_period(secondary_period):
            secondary_period += 1
            if secondary_period > self.hyperperiod:
                raise Exception('Could not found a valid secondary period less or equal than hyperperiod')
        self.secondary_period = secondary_period

    def get_plan(self) -> ExecutionMatrix:
        self.matrix = ExecutionMatrix(self.processors, self.hyperperiod, self.secondary_period)
        processor = self.matrix.processors[0]
        for x in range(self.hyperperiod):                
            processor.add_time_unit()
            if not processor.is_free():
                continue
            for t in self.tasks:
                if self.can_add_task(t, x):
                    processor.set_task(t)
                    break
        if(not self.is_valid_matrix_result()):
            raise Exception('Can not get a valid plan with provided tasks configuration')
        return self.matrix

    def is_valid_matrix_result(self):
        for task in self.tasks:
            expected_times = int(task.compute_time * (self.hyperperiod / task.deadline))
            scheduled_times = len(list(filter(lambda x: x == task, self.matrix.processors[0].time_units)))
            if scheduled_times != expected_times:
                return False
        return True

    def can_add_task(self, task: Task, time: int):
        last_executed_deadline = floor(self.matrix.get_last_time_task_started(task) / task.deadline)
        current_deadline = floor(time / task.deadline)        
        return task.compute_time <= self.calculate_remaining_sp_space(time) and (last_executed_deadline < current_deadline)

    def calculate_remaining_sp_space(self, time: int):
        return self.secondary_period - (time % self.secondary_period)

    def validate_secondary_period(self, sp) -> bool:
        is_valid = False
        for t in self.tasks:
            # 2nd condition
            is_valid = is_valid or (
                (t.deadline / sp) - abs(t.deadline / sp) == 0)
            # 3rd condition
            if ((2 * sp) - gcd(sp, t.deadline)) > t.deadline:
                return False
        return is_valid
