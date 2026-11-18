from dataclasses import dataclass
from enum import Enum, auto


class ConstraintType(Enum):
    pass


@dataclass(frozen=True)
class Constraint:
    constraint_type: ConstraintType
    cells: frozenset[tuple[int, int]]


@dataclass(frozen=True)
class Sudoku:
    size: int
    givens: frozendict[tuple[int, int], int]
    constraints: frozenset[Constraint]

    @property
    def number_range(self) -> range:
        return range(1, self.size + 1)
