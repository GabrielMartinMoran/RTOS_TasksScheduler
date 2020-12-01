import pytest

from src.models.task import Task
from src.planners.planner import Planner
from src.planners.rate_monotonic_planner import RateMonotonicPlanner
from src.planners.cyclic_executive_planner import CyclicExecutivePlanner

def list_of_tasks():
    return [
        Task(name="T1" , deadline=30 , compute_time=6),
        Task(name="T2" , deadline=120 , compute_time=14),
        Task(name="T3" , deadline=20 , compute_time=3),
    ]

def test_empty_base_planner():

    tasks = []
    processors = 1
    planner = Planner(tasks=tasks , processors=processors)

    assert planner.tasks == []
    assert planner.processors == 1
    planner.calculate_hyperperiod()
    assert planner.hyperperiod == 0


def test_hyperperiod_rate_monotonic_planner():


    tasks = list_of_tasks()
    processors = 1
    planner = RateMonotonicPlanner(tasks=tasks , processors=processors)

    assert planner.tasks == tasks
    assert planner.processors == 1
    planner.calculate_hyperperiod()
    assert planner.hyperperiod == 120


def test_hyperperiod_cyclic_executive_planner():


    tasks = list_of_tasks()
    processors = 1
    planner = CyclicExecutivePlanner(tasks=tasks , processors=processors)

    assert planner.tasks == tasks
    assert planner.processors == 1
    planner.calculate_hyperperiod()
    assert planner.hyperperiod == 120