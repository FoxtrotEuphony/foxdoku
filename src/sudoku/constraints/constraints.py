from dataclasses import dataclass
from enum import Enum, auto


class ConstraintType(Enum):
    pass


@dataclass(frozen=True)
class Constraint:
    type: ConstraintType
    cells: frozenset[tuple[int, int]]
