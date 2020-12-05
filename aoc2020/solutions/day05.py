import logging

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day05:
    @staticmethod
    def get_seat_id(row: int, col: int) -> int:
        return row * 8 + col

    @staticmethod
    def parse_line(line):
        lower, upper = 0, 127
        for c in line[:6]:
            lower, upper = Day05.split_range(lower, upper, c == 'F')

        if line[6] == 'F':
            row = lower
        else:
            row = upper

        lower, upper = 0, 7
        for c in line[7:9]:
            lower, upper = Day05.split_range(lower, upper, c == 'L')

        if line[9] == 'L':
            col = lower
        else:
            col = upper

        return row, col

    @staticmethod
    def split_range(lower, upper, lower_half=True):
        mid = (lower + upper) // 2
        if lower_half:
            return lower, mid

        return mid + 1, upper

class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str):
        ids = []
        for l in input_data.split('\n'):
            row, col = self.parse_line(l)
            seat_id = self.get_seat_id(row, col)
            logger.debug('%s: %d, %d -> %d', l, row, col, seat_id)
            ids.append(seat_id)

        return max(ids)

class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data):
        ids = {}
        for l in input_data.split('\n'):
            row, col = self.parse_line(l)
            seat_id = self.get_seat_id(row, col)

            logger.debug('%s: %d, %d -> %d', l, row, col, seat_id)

            ids[seat_id] = True

        seats_with_neighbours = filter(
            lambda k: ids.get(k - 1) and ids.get(k + 1),
            ids
        )

        sorted_seats = sorted(seats_with_neighbours)

        logger.debug('Lower seat ID = %d', sorted_seats[0])
        logger.debug('Upper seat ID = %d', sorted_seats[-1])

        all_seats = set(range(sorted_seats[0], sorted_seats[-1] + 1))

        return all_seats - set(sorted_seats)
