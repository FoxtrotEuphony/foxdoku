from .constraints import Constraint


class Sudoku:
    def __init__(
        self,
        size: int,
        givens: frozendict[tuple[int, int], int],
        constraints: frozenset[Constraint],
    ) -> None:
        self._size: int = size
        self._givens: frozendict[tuple[int, int], int] = givens
        self._constraints: frozenset[Constraint] = constraints

    @property
    def size(self):
        return self._size

    @property
    def number_range(self):
        return set(range(1, self._size + 1))

    @property
    def givens(self):
        return self._givens

    @property
    def constraints(self):
        return self._constraints
