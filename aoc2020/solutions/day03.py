import logging
import math

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day03:
    @staticmethod
    def run(input_data, row_step, col_step):
        grid = Map(input_data)
        return grid.count(row_step, col_step)

class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data):
        return self.run(input_data, 1, 3)

class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data):
        slops = [
            (1, 1),
            (1, 3),
            (1, 5),
            (1, 7),
            (2, 1)
        ]
        results = []
        for slop in slops:
            results.append(
                self.run(input_data, slop[0], slop[1])
            )

        return math.prod(results)


class Map:
    def __init__(self, raw_map: str) -> None:

        self.grid = raw_map.strip().splitlines()
        self.row_width = len(self.grid[0])

        self.num_of_rows = len(self.grid)


    def is_tree_at_pos(self, row, col):
        return self.grid[row][col % self.row_width] == '#'

    def count(self, row_step, col_step) -> int:
        row_counter = 0
        col_counter = 0

        tree_counter = 0

        while row_counter < self.num_of_rows - 1:
            row_counter += row_step
            col_counter += col_step

            if self.is_tree_at_pos(row_counter, col_counter):
                tree_counter += 1

        return tree_counter
