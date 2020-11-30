#from src.models.scheduller import Scheduler
#from src.models.task import Task
from src.server.server import run_server

def main():
    run_server()
    """
    TASKS = [
        Task("T1", 30, 6),
        Task("T3", 20, 3),
        Task("T2", 120, 14)
    ]
    """
    """    
    TASKS = [
        Task("T1", 20, 3),
        Task("T2", 5, 2),
        Task("T3", 10, 2)
    ]
    PROCESSORS = 50
    scheduler = None
    try:
        scheduler = Scheduler(TASKS, PROCESSORS)
    except Exception as e:
        print(e)
        return    
    scheduler.schedule()
    """

if __name__ == "__main__":
    main()
