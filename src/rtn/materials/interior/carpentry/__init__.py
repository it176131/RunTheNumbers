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

    Depending on whether your carpenter charges by the hour or by the
    task will ultimately determine what you're paying for a job (by the
    hour is often cheaper if your carpenter is reliable and works
    diligently). Because a carpenter's job will be pretty diverse on a
    particular day, until you actually sit down and work through a
    specific scope of work, it will be hard to determine the price for
    individual tasks.

    For example, one carpenter might take 15 minutes to install an
    interior door and another might take 30 minutes. If they were to
    charge by the task, the prices for each would likely be pretty
    close. But if they charged hourly, the slower carpenter would cost
    about twice as much. Therefore, it would seem like an hourly wage
    is better. But each project will have its challenges, and if a big
    challenge comes up that requires a large amount of time to fix,
    paying an hourly wage could end up being the more expensive option.
    There are risks and trade-offs with each method, though I tend to
    prefer to get a fixed price bid on each job based on the specific
    list of tasks.

    Carpenters tend to be on the job for relatively long periods of
    time, so paying them on a weekly basis, or after completing certain
    milestones, is how payment is typically handled. You should be
    prepared to provide all material, though a good carpenter will have
    connections to local lumberyards and supply houses and should be
    able to get most of the material delivered to the project.
    """

    name_first: str
    name_last: str
    hourly_rate: float
    task_rate: float
