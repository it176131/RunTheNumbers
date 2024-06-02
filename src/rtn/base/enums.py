from enum import Enum


class RoofMaterial(Enum):
    """Type of roof material."""

    Asphalt: str = "Asphalt"
    Wood: str = "Wood"
    Metal: str = "Metal"
    Clay: str = "Clay"
    Slate: str = "Slate"
    Other: str = "Other"
