"""Ensure that every window works properly and as expected.

Verify the following:
    - Does it open smoothly and easily?
    - Does it remain open without assistance?
    - Does it close and latch without any unnecessary force?
    - Are the panes of glass free from cracks and moisture?
    - Are there any gaps or openings around the window?

Windows come in all different shapes, sizes, and styles. It is highly
recommended you spend some time looking at different types of windows
and getting a feel for the style of windows that are typical in the
houses you plan to renovate.
"""

from enum import Enum

from pydantic.main import BaseModel


class WindowStyle(Enum):
    """Style of the window.

    Can be one of the following:
      - Single
      - Double
      - Sliding
      - Casement
      - Picture
      - Bay
      - Skylight
      - Awning
      - GlassBlock
      - Hopper
    """

    Single: str = "Single"
    Double: str = "Double"
    Sliding: str = "Sliding"
    Casement: str = "Casement"
    Picture: str = "Picture"
    Bay: str = "Bay"
    Skylight: str = "Skylight"
    Awning: str = "Awning"
    GlassBlock: str = "GlassBlock"
    Hopper: str = "Hopper"


class FrameMaterial(Enum):
    """Material of the window frame.

    Can be one of the following:
      - Vinyl
      - Aluminum
      - WoodClad
      - Composite
    """

    Vinyl: str = "Vinyl"
    Aluminum: str = "Aluminum"
    WoodClad: str = "WoodClad"
    Composite: str = "Composite"


class WindowUse(Enum):
    """What the window will be used for.

    Can be one of the following:
      - Replacement
      - NewConstruction

    New construction windows have additional parts that allow them to
    attach to a wall's wooden frame. Replacement windows don't have
    these parts because the frame is already in place.
    """

    Replacement: str = "Replacement"
    NewConstruction: str = "NewConstruction"


class Glazing(Enum):
    """Glazing type of the window, i.e., the number of panes.

    Can be one of the following:
      - SinglePane
      - DoublePane
      - TriplePane
    """

    SinglePane: str = "SinglePane"
    DoublePane: str = "DoublePane"
    TriplePane: str = "TriplePane"


class GlassType(Enum):
    """Type of glass for the window.

    Can be one of the following:
      - Privacy
      - LowEnergy
      - Insulated
      - Standard
      - EnergyEfficient
      - Patterned
      - Tempered
      - Tinted
      - Toughened
    """

    Privacy: str = "Privacy"
    LowEnergy: str = "LowEnergy"
    Insulated: str = "Insulated"
    Standard: str = "Standard"
    EnergyEfficient: str = "EnergyEfficient"
    Patterned: str = "Patterned"
    Tempered: str = "Tempered"
    Tinted: str = "Tinted"
    Toughened: str = "Toughened"


class Window(BaseModel):
    """A Window.

    Standard double-hung replacement windows come in a variety of sizes,
    styles, and qualities. For most low- to mid-level renovations, it is
    recommended to use stock vinyl windows that can be purchased from a
    big-box store or ordered through a local window company.

    You'll likely find that using the window company to install the
    windows will cost quite a bit more than having a carpenter do the
    installation. It is suggested to find a professional window
    installer looking for side work at night or on weekends and pay him
    an hourly rate for installation. Professional installers can
    replace windows very quickly, and paying hourly will keep the
    per-window price to a minimum.
    """

    cost: float
    brand: str
    style: WindowStyle
    frame_material: FrameMaterial
    window_use_type: WindowUse
    glazing: Glazing
    glass_type: GlassType
    interior_color: str
    exterior_color: str
