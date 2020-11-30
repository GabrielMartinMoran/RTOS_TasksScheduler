from src.utils.lcm import lcm

class Planner:

    def __init__(self ,tasks=[] , processors = 1):
        self.tasks = tasks
        self.processors = processors
        self.calculate_hyperperiod()

    def calculate_hyperperiod(self):
        self.hyperperiod = lcm([x.deadline for x in self.tasks])

    def get_plan(self):
        pass

    def can_add_task(self, task: Task, time: int) -> bool:
        return True