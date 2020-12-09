import logging

from aoc2020.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

class Day08:
    @staticmethod
    def parse_line(line: str):
        instruction, value = line.split(' ')

        return instruction, int(value)

class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data):
        program_mem = []

        for l in input_data.split('\n'):
            program_mem.append(Day08.parse_line(l))

        instruction_pointer = 0
        register = 0
        history = []

        while instruction_pointer < len(program_mem) - 1:
            instruction, value = program_mem[instruction_pointer]

            if instruction_pointer in history:
                return register

            history.append(instruction_pointer)

            if instruction == 'acc':
                register += value

            elif instruction == 'jmp':
                instruction_pointer += value
                continue

            # nop or acc at this point
            instruction_pointer += 1

        return register

class Day08PartB(Day08, FileReaderSolution):
    def run_program(self, program_mem):
        instruction_pointer = 0
        register = 0
        history = []

        while instruction_pointer < len(program_mem) - 1:
            instruction, value = program_mem[instruction_pointer]

            if instruction_pointer in history:
                print('\n'.join([
                    f'{i+1}: {program_mem[i]}' for i in history[-10:]
                ]))
                return False, register

            history.append(instruction_pointer)

            if instruction == 'acc':
                register += value

            elif instruction == 'jmp':
                instruction_pointer += value
                continue

            # nop or acc at this point
            instruction_pointer += 1

        return True, register

    def solve(self, input_data):
        program_mem = []

        for l in input_data.split('\n'):
            program_mem.append(Day08.parse_line(l))

        for instruction_pointer, v in enumerate(program_mem):
            instruction, value = v
            if instruction == 'jmp':
                new_instruction = 'nop'
            elif instruction == 'nop':
                new_instruction = 'jmp'
            else:
                continue

            new_program = program_mem.copy()
            new_program[instruction_pointer] = (new_instruction, value)

            program_terminated, register_value = self.run_program(new_program)
            if program_terminated:
                logger.debug('changed %s to %s at line #%d', f'{instruction} {value}', f'{new_instruction} {value}', instruction_pointer + 1)
                return register_value
