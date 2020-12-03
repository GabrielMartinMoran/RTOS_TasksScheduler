import pytest
from src.planners.rate_monotonic_planner import RateMonotonicPlanner
from src.models.task import Task
from src.models.execution_matrix import ExecutionMatrix
from copy import deepcopy


def test_sort_tasks_return_task_sorted_by_min_deadline_first_when_tasks_provided():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = RateMonotonicPlanner(tasks)
    assert planner.sort_tasks(tasks)[0] == tasks[1]
    assert planner.sort_tasks(tasks)[1] == tasks[0]
    assert planner.sort_tasks(tasks)[2] == tasks[2]

def test_can_add_task_returns_true_when_task_not_executed_in_current_deadline():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = RateMonotonicPlanner(tasks)
    planner.matrix = ExecutionMatrix(planner.processors, planner.hyperperiod)
    planner.matrix.processors[0].add_time_unit()
    planner.matrix.processors[0].set_task(tasks[1])
    for x in range(tasks[1].deadline - 1):
        planner.matrix.processors[0].add_time_unit()
    assert planner.can_add_task(tasks[1], tasks[1].deadline)

def test_can_add_task_returns_false_when_task_was_executed_in_current_deadline_in_any_processor():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = RateMonotonicPlanner(tasks, 2)
    planner.matrix = ExecutionMatrix(planner.processors, planner.hyperperiod)
    planner.matrix.processors[0].add_time_unit()
    planner.matrix.processors[1].add_time_unit()
    planner.matrix.processors[0].set_task(tasks[1])
    for x in range(int(tasks[1].deadline / 2)):
        planner.matrix.processors[0].add_time_unit()
        planner.matrix.processors[1].add_time_unit()
    assert not planner.can_add_task(tasks[1], int(tasks[1].deadline / 2))

def test_is_task_with_same_id_in_list_returns_true_when_task_with_same_id_is_in_list():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = RateMonotonicPlanner(tasks)
    t_3_edited = deepcopy(tasks[2])
    t_3_edited.compute_time = 2
    t_list = [tasks[0], tasks[1], t_3_edited]
    assert planner.is_task_with_same_id_in_list(tasks[0], t_list)
    assert planner.is_task_with_same_id_in_list(tasks[1], t_list)
    assert planner.is_task_with_same_id_in_list(tasks[2], t_list)

def test_is_task_with_same_id_in_list_returns_false_when_task_with_same_id_is_not_in_list():
    tasks = [Task('T1', 30, 6), Task('T2', 20, 3), Task('T3', 120, 14)]
    planner = RateMonotonicPlanner(tasks)
    t_list = [tasks[0], tasks[1]]
    assert not planner.is_task_with_same_id_in_list(tasks[2], t_list)

def compare_each_processor_value(expected_by_processor, processors):
    for i in range(len(processors)):
        processor = processors[i]
        expected = expected_by_processor[i]
        for x in range(len(expected)):
            if processor.time_units[x] is None:
                assert expected[x] == ''
            else:
                assert processor.time_units[x].name == expected[x]

def test_get_plan_returns_cyclic_executive_planified_matrix_when_tasks_are_valids():
    # Case 1
    planner = RateMonotonicPlanner([Task('T1', 5, 2), Task('T2', 10, 3), Task('T3', 5, 1)], 1)
    matrix = planner.get_plan()
    expected = [['T1',  'T1',  'T3',  'T2', 'T2',  'T1',  'T1',  'T3',  'T2', '']]
    compare_each_processor_value(expected, matrix.processors)
    # Case 2
    planner = RateMonotonicPlanner([Task('T1', 5, 2), Task('T2', 10, 3), Task('T3', 5, 1)], 2)
    matrix = planner.get_plan()
    expected = [['T1',  'T1',  '',  '', '',  'T1',  'T1',  '',  '', ''],
                ['T3',  'T2',  'T2',  'T2', '',  'T3',  '',  '',  '', '']]
    compare_each_processor_value(expected, matrix.processors)
    # Case 3
    planner = RateMonotonicPlanner([Task('T1', 20, 3), Task('T2', 5, 2), Task('T3', 10, 2)], 1)
    matrix = planner.get_plan()
    expected = [['T2', 'T2', 'T3', 'T3', 'T1', 'T2', 'T2', 'T1', 'T1', '', 'T2', 'T2', 'T3', 'T3', '', 'T2', 'T2', '', '', '']]
    compare_each_processor_value(expected, matrix.processors)
    # Case 4
    planner = RateMonotonicPlanner([Task('T1', 20, 3), Task('T2', 5, 2), Task('T3', 10, 2)], 2)
    matrix = planner.get_plan()
    expected = [['T2', 'T2', 'T1', 'T1', 'T1', 'T2', 'T2', '', '', '', 'T2', 'T2', '', '', '', 'T2', 'T2', '', '', ''],
                ['T3', 'T3', '', '', '', '', '', '', '', '', 'T3', 'T3', '', '', '', '', '', '', '', '']]
    compare_each_processor_value(expected, matrix.processors)