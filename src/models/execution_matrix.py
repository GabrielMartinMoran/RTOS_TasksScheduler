from src.models.task import Task

class ExecutionMatrix:

    def __init__(self, processors: int):
        self.processors = processors
        self.tasks_indexes_by_processor = [0 for x in range(self.processors)]
        self.taks_by_processor = { x : [] for x in range(self.processors)}

    def add_task(self, task: Task, processor_number: int):
        self.taks_by_processor[processor_number].append(task)

    def get_next_task(self, processor_number: int):
        self.tasks_indexes_by_processor[processor_number] += 1
        return self.tasks_indexes_by_processor[processor_number]

    def __str__(self):
        return "Reemplazar por print de ExecutionMatrix"