from abc import ABC, abstractmethod
from pathlib import Path
from typing import Union

import logging

logger = logging.getLogger(__name__)

class AbstractSolution:

    @abstractmethod
    def solve(self, input_data: str) -> Union[str, int]:
        raise NotImplementedError


class SimpleSolution(AbstractSolution, ABC):

    def __call__(self, input_text: str) -> Union[str, int]:
        result = self.solve(input_text)
        return result


class FileReaderSolution(AbstractSolution, ABC):

    def __call__(self, input_file: str) -> Union[str, int]:
        root_dir = Path(__file__).parent.parent
        logger.debug('FileReaderSolution: %s', root_dir)
        logger.debug('FileReaderSolution: %s', input_file)
        with open(root_dir / 'solutions' / 'data' / input_file) as f:
            input_data = f.read().strip()

        result = self.solve(input_data)
        return result
