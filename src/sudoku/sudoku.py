from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override


class Constraint(ABC):
    @abstractmethod
    def valid_for_sudoku(self, sudoku: Sudoku) -> bool:
        raise NotImplementedError


@dataclass(frozen=True)
class Given(Constraint):
    cell: tuple[int, int]
    value: int

    @override
    def valid_for_sudoku(self, sudoku: Sudoku):
        return all(
            x in sudoku.number_range for x in (self.cell[0], self.cell[1], self.value)
        )


@dataclass(frozen=True)
class Sudoku:
    size: int
    constraints: frozenset[Constraint]

    @property
    def number_range(self) -> range:
        return range(1, self.size + 1)
