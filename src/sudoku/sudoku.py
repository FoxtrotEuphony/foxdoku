from .constraints import Constraint


class Sudoku:
    def __init__(
        self,
        size: int,
        givens: dict[tuple[int, int], int],
        constraints: list[Constraint],
    ) -> None:
        if not all(self._is_valid_givens(size, entry) for entry in givens.items()):
            raise ValueError(
                f"All values in argument givens must be in range 1 to {size} (argument size) inclusive"
            )
        self._size: int = size
        self._givens: dict[tuple[int, int], int] = givens
        self._constraints: list[Constraint] = constraints

    @staticmethod
    def _is_valid_givens(size: int, entry: tuple[tuple[int, int], int]):
        (x, y), v = entry
        return (
            x in range(1, size + 1)
            and y in range(1, size + 1)
            and v in range(1, size + 1)
        )

    @property
    def size(self):
        return self._size

    @property
    def number_range(self):
        return set(range(1, self._size + 1))

    @property
    def givens(self):
        return self._givens.copy()

    @property
    def constraints(self):
        return self._constraints.copy()
