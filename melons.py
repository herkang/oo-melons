
"""Classes for melon orders."""

import random
import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):

        # base_price = random.randrange(5, 10)

        # time_now = datetime.datetime.now()

        today = datetime.date.today()

        #TODO test time.time()
        time = datetime.time

        print(time)

        # return base_price

    def get_total(self):
        """Calculate price, including tax."""
        
        base_price = self.get_base_price()
        
        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty <10:
            total = total + 3

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class GovernmentMelonOrder(AbstractMelonOrder):
    """ A melon order for the government. """
    
    def __init__(self, species, qty):
        super().__init__(sepcies, qty, "domestic", 0.0)
        self.passed_inspection = False
    
    def mark_inspection(self, passed):
        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        self.country_code = country_code
  
  
    def get_country_code(self):
        return self.country_code