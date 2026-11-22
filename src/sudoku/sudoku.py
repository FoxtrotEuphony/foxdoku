from abc import ABC, abstractmethod
from dataclasses import dataclass


class Constraint(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Given(Constraint):
    def __init__(self, cell: tuple[int, int], value: int):
        self._cell = cell
        self._value = value


@dataclass(frozen=True)
class Sudoku:
    size: int
    constraints: frozenset[Constraint]

    @property
    def number_range(self) -> range:
        return range(1, self.size + 1)
