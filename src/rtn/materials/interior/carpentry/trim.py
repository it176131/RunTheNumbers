"""Finish trim.

Finish trim generally includes the following:
    - Baseboard and shoe molding
    - Crown molding
    - Door casing
    - Window casing
"""

from enum import Enum

from pydantic.fields import computed_field

from ....base import BaseModel


class TrimType(str, Enum):
    """Type of trim.

    Can be one of the following:
      - Baseboard
      - CrownMolding
      - DoorCasing
      - WindowCasing
    """

    Baseboard: str = "Baseboard"
    CrownMolding: str = "CrownMolding"
    DoorCasing: str = "DoorCasing"
    WindowCasing: str = "WindowCasing"


class MoldingUse(str, Enum):
    """Use of the molding.

    Can be one of the following:
      - Door
      - Window
      - Floor
      - Ceiling
      - General
    """

    Door: str = "Door"
    Window: str = "Window"
    Floor: str = "Floor"
    Ceiling: str = "Ceiling"
    General: str = "General"


class MoldingMaterial(str, Enum):
    """Material the molding is made of.

    Can be one of the following:
      - StainlessSteel
      - Polyurethane
      - Aluminum
      - SolidWood
      - Wood
      - PVC
      - Acrylic
      - Composite
      - Steel
      - Vinyl
      - WhiteOak
      - Hickory
      - Maple
      - Bamboo
      - Laminate
      - MDF, i.e., Medium Density Fiberboard
      - Plastic
      - Polystyrene
      - Polymer
      - Fiberglass
    """

    StainlessSteel: str = "StainlessSteel"
    Polyurethane: str = "Polyurethane"
    Aluminum: str = "Aluminum"
    SolidWood: str = "SolidWood"
    Wood: str = "Wood"
    PVC: str = "PVC"
    Acrylic: str = "Acrylic"
    Composite: str = "Composite"
    Steel: str = "Steel"
    Vinyl: str = "Vinyl"
    WhiteOak: str = "WhiteOak"
    Hickory: str = "Hickory"
    Maple: str = "Maple"
    Bamboo: str = "Bamboo"
    Laminate: str = "Laminate"
    MDF: str = "MDF"
    Plastic: str = "Plastic"
    Polystyrene: str = "Polystyrene"
    Polymer: str = "Polymer"
    Fiberglass: str = "Fiberglass"


class FinishType(str, Enum):
    """Type of trim finish.

    Can be one of the following:
      - Primed
      - Unfinished
      - Finished
      - Painted
      - Stained
    """

    Primed: str = "Primed"
    Unfinished: str = "Unfinished"
    Finished: str = "Finished"
    Painted: str = "Painted"
    Stained: str = "Stained"


class InstallationType(str, Enum):
    """Type of trim installation.

    Can be one of the following:
      - Nail
      - Glue
      - Adhesive
      - Screw
      - PeelAndStick
      - Clip
      - Staple
      - Interlocking
      - ClickInterlocking
      - FullyBondedAdhesive
      - PerimeterBondAdhesive
    """

    Nail: str = "Nail"
    Glue: str = "Glue"
    Adhesive: str = "Adhesive"
    Screw: str = "Screw"
    PeelAndStick: str = "PeelAndStick"
    Clip: str = "Clip"
    Staple: str = "Staple"
    Interlocking: str = "Interlocking"
    ClickInterlocking: str = "ClickInterlocking"
    FullyBondedAdhesive: str = "FullyBondedAdhesive"
    PerimeterBondAdhesive: str = "PerimeterBondAdhesive"


class Durability(str, Enum):
    """Durability of the trim.

    Can be one of the following:
      - MoistureResistant
      - RotResistant
      - TermiteResistant
      - NotApplicable
      - SplitResistant
      - RustResistant
      - ScratchResistant
      - Tempered
    """

    MoistureResistant: str = "MoistureResistant"
    RotResistant: str = "RotResistant"
    TermiteResistant: str = "TermiteResistant"
    NotApplicable: str = "NotApplicable"
    SplitResistant: str = "SplitResistant"
    RustResistant: str = "RustResistant"
    ScratchResistant: str = "ScratchResistant"
    Tempered: str = "Tempered"


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

    cost_per_foot: float
    brand: str
    house_square_footage: float
    linear_footage: float
    width: float
    color: str
    trim_type: TrimType
    molding_use: MoldingUse
    material: MoldingMaterial
    finish_type: FinishType
    installation_type: InstallationType
    durability: Durability

    @computed_field  # type: ignore[misc]
    @property
    def total_cost(self) -> float:
        """Total cost of trim.

        Cost is calculated using :attribute:``Trim.cost_per_foot`` and
        :attribute:``Trim.linear_footage``.
        """
        return self.cost_per_foot * self.linear_footage
