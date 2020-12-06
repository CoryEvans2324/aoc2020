import logging
from string import ascii_lowercase

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day06:
    @staticmethod
    def count_group(data: str) -> set:
        length = len(set(data.replace('\n', '')))
        # logger.debug('length -> %d', length)
        return length

class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data):
        group_counts = []
        for g_str in input_data.split('\n\n'):
            group_counts.append(
                self.count_group(g_str)
            )
        return sum(group_counts)

class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data):
        group_counts = []

        for g_str in input_data.split('\n\n'):
            questions = set(ascii_lowercase)
            for person in g_str.split('\n'):
                questions.intersection_update(set(person))

            # logger.debug(str(questions))
            group_counts.append(len(questions))

        return sum(group_counts)
