from dataclasses import dataclass

from .constraints import Constraint


@dataclass(frozen=True)
class Sudoku:
    size: int
    givens: frozendict[tuple[int, int], int]
    constraints: frozenset[Constraint]

    @property
    def number_range(self) -> range:
        return range(1, self.size + 1)
