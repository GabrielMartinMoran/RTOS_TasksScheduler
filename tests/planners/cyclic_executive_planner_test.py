import pytest
from src.planners.cyclic_executive_planner import CyclicExecutivePlanner
from src.models.task import Task
from src.models.execution_matrix import ExecutionMatrix


def test_calculates_secondary_period_when_initialized():
    planner = CyclicExecutivePlanner([Task('T1', 10, 5)])
    assert planner.secondary_period == 5
    planner = CyclicExecutivePlanner(
        [Task('T1', 20, 3), Task('T2', 5, 2), Task('T3', 10, 2)])
    assert planner.secondary_period == 3
    planner = CyclicExecutivePlanner(
        [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)])
    assert planner.secondary_period == 20


def test_initialization_trows_error_when_tasks_is_empty():
    with pytest.raises(Exception):
        CyclicExecutivePlanner([])


def test_initialization_trows_error_when_secondary_period_cannot_be_calculated():
    with pytest.raises(Exception):
        CyclicExecutivePlanner([Task('T1', 30, 60), Task('T2', 20, 3)])


def test_planner_always_set_processors_in_one_when_initialized():
    planner = CyclicExecutivePlanner([Task('T1', 10, 5)], 5)
    assert planner.processors == 1


def test_can_add_task_returns_true_when_task_can_fit_in_secondary_period_and_was_not_executed_in_this_deadline_slice():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = CyclicExecutivePlanner(tasks)
    planner.matrix = ExecutionMatrix(
        planner.hyperperiod, planner.hyperperiod, planner.secondary_period)
    assert planner.can_add_task(tasks[0], 0)


def test_can_add_task_returns_false_when_task_not_fit_in_secondary_period():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = CyclicExecutivePlanner(tasks)
    planner.matrix = ExecutionMatrix(
        planner.hyperperiod, planner.hyperperiod, planner.secondary_period)
    time_stamp = 15
    for x in range(time_stamp):
        planner.matrix.processors[0].add_time_unit()
    assert not planner.can_add_task(tasks[0], time_stamp)


def test_can_add_task_returns_false_when_task_was_already_enqueued_in_this_deadline_slice():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = CyclicExecutivePlanner(tasks)
    planner.matrix = ExecutionMatrix(
        planner.hyperperiod, planner.hyperperiod, planner.secondary_period)
    planner.matrix.processors[0].add_time_unit()
    planner.matrix.processors[0].set_task(tasks[0])
    for x in range(tasks[0].deadline - 1):
        planner.matrix.processors[0].add_time_unit()
    assert not planner.can_add_task(tasks[0], planner.secondary_period + 1)


def test_calculate_remaining_sp_space_returns_remaining_secondary_period_space_when_timestamp_provided():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = CyclicExecutivePlanner(tasks)
    assert planner.calculate_remaining_sp_space(0) == 20
    assert planner.calculate_remaining_sp_space(1) == 19
    assert planner.calculate_remaining_sp_space(19) == 1
    assert planner.calculate_remaining_sp_space(20) == 20
    assert planner.calculate_remaining_sp_space(39) == 1


def test_validate_secondary_period_returns_true_when_provided_sp_is_valid():
    planner = CyclicExecutivePlanner(
        [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)])
    assert planner.validate_secondary_period(20)


def test_validate_secondary_period_returns_false_when_provided_sp_is_negative():
    planner = CyclicExecutivePlanner(
        [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)])
    assert not planner.validate_secondary_period(-5)


def test_validate_secondary_period_returns_false_when_not_full_frame_from_task_start_to_task_deadline_for_each_task():
    planner = CyclicExecutivePlanner(
        [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)])
    assert not planner.validate_secondary_period(15)


def compare_each_processor_value(expected, processor):
    for x in range(len(expected)):
        if processor.time_units[x] is None:
            assert expected[x] == ''
        else:
            assert processor.time_units[x].name == expected[x]


def test_get_plan_returns_cyclic_executive_planified_matrix_when_tasks_are_valids():
    # Case 1
    planner = CyclicExecutivePlanner([Task('T1', 5, 2), Task('T2', 10, 3), Task('T3', 5, 1)])
    matrix = planner.get_plan()
    expected = ['T1',  'T1',  'T3',  'T2', 'T2',  'T2',  'T1',  'T1',  'T3', '']
    compare_each_processor_value(expected, matrix.processors[0])
    # Case 2
    planner = CyclicExecutivePlanner([Task('T1', 6, 2), Task('T2', 4, 1), Task('T3', 10, 3)])
    matrix = planner.get_plan()
    expected = ['T1',  'T1',  'T2',  '',  'T2',  'T3',  'T3',  'T3',  'T1',  'T1',  'T2',  '',  'T1',  'T1',  'T2',  '',  'T2',  'T3',  'T3',  'T3',  'T1',  'T1',  'T2',  '',  'T1',  'T1',  'T2',  '',  'T2',
                'T3',  'T3',  'T3',  'T1',  'T1',  'T2',  '',  'T1',  'T1',  'T2',  '',  'T2',  'T3',  'T3',  'T3',  'T1',  'T1',  'T2',  '',  'T1',  'T1',  'T2',  '',  'T2',  'T3',  'T3',  'T3',  'T1',  'T1',  'T2',  '']
    compare_each_processor_value(expected, matrix.processors[0])
