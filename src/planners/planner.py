from src.utils.lcm import lcm

class Planner:

    def __init__(self ,tasks=[] , processors = 1):
        self.tasks = tasks
        self.processor = processors
        self.calculate_hyperperiod()


    def calculate_hyperperiod(self):
        """
            Calculates the hyper period of the tasks to be scheduled
        """
        self.hyperperiod = lcm([x.deadline for x in self.tasks])

    def get_plan(self):
        pass