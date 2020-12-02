import pytest

from src.models.task import Task

def test_attributes_tasks():

    e_task = Task(
        name="A",
        deadline=1,
        compute_time=100
    )

    assert e_task.name == "A"
    assert e_task.deadline == 1
    assert e_task.compute_time == 100
    assert e_task.task_id != ""


def test_repr_tasks():

    e_task = Task(
        name="A",
        deadline=1,
        compute_time=100
    )

    assert  e_task.__str__() == "A -> C:100 | D:1"


