from src.planners.planner import Planner
from src.models.task import Task
from typing import List
from math import gcd
from src.models.execution_matrix import ExecutionMatrix

class CyclicExecutivePlanner(Planner):

    def __init__(self, tasks: List[Task], processors: int = 1):
        super().__init__(tasks, processors)
        self.calculate_secondary_period()

    def calculate_secondary_period(self):
        # 1st contidion
        secondary_period = max([x.compute_time for x in self.tasks])
        while not self.validate_secondary_period(secondary_period):
            secondary_period += 1
        self.secondary_period = secondary_period

    def get_plan(self) -> ExecutionMatrix:
        matrix = ExecutionMatrix(self.processors)
        return matrix

    def validate_secondary_period(self, sp) -> bool:
        print(f'Probando como periodo secundario {sp}')
        is_valid = False
        for t in self.tasks:
            # 2nd condition
            is_valid = is_valid or ((t.deadline / sp) - abs(t.deadline / sp) == 0)
            # 3rd condition
            if (2*sp - gcd(sp, t.compute_time)) > t.deadline:
                return False
        return is_valid
