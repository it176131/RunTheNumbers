from dataclasses import dataclass
from enum import Enum
from functools import wraps


class RoofMaterial(Enum):
    """Type of roof material."""

    Asphalt: str = "Asphalt"
    Wood: str = "Wood"
    Metal: str = "Metal"
    Clay: str = "Clay"
    Slate: str = "Slate"
    Other: str = "Other"


@dataclass(init=True, repr=True, eq=True)
class BaseProperty:
    """Base property instance.

    :param square_feet:
    :param city:
    :param state:
    :param zip_cd:
    """

    square_feet: float | None = None
    city: str | None = None
    state: str | None = None
    zip_cd: str | None = None


def check_price(method):
    """Decorator function to set ``price``.

    If ``price`` is None, set it to the instance's ``listing_price``.
    """

    @wraps(method)
    def wrapper(self, price: float | None = None, *args, **kwargs):
        if price is None:
            price = self.listing_price
        return method(self, price, *args, **kwargs)

    return wrapper
