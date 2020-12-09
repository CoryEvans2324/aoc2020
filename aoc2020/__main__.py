import importlib
import logging
import sys
import timeit
import argparse
import tqdm

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(
        description='Usage: %(prog)s',
        prog=sys.argv[0],
        add_help=True
    )

    parser.add_argument('-d', '--day', type=int, required=True)
    parser.add_argument('-t', '--timeit', type=int)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    parser.add_argument('-e', '--example-input', action='store_true', default=False, dest='example_input')

    args = parser.parse_args()

    if args.verbose:
        level = logging.DEBUG
    else:
        level = logging.WARNING

    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

    if args.timeit:
        times = []
        result = []
        for _ in tqdm.trange(args.timeit):
            time_start = timeit.default_timer()

            result = run_day(args.day, args.example_input)

            time_end = timeit.default_timer()
            times.append(time_end - time_start)

        avg_time = sum(times) / len(times)

        if avg_time < 0.1:
            unit = 'ms'
            avg_time *= 1000

        else:
            unit = 's'

        print(
            f'Average run time: {avg_time:.6f}{unit} for {args.timeit} iterations'
        )

    else:
        result = run_day(args.day, args.example_input)

    day_str = f'day{args.day:02}'
    print(f'{day_str} Part A: {result[0]}')
    print(f'{day_str} Part B: {result[1]}')

def run_day(day: int, use_example_input: bool):
    day_str = f'day{day:02}'

    import_path = f'aoc2020.solutions.{day_str}'
    if use_example_input:
        data_path = f'{day_str}/example.txt'
    else:
        data_path = f'{day_str}/input.txt'

    logger.debug('Import Path: %s', import_path)
    logger.debug('Data Path:   %s', data_path)

    try:
        day_module = importlib.import_module(import_path)
    except ModuleNotFoundError:
        logger.error('Module %s not found. . . exiting', day_str)
        sys.exit(-1)

    ra = run_part(day, 'A', day_module, data_path)
    rb = run_part(day, 'B', day_module, data_path)

    return ra, rb


def run_part(day: int, part: str, day_module, data_path):

    if part == 'A':
        attr = f'Day{day:02}PartA'
    else:
        attr = f'Day{day:02}PartB'

    result = getattr(day_module, attr)()(data_path)
    return result

if __name__ == '__main__':
    main()
