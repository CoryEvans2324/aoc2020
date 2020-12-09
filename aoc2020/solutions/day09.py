import logging

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day09:
    @staticmethod
    def check_number(n, previous_numbers):
        for v in previous_numbers:
            if n - v in previous_numbers:
                return True

        return False


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data):
        numbers = [int(i) for i in input_data.split('\n')]
        preamble_length = 25

        index = preamble_length
        while index < len(numbers):
            number_to_check = numbers[index]
            if not self.check_number(number_to_check, numbers[index - preamble_length : index]):
                return number_to_check

            index += 1


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data):
        numbers = [int(i) for i in input_data.split('\n')]
        invalid_number = 69316178

        assert invalid_number in numbers

        for i, n in enumerate(numbers[:-1]):
            s = n
            contiguous_numbers = [n]

            for other in numbers[i + 1:]:
                s += other
                contiguous_numbers.append(other)

                if s == invalid_number:
                    logger.debug('%d, %d', n, other)
                    return min(contiguous_numbers) + max(contiguous_numbers)
