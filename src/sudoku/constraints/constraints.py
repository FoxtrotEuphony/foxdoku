from enum import Enum, auto


class ConstraintType(Enum):
    pass


class Constraint:
    def __init__(self, type: ConstraintType, cells: set[tuple[int, int]]) -> None:
        self._cells: set[tuple[int, int]] = cells

    @property
    def cells(self):
        return self._cells.copy()
