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

from pydantic.main import BaseModel


class DoorType(Enum):
    """Type of door.

    Can be one of the following:
      - Prehung
      - Slab
    """

    Prehung: str = "Prehung"
    Slab: str = "Slab"


class DoorStyle:
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


class Door(BaseModel):
    """A good carpenter can install an interior door in ~20 minutes.

    French and sliding glass doors may take two to three hours. The
    hourly rate a carpenter charges to install doors can be quite high.
    """

    cost: float
    material: str
    typ: DoorType
    style: DoorStyle
    brand: str
    height: float
    width: float
