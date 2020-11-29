from src.models.task import Task
from src.models.processor import Processor

class ExecutionMatrix:

    def __init__(self, processors_number: int, hyperperiod: int):
        self.hyperperiod = hyperperiod
        self.processors = { x : Processor() for x in range(processors_number)}

    def get_last_time_task_started(self, task: Task):
        times = []
        for x in self.processors:
            times.append(self.processors[x].get_task_last_start_time(task))
        return max(times)

    def print(self):
        print('Execution Matrix result:')
        for x in range(len(self.processors)):
            tasks_str = ''
            for t_i, t in enumerate(self.processors[x].time_units):
                if t is None:
                    tasks_str += f' _'
                else:
                    tasks_str += f' {t.name}'
                tasks_str += (',' if t_i < len(self.processors[x].time_units) - 1 else '')
            print(f'> Processor {x}: {tasks_str}')
        