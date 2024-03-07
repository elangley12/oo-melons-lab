"""Classes for melon orders."""


class DomesticMelonOrder:
    """A melon order within the USA."""
    
    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder:
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = "international"

    def __init__(self, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    # order_type = None
    # tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True