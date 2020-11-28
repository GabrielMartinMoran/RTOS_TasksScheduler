from src.models.scheduller import Scheduler
from src.models.task import Task

def main():
    TASKS = [
        Task(20, 8),
        Task(40, 12)
    ]
    PROCESSORS = 1
    scheduler = Scheduler(TASKS, PROCESSORS)
    scheduler.schedule()

if __name__ == "__main__":
    main()
