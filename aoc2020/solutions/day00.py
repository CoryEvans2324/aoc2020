import logging

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day00:
    @staticmethod
    def run(input_data: str):
        print(input_data)
        return -1

class Day00PartA(Day00, FileReaderSolution):
    def solve(self, input_data):
        return self.run(input_data)

class Day00PartB(Day00, FileReaderSolution):
    def solve(self, input_data):
        return self.run(input_data)
