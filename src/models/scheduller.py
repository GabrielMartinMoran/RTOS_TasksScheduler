from typing import List
from src.models.task import Task
from src.planners.cyclic_executive_planner import CyclicExecutivePlanner

class Scheduler:

    SORT_CRITERIA = {
        'FIFO': None # Default
    }

    def __init__(self, tasks: List[Task], processors: int, sort_criterion= 'FIFO'):
        self.tasks = self.sort_tasks(tasks, sort_criterion)
        self.planner = CyclicExecutivePlanner(self.tasks, processors)

    def schedule(self):
        print(self.planner.get_plan())

    def sort_tasks(self, tasks: List[Task], sort_criterion):
        if sort_criterion in self.SORT_CRITERIA and self.SORT_CRITERIA[sort_criterion]:
            return self.SORT_CRITERIA[sort_criterion](tasks)
        return tasks
        
        