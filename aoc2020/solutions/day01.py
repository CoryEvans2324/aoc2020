import logging
import math
from itertools import combinations

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day01:
    @staticmethod
    def compute_factor(input_data: str, n: int):
        numbers = [int(n) for n in input_data.splitlines()]
        for c in combinations(numbers, n):
            if sum(c) == 2020:
                logger.debug('Found values %s', c)
                return math.prod(c)

        return -1

class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data):
        return self.compute_factor(input_data, 2)

class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data):
        return self.compute_factor(input_data, 3)
