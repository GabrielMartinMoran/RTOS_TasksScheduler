from src.models.scheduller import Scheduler
from src.models.task import Task

def main():
    TASKS = [
        Task("T1", 30, 6),
        Task("T3", 20, 3),
        Task("T2", 120, 14),
    ]
    PROCESSORS = 1
    scheduler = Scheduler(TASKS, PROCESSORS)
    scheduler.schedule()

if __name__ == "__main__":
    main()