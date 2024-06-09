"""Finish trim.

Finish trim generally includes the following:
    - Baseboard and shoe molding
    - Crown molding
    - Door casing
    - Window casing
"""

from pydantic.main import BaseModel


class Trim(BaseModel):
    """Finish trim.

    Labor cost is based on square footage of the house while material
    cost is based on the linear feet of actual trim to be installed.

    To trim out a full house, many carpenters will charge based on the
    square footage of the house as opposed to the specific amount of
    trim you plan to use. This means you may pay the same price
    regardless of whether you put crown molding in every room or none
    of them.

    Prices are typically for medium to large jobs that will take
    several days or more, such as trimming an entire house. For smaller
    jobs, you can base the labor price off the hourly price of your
    carpenter.
    """

    cost: float
    house_square_footage: float
    linear_footage: float
