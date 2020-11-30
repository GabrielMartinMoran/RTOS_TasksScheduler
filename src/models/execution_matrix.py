from src.models.task import Task
from src.models.processor import Processor

class ExecutionMatrix:

    def __init__(self, processors_number: int, hyperperiod: int, secondary_period: int = None):
        self.hyperperiod = hyperperiod
        self.secondary_period = secondary_period
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
        
    def to_dict(self):
        processors_dict = {}
        for x in self.processors:
            processor_tasks = []
            for t in self.processors[x].time_units:
                if t is not None:
                    processor_tasks.append(t.name)
                else:
                    processor_tasks.append('')
            processors_dict[x] = processor_tasks
        return {
            'processors': processors_dict,
            'hyperperiod': self.hyperperiod,
            'secondaryPeriod': self.secondary_period
        }