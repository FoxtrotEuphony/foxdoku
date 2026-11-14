class Sudoku:
    def __init__(self, size: int) -> None:
        self._size: int = size

    @property
    def size(self):
        return self._size
