from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override


class Constraint(ABC):
    @abstractmethod
    def valid_for_sudoku(self, sudoku: Sudoku) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __hash__(self) -> int:
        raise NotImplementedError


@dataclass(frozen=True)
class Given(Constraint):
    cell: tuple[int, int]
    value: int

    @override
    def valid_for_sudoku(self, sudoku: Sudoku) -> bool:
        return all(
            x in sudoku.number_range for x in (self.cell[0], self.cell[1], self.value)
        )

    @override
    def __eq__(self, other: object) -> bool:
        if isinstance(object, Given):
            return other.cell == self.cell and other.value == self.value  # ty: ignore[missing-attribute]
        else:
            return False

    @override
    def __hash__(self) -> int:
        return hash((self.cell, self.value))


@dataclass(frozen=True)
class UniqueRegion(Constraint):
    cells: set[tuple[int, int]]

    @override
    def valid_for_sudoku(self, sudoku: Sudoku) -> bool:
        return all(
            x in sudoku.number_range and y in sudoku.number_range for x, y in self.cells
        )

    @override
    def __eq__(self, other: object) -> bool:
        return isinstance(other, UniqueRegion) and self.cells == other.cells

    @override
    def __hash__(self) -> int:
        return hash(self.cells)


class Sudoku:
    def __init__(self, size: int, constraints: list[Constraint]):
        if not size > 0:
            raise ValueError("Size must be positive")

        if not all(c.valid_for_sudoku(self) for c in constraints):
            raise ValueError("Constraints must be valid for given size")

        self._size = size
        self._constraints = constraints

    @property
    def size(self) -> int:
        return self._size

    @property
    def constraints(self) -> list[Constraint]:
        return self._constraints.copy()

    @property
    def number_range(self) -> range:
        return range(1, self.size + 1)
