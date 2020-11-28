import json
import copy
from sys import *
from math import gcd
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
from collections import defaultdict
from .utils import lcm
from _distutils_hack import override


class Planner:

    def __init__(self ,tasks=[] , processors = 1):
        self.tasks = tasks
        self.processor = processors
        self.hyperperiod()


    def hyperperiod(self):
        """
            Calculates the hyper period of the tasks to be scheduled
        """
        self._hyperperiod = lcm([x.deadline for x in self.tasks])

    def get_plan(self):
        pass


class CyclicExecutivePlanner(Planner):

    def __init__(self ,tasks=[], processors = 1):
        super().__init__(tasks, processors)

    def secondary_period(self):
        pass

    @override
    def get_plan(self):
        """
        :return:
        """
        periods = []
        secondary_period = max([x.compute_time for x in self.tasks])


        while not self.validate_secondary_period(secondary_period):
            secondary_period +=1

        self._secondary_period = secondary_period


    def validate_secondary_period(self, sp):
        is_valid = False
        for t in self.tasks:
            # 2nd condition
            is_valid = is_valid or ((t.deadline / sp) - abs(t.deadline / sp) != 0)

            #3rd condition
            if (2*sp - lcm(sp , t.compute.time)) > t.deadline:
                return False

        return is_valid


class RateMonotonicPlanner(Planner):

    def __init__(self, list_task = []):
        self.list_task = list_task


    def count_list(self):
        return len(self.list_task)

