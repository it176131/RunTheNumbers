from .base import BaseProperty, check_price


class SingleFamilyHome(BaseProperty):
    """Single family home rental property instance."""

    def __init__(
        self,
        listing_price: float,
        bedrooms: int | None = None,
        bathrooms: float | None = None,
        square_feet: int | None = None,
        city: str | None = None,
        state: str | None = None,
        zip_cd: str | None = None,
    ):
        self.listing_price = listing_price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        super().__init__(
            square_feet=square_feet, city=city, state=state, zip_cd=zip_cd
        )
        self.one_percent = self.calculate_one_percent()
        self.cap_rate = self.calculate_cap_rate()

    # TODO -- swap multi-line string for single-line string with \n
    def __repr__(self):
        return f"""SingleFamilyHome(
    listing_price={self.listing_price},
    bedrooms={self.bedrooms},
    bedrooms={self.bathrooms},
    square_feet={self.square_feet},
    city={self.city},
    state={self.state},
    zip_cd={self.zip_cd},
)"""

    @check_price
    def calculate_one_percent(self, price: float | None = None) -> float:
        """Calculate 1% of ``price``.

        :param price: purchase price.
            If ``price`` is None, use ``listing_price``.
        :returns: one_percent
        """
        one_percent = 0.01 * price
        return one_percent

    @check_price
    def estimate_expenses(self, price: float | None = None) -> float:
        """Estimate annual property expenses.

        :param price: purchase price.
            If ``price`` is None, use ``listing_price``.
        :returns: estimated_expenses
        """
        # TODO -- determine formula for estimating expenses
        estimated_expenses = price * 0.01
        return estimated_expenses

    @check_price
    def calculate_cap_rate(
        self,
        price: float | None = None,
        rent_rate: float | None = None,
        expenses: float | None = None,
    ) -> float:
        """Calculate the cap rate.

        Formula:
        Cap Rate = (Gross Income - Expenses) / Purchase Price

        :param price: purchase price.
            If ``price`` is None, use ``listing_price``.
        :param rent_rate: monthly rent rate.
            Used to calculate gross income. If ``rent_rate`` is None,
            use ``one_percent`` of ``listing_price``.
        :param expenses: annual expenses for the property.
            e.g. insurance, taxes, utilities, property management, etc.
            If ``expenses` is None, use ``estimated_expenses`` based on
            ``listing_price``.
        :returns: cap_rate
        """
        if rent_rate is None:
            rent_rate = self.calculate_one_percent(price=price)
        if expenses is None:
            expenses = self.estimate_expenses(price=price)
        gross_income = rent_rate * 12
        cap_rate = (gross_income - expenses) / price
        return cap_rate
