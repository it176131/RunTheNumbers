from datetime import date

from pydantic.main import BaseModel


class Roof(BaseModel):
    """Roof materials and costs."""

    material: str
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


class SepticSystem: ...


class Foundation: ...


class Demo: ...


class Plumbing: ...


class Electrical: ...


class HVAC: ...


class Framing: ...


class Insulation: ...


class Sheetrock: ...


class Doors: ...


class Windows: ...


class Trim: ...


class InteriorPaint: ...


class CabinetsAndCountertops: ...


class Flooring: ...


class Permits: ...


class Mold: ...


class Termites: ...


class Miscellaneous: ...
