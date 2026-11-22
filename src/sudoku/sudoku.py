from abc import ABC, abstractmethod
from dataclasses import dataclass


class Constraint(ABC):
    @abstractmethod
    def __init__(self):
        pass


@dataclass(frozen=True)
class Sudoku:
    size: int
    givens: frozendict[tuple[int, int], int]
    constraints: frozenset[Constraint]

    @property
    def number_range(self) -> range:
        return range(1, self.size + 1)
