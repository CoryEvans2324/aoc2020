import logging
import re

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day02:
    pass

class Day02PartA(Day02, FileReaderSolution):
    def solve(self, input_data):
        def parse_line(line):
            # logger.debug(line)
            m = re.search(
                r'(\d+)-(\d+) ([a-z]): ([a-z]+)',
                line
            )

            policy_min = int(m.group(1))
            policy_max = int(m.group(2))
            policy_char = m.group(3)
            password = m.group(4)

            count = password.count(policy_char)
            return policy_min <= count and count <= policy_max


        valid = 0
        for line in input_data.splitlines():
            if parse_line(line):
                valid += 1

        return valid


class Day02PartB(Day02, FileReaderSolution):
    def solve(self, input_data):

        def parse_line(line):
            # logger.debug(line)
            m = re.search(
                r'(\d+)-(\d+) ([a-z]): ([a-z]+)',
                line
            )

            policy_first_index = int(m.group(1))
            policy_next_index = int(m.group(2))
            policy_char = m.group(3)
            password = m.group(4)

            count = 0
            if password[policy_first_index - 1] == policy_char:
                count += 1

            if password[policy_next_index - 1] == policy_char:
                count += 1

            return count == 1


        valid = 0
        for line in input_data.splitlines():
            if parse_line(line):
                valid += 1

        return valid
