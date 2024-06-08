"""Carpentry can make or break a house.

Great carpentry makes a house feel well put together, while poor
carpentry will make a buyer (or renter) question every part of the
renovation. A good carpenter can serve in many different roles and can
replace a lot of other contractors.

But other than framing and decks, the bread and butter of carpentry
work consists of things like door installations, window installations,
and finish trim work. These are renovation tasks you'll likely have to
perform in every one of your houses, so find a good carpenter sooner
rather than later, and you'll find your renovations going more quickly
and more smoothly than you can imagine. Bring in a bad carpenter, and
all you'll find is frustration and a questionable looking renovation.

This ``carpentry`` package will hold the bread-and-butter carpentry
tasks:
    - Install doors
    - Install windows
    - Finish trim

There are many tasks on a renovation that a good carpenter can perform.
In fact, a carpenter can be thought of as a jack of all trades who can
generally do not only all the wood-related work, but also all the stuff
that may not require a specialty carpenter. For example, mounting the
microwave, installing appliances, mounting mirrors in bathrooms,
installing backsplash behind kitchen counters, and installing doorknobs
and mini blinds.

While a handyman can do a lot of these tasks and a carpenter will cost
a little bit more, his work will generally be cleaner than the
handyman's. The other nice thing about using a carpenter for these
types of tasks is that if and when he runs into an issue, he's likely
more equipped to come up with a creative solution that most other
contractors.
"""

from pydantic.main import BaseModel


class Carpenter(BaseModel):
    """A good carpenter isn't cheap.

    But given that great carpentry can sell (or rent) a house and bad
    carpentry can keep you from selling (or renting) a house, he is
    worth every penny. If your carpenter has an apprentice, expect to
    pay less for the apprentice's time than the carpenter's, depending
    on how skilled he is.
    """

    ...
