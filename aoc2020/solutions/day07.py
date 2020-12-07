import logging
import re
from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day07:
    init_search = re.compile(r'([a-z| ]+) bags contain (.+).')
    contains_search = re.compile(r'(\d+) ([a-z| ]+) bags?')

    def parse_line(self, line: str):
        m = re.search(self.init_search, line)

        color = m.group(1)
        contains = self.parse_contains(m.group(2))

        return color, contains

    def parse_contains(self, contains: str):
        bags = {}
        for m in re.finditer(self.contains_search, contains):
            amount = int(m.group(1))
            color = m.group(2)

            bags[color] = amount

        return bags

    def can_contain_bag(self, all_bags, bag, search_color='shiny gold'):
        for sub_bag in all_bags[bag]:
            if sub_bag == search_color or \
                 self.can_contain_bag(all_bags, sub_bag, search_color):
                return True

        return False

class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str):
        bags = {}
        for line in input_data.split('\n'):
            new_c, contains = self.parse_line(line)
            bags[new_c] = contains

        count = 0

        for b in bags:
            if self.can_contain_bag(bags, b):
                count += 1

        return count

class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str):
        bags = {}
        for line in input_data.split('\n'):
            new_c, contains = self.parse_line(line)
            bags[new_c] = contains


        count = 0
        to_count = [('shiny gold', 1)]
        while to_count:
            color, amount = to_count.pop()

            count += amount
            for color_i, amount_i in bags[color].items():
                to_count.append((color_i, amount_i * amount))


        return count - 1
