from dataclasses import dataclass
from functools import wraps

from pydantic.config import ConfigDict
from pydantic.main import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    """Global config for BaseModel."""

    model_config = ConfigDict(
        # Track extra arguments in the :attribute:``model_extra``.
        extra="allow",
        # Allow population via alias or parameter name.
        populate_by_name=True,
        # Use enums by default.
        use_enum_values=True,
    )


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
