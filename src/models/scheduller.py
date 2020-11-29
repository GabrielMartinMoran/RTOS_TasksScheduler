from typing import List
from src.models.task import Task
from src.planners.cyclic_executive_planner import CyclicExecutivePlanner
from src.models.execution_matrix_drawer import ExecutionMatrixDrawer

class Scheduler:

    SORT_CRITERIA = {
        'FIFO': None # Default
    }

    def __init__(self, tasks: List[Task], processors: int, sort_criterion= 'FIFO'):
        self.tasks = self.sort_tasks(tasks, sort_criterion)
        self.planner = CyclicExecutivePlanner(self.tasks, processors)

    def schedule(self):
        matrix = self.planner.get_plan()
        drawer = ExecutionMatrixDrawer()
        drawer.draw_matrix(matrix)

    def sort_tasks(self, tasks: List[Task], sort_criterion):
        if sort_criterion in self.SORT_CRITERIA and self.SORT_CRITERIA[sort_criterion]:
            return self.SORT_CRITERIA[sort_criterion](tasks)
        return tasks
        
        