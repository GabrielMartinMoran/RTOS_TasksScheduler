import pytest
from src.models.processor import Processor
from src.models.task import Task

def test_init_set_time_units_as_empty_array_when_called():
    processor = Processor()
    assert processor.time_units == []

def test_add_time_unit_inserts_none_when_no_last_task():
    processor = Processor()
    processor.add_time_unit()
    assert len(processor.time_units) == 1
    assert processor.time_units[0] is None

def test_add_time_unit_inserts_none_when_last_task_ended():
    processor = Processor()
    processor.add_time_unit()
    t = Task('T1', 2, 1)
    processor.set_task(t)
    processor.add_time_unit()
    assert len(processor.time_units) == 2
    assert processor.time_units[1] is None

def test_add_time_unit_inserts_previous_task_when_last_task_not_ended():
    processor = Processor()
    processor.add_time_unit()
    t = Task('T1', 2, 2)
    processor.set_task(t)
    processor.add_time_unit()
    assert len(processor.time_units) == 2
    assert processor.time_units[1] == t

def test_is_fee_returns_true_when_current_task_is_none():
    processor = Processor()
    processor.add_time_unit()
    assert processor.is_free()

def test_is_fee_returns_false_when_current_task_is_not_none():
    processor = Processor()
    processor.add_time_unit()
    processor.set_task(Task('T1', 2, 2))
    assert not processor.is_free()

def test_set_task_set_last_time_unit_with_task_when_task_provided():
    processor = Processor()
    processor.add_time_unit()
    t = Task('T1', 1, 1)
    processor.set_task(t)
    assert processor.time_units[0] == t

def test_last_task_ended_returns_true_when_current_task_is_none():
    processor = Processor()
    processor.add_time_unit()
    assert processor.last_task_ended()

def test_last_task_ended_returns_true_when_last_assigned_task_ended():
    processor = Processor()
    processor.add_time_unit()
    t = Task('T1', 2, 2)
    processor.set_task(t)
    processor.add_time_unit()
    assert processor.last_task_ended()

def test_last_task_ended_returns_false_when_last_assigned_task_not_ended():
    processor = Processor()
    processor.add_time_unit()
    t = Task('T1', 2, 2)
    processor.set_task(t)
    assert not processor.last_task_ended()


def test_get_current_task_returns_none_when_time_units_is_empty():
    processor = Processor()
    assert processor.get_current_task() is None

def test_get_current_task_returns_last_time_units_element():
    processor = Processor()
    processor.add_time_unit()
    t = Task('T1', 1, 1)
    processor.set_task(t)
    assert processor.get_current_task() == t


def test_get_task_last_start_time_returns_minus_one_when_task_was_never_scheduled():
    processor = Processor()
    processor.add_time_unit()
    t = Task('T1', 1, 1)
    assert processor.get_task_last_start_time(t) == -1

def test_get_task_last_start_time_returns_task_start_timestamp_when_scheduled_task_provided():
    processor = Processor()
    t1 = Task('T1', 2, 2)
    t2 = Task('T2', 2, 1)
    processor.time_units = [None, t1, t1, None, None]
    assert processor.get_task_last_start_time(t1) == 1
    processor.time_units = [None, t2, t1, t1, None]
    assert processor.get_task_last_start_time(t1) == 2
    processor.time_units = [None, None, t1, t1, t2]
    assert processor.get_task_last_start_time(t2) == 4
    processor.time_units = [t1, t1, t2, None, None]
    assert processor.get_task_last_start_time(t2) == 2
    processor.time_units = [t1, t1, None, t2, None]
    assert processor.get_task_last_start_time(t1) == 0