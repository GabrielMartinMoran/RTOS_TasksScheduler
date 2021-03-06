from src.planners.planner import Planner
from src.models.task import Task
from typing import List
from math import gcd, floor , pow
from src.models.execution_matrix import ExecutionMatrix
from copy import deepcopy
import functools


class RateMonotonicPlanner(Planner):

    def __init__(self, tasks: List[Task], processors: int = 1):
        super().__init__(tasks, processors)

        if not self.is_planeable():
            print("RateMonotonic no cumple el factor de utilizacion del conjunto de tareas, igual se intentara planificar pero no entraran todas las tareas")

        self.matrix = None

    def is_planeable(self):
        n = len(self.tasks)
        max_threshold = n*(pow(2 , (1/n) ) - 1)
        list_map_task = list(map(lambda t: t.compute_time/t.deadline , self.tasks))
        utilization_factor = functools.reduce(lambda a,b: a+b , list_map_task)

        return utilization_factor <= max_threshold


    def sort_tasks(self, tasks: List[Task]):
        return sorted(tasks, key=lambda x: x.deadline)

    def get_plan(self) -> ExecutionMatrix:
        self.matrix = ExecutionMatrix(self.processors, self.hyperperiod)
        tasks_to_add = []
        for x in range(self.hyperperiod):
            for t in self.tasks:
                if self.can_add_task(t, x) and not self.is_task_with_same_id_in_list(t, tasks_to_add):
                    tasks_to_add.append(t)
            tasks_to_add = self.sort_tasks(tasks_to_add)
            for p in range(self.processors):
                processor = self.matrix.processors[p]
                processor.add_time_unit()
                if len(tasks_to_add) == 0:
                    continue
                if processor.is_free():
                    processor.set_task(tasks_to_add.pop(0))
                else:
                    current_task = processor.get_current_task()
                    if current_task.deadline > tasks_to_add[0].deadline:
                        t_copy = deepcopy(current_task)
                        t_copy.compute_time = t_copy.compute_time - (x - processor.get_task_last_start_time(current_task))
                        tasks_to_add.append(t_copy)
                        processor.set_task(tasks_to_add.pop(0))
                        tasks_to_add = self.sort_tasks(tasks_to_add)
                        
                
        return self.matrix

    def can_add_task(self, task: Task, time: int) -> bool:
        last_executed_deadline = floor(self.matrix.get_last_time_task_started(task) / task.deadline)
        current_deadline = floor(time / task.deadline)        
        return last_executed_deadline < current_deadline and self.hyperperiod >= time + task.compute_time

    """
    This method compares 'taks_id' property in tasks, not the reference
    """
    def is_task_with_same_id_in_list(self, task: Task, tasks_list: List[Task]) -> bool:
        for x in tasks_list:
            if x.task_id == task.task_id:
                return True
        return False
