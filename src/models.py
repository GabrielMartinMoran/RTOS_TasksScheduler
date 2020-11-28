
class Task:
    def __init__(self , deadline, compute_time,release_time,exec_time):
        self.deadline = deadline
        self.compute_time = compute_time
        self.release_time = release_time
        self.exec_time = exec_time

    def run(self):
        pass

class Scheduler:
    def __init__(self , planner = None , mapped_task_list = []):
        self.planner = planner
        self.mapped_task_list = mapped_task_list


    def create_scheduler(self):
        pass

    def dispatch(self):
        pass

class Processor:
    def __init__(self, task=None,):
        self.task = task
        self.is_free = False
        self.task_remaining_time = 0


    def execute(self):
        pass





