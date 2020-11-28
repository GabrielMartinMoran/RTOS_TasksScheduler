from src.planners.planner import Planner
from src.models.task import Task
from typing import List
from _distutils_hack import override
from math import gcd

class CyclicExecutivePlanner(Planner):

    def __init__(self, tasks: List[Task], processors: int = 1):
        super().__init__(tasks, processors)
        self.calculate_secondary_period()

    def calculate_secondary_period(self):
        secondary_period = max([x.compute_time for x in self.tasks])
        while not self.validate_secondary_period(secondary_period):
            secondary_period += 1
        self.secondary_period = secondary_period

    @override
    def get_plan(self):
        periods = []

    def validate_secondary_period(self, sp):
        is_valid = False
        for t in self.tasks:
            # 2nd condition
            is_valid = is_valid or (
                (t.deadline / sp) - abs(t.deadline / sp) != 0)

            # 3rd condition
            if (2*sp - gdc(sp, t.compute.time)) > t.deadline:
                return False

        return is_valid
