import datetime

from django.conf import settings
from django.db import models
from django.db.models import Q


class Pricable(models.Model):
    def get_current_price_levels(
            self,
            date_time=None,
            category=settings.PRICE_LEVEL_CATEGORY_DEFAULT,
    ):
        if date_time is None:
            date_time = datetime.datetime.now()
        price_level_query = self.pricelevel_set.filter(
            Q(offer_ends__gte=date_time)|Q(offer_ends=None),
            takes_effect_on__lte=date_time,
            category=category,
        )
        return price_level_query

    def get_current_price_level(self, *args, **kwargs):
        price_level_query = self.get_current_price_levels(*args, **kwargs)
        return price_level_query.order_by('-takes_effect_on').first()

    class Meta:
        abstract = True

Priceable = Pricable
