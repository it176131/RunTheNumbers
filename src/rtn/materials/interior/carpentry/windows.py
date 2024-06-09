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

from pydantic.main import BaseModel


class Window(BaseModel):
    """Window replacement.

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
