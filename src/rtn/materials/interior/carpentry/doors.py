"""Ensure that every door works properly and as expected.

Verify the following:
    - Does the door open and close without obstructions?
    - Does the door latch properly without unnecessary force?
    - Does the door open in the expected direction?

If the existing doors are old or beat up, replace all the doors in the
house. When purchasing doors, you have the option of purchasing just
the door slab (the part that opens and closes) or a pre-hung door (the
slab attached to the doorjamb). While many investors are happy to save
a little money by just buying the slab, replacing a slab instead of the
entire jamb can be more work for your carpenter. Additionally, you'll
often end up paying extra to fix doors that aren't plumb or don't lock
properly.

It's highly recommended that when replacing a door, pay the few extra
bucks to get a pre-hung door. The carpenter will appreciate it, and
you'll save yourself some headaches, even if it costs a bit more.
"""

from enum import Enum

from pydantic.fields import Field
from pydantic.main import BaseModel


class DoorType(Enum):
    """Type of door.

    Can be one of the following:
      - Prehung
      - Slab
    """

    Prehung: str = "Prehung"
    Slab: str = "Slab"


class DoorStyle(Enum):
    """Style of the door.

    Can be one of the following:
      - Hinged
      - Barn
      - Glass
      - Closet
      - Bifold
      - Sliding
      - French
      - Pockets
    """

    Hinged: str = "Hinged"
    Barn: str = "Barn"
    Glass: str = "Glass"
    Closet: str = "Closet"
    Bifold: str = "Bifold"
    Sliding: str = "Sliding"
    French: str = "French"
    Pocket: str = "Pocket"


class TextureType(Enum):
    """Texture of the door.

    Can be one of the following:
      - Textured
      - Smooth
    """

    Textured: str = "Textured"
    Smooth: str = "Smooth"


class FinishType(Enum):
    """Finish of the door.

    Can be one of the following:
      - Finished
      - Primed
      - Stained
      - Unfinished
      - Painted
    """

    Finished: str = "Finished"
    Primed: str = "Primed"
    Stained: str = "Stained"
    Unfinished: str = "Unfinished"
    Painted: str = "Painted"


class DoorHanding(Enum):
    """Handing of the door.

    Can be one of the following:
      - Right
      - Left
      - Reversible
    """

    Right: str = "Right"
    Left: str = "Left"
    Reversible: str = "Reversible"


class LockFunction(Enum):
    """Lock function of a door knob.

    Can be one of the following:
      - Privacy (i.e., bed/bath)
      - Passage (i.e., hall/closet)
      - Unkeyed (i.e., non-functioning)
    """

    Privacy: str = "Privacy"
    Passage: str = "Passage"
    Unkeyed: str = "Unkeyed"


class LockStyle(Enum):
    """Style of the door lock.

    Can be one of the following:
      - Classic
      - Modern
      - Contemporary
      - Rustic
      - Antique
      - Vintage
    """

    Classic: str = "Classic"
    Modern: str = "Modern"
    Contemporary: str = "Contemporary"
    Rustic: str = "Rustic"
    Antique: str = "Antique"
    Vintage: str = "Vintage"


class StrikePlate(BaseModel):
    """Door strike plate."""

    cost: float
    brand: str
    color: str


class DoorKnob(BaseModel):
    """A door knob."""

    typ: LockFunction
    brand: str
    color: str
    style: LockStyle
    cost: float


class Door(BaseModel):
    """An interior door.

    A good carpenter can install an interior door in ~20 minutes.
    French and sliding glass doors may take two to three hours. The
    hourly rate a carpenter charges to install doors can be quite high.
    """

    cost: float
    material: str
    texture: TextureType
    panels: int = Field(ge=0, le=8)
    typ: DoorType
    style: DoorStyle
    brand: str
    height: float
    width: float
    finish: FinishType
    door_handing: DoorHanding
    door_knob: DoorKnob
    strike_plate: StrikePlate
