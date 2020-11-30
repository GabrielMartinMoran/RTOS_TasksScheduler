from typing import List
from src.models.task import Task
from src.planners.cyclic_executive_planner import CyclicExecutivePlanner
from src.planners.rate_monotonic_planner import RateMonotonicPlanner

class Scheduler:

    PLANNERS = {
        'CYCLIC_EXECUTIVE': CyclicExecutivePlanner,
        'RATE_MONOTONIC': RateMonotonicPlanner
    }

    def __init__(self, tasks: List[Task], processors: int, planner: str):
        self.planner = self.PLANNERS[planner](tasks, processors)

    def schedule(self):
        return self.planner.get_plan()
        
        