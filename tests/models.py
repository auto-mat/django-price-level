from django.db import models

from price_level.models import Priceable


class PriceableModel(Priceable, models.Model):
    pass
