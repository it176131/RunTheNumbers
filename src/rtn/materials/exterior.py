from datetime import date

from pydantic.main import BaseModel

from ..base.enums import RoofMaterial


class Roof(BaseModel):
    """Roof materials and costs."""

    material: RoofMaterial
    cost: float
    life_expectancy: tuple[int, int]
    install_date: date | None
    current_age: float
    is_damaged: bool
    tree_coverage: bool
    square_footage: float


class Gutters: ...


class Soffit: ...


class Fascia: ...


class Siding: ...


class ExteriorPaint: ...


class DecksAndPorches: ...


class Concrete: ...


class Garage: ...


class Landscaping: ...


class Foundation: ...
