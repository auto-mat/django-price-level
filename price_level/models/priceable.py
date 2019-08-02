import datetime

from django.conf import settings
from django.db import models


class Pricable(models.Model):
    def get_current_price_level(
            self,
            date_time=None,
            category=settings.PRICE_LEVEL_CATEGORY_DEFAULT,
    ):
        if date_time is None:
            date_time = datetime.datetime.now()
        price_level_query = self.pricelevel_set.filter(
            takes_effect_on__lte=date_time,
            category=category,
        )
        price_level_query = price_level_query.order_by('-takes_effect_on')
        return price_level_query.first()

    class Meta:
        abstract = True

Priceable = Pricable
