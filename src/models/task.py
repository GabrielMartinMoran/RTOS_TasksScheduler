from src.utils.id_generator import generate_unique_id

class Task:
    def __init__(self, name, deadline, compute_time):
        self.name = name
        self.deadline = deadline
        self.compute_time = compute_time
        self.task_id = generate_unique_id()

    def __repr__(self) -> str:
        return f'{self.name} -> C:{self.compute_time} | D:{self.deadline}'