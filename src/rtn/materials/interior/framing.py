"""Framing.

The two most common costs associated with framing are finishing an
interior space and building new construction. This module represents
framing an *interior space*, e.g., finishing an unfinished space or
adding partitions within rooms.

A basic wall consists of three parts:
    1. Bottom Plate := A 2x4 piece of lumber running horizontally along
        the bottom of the wall.
    2. Top Plates := Two 2x4 pieces of lumber running horizontally
        along the top of the wall.
    3. Studs := 2x4 pieces of lumber running vertically every 16".
"""

from pydantic.fields import computed_field
from pydantic.main import BaseModel


class Plate:
    """A 2x4 piece of lumber running horizontally."""


class Wall(BaseModel):
    """A basic wall.

    A wall is made of a bottom plate, a top plate, and studs.
    """

    length: float

    @computed_field  # type: ignore[misc]
    @property
    def number_of_studs(self) -> float:
        """The number of studs needed for the :class:``Wall``."""
        inches = self.length * 12
        spacing = 16.0
        return inches / spacing + 1


class Framing:
    """Interior framing materials."""

    ...
